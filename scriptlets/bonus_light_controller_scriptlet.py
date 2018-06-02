from mpf.core.scriptlet import Scriptlet
from mpf.devices.light import Light
from mpf.core.device_manager import DeviceCollectionType

lights = None  # type: DeviceCollectionType[str, Light]


class BonusLightController(Scriptlet):

    def on_load(self):
        self.debug_log("Bonus Light Controller scriptlet loaded!")
        BonusLightController.lights = self.machine.lights.items_tagged('bonus_light')
        self.debug_log("{} bonus lights being managed.".format(BonusLightController.lights.__len__()))
        self.machine.events.add_handler('player_bonuscount', self._handle_bonus_change, 10000)

    def _handle_bonus_change(self, **kwargs):
        intvalue = kwargs.get("value")
        fade = 0 if kwargs.get("change") < 0 else None

        if intvalue > 511:
            intvalue = 511

        binary = '{0:09b}'.format(intvalue)

        for x in range(9):
            if binary[8-x] == '1':
                self._get_bonus_light_by_number(x).on(fade_ms=fade, priority=1000)
            else:
                self._get_bonus_light_by_number(x).off(fade_ms=fade, priority=1000)

    @staticmethod
    def _get_bonus_light_by_number(num: int):
        for light in BonusLightController.lights:
            if light.tags.__contains__('bonus{}'.format(num)):
                return light



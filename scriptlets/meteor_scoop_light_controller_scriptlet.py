from mpf.core.scriptlet import Scriptlet
from mpf.devices.light import Light
from mpf.core.device_manager import DeviceCollectionType

lights = None  # type: DeviceCollectionType[str, Light]


class MeteorScoopLightController(Scriptlet):

    def on_load(self):
        self.debug_log("Meteor Scoop Light Controller scriptlet loaded!")
        MeteorScoopLightController.lights = self.machine.lights.items_tagged('scoop_light')
        self.machine.events.add_handler('timer_meteortimer_started', self._initialize(), 10000)
        self.machine.events.add_handler('timer_meteortimer_tick', self._flash_scoop_light(), 10000)

    def _flash_scoop_light(self, **kwargs):
        ticks_remaining = kwargs.get("ticks_remaining")
        ticks
        fade = 0 if kwargs.get("change") < 0 else None

        if intvalue > 511:
            intvalue = 511

        binary = '{0:09b}'.format(intvalue)

        for x in range(9):
            if binary[8-x] == '1':
                self._get_bonus_light_by_number(x).on(fade_ms=fade)
            else:
                self._get_bonus_light_by_number(x).off(fade_ms=fade)

    @staticmethod
    def _get_bonus_light_by_number(num: int):
        for light in BonusLightController.lights:
            if light.tags.__contains__('bonus{}'.format(num)):
                return light



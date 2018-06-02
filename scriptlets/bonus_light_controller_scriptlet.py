from mpf.core.scriptlet import Scriptlet


class BonusLightController(Scriptlet):
    def on_load(self):
        self.debug_log("Bonus Light Controller scriptlet loaded!")

        self.machine.events.add_handler('player_bonuscount', self._handle_bonus_change)

    def _handle_bonus_change(self, **kwargs):
        binary = '{0:09b}'.format(kwargs.get("value"))
        for x in range(9):
            event_name = 'bonus_light_{light}_{lit}'.format(light=str(x), lit='on' if binary[8-x] == '1' else 'off')
            self.machine.events.post(event_name)

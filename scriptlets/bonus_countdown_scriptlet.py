from mpf.core.scriptlet import Scriptlet
from mpf.core.delays import DelayManager

delay_time = None  # type: int


class BonusCountdown(Scriptlet):
    def on_load(self):
        self.debug_log("Bonus Countdown scriptlet loaded!")
        self.machine.events.add_handler('bonus_product', self._start_bonus_countdown)
        self.machine.events.add_handler('player_bonuscount', self._decrement_bonus, 1)

    def _start_bonus_countdown(self, **kwargs):
        del kwargs
        if self.machine.game.player.bonuscount > 0:
            BonusCountdown.delay = 1800/self.machine.game.player.bonuscount
            if BonusCountdown.delay > 100:
                BonusCountdown.delay = 100
            self.machine.game.player.bonuscount -= 1
            self.machine.game.player.bonuscountdisplay += 1

    def _decrement_bonus(self, **kwargs):
        intchange = kwargs.get("change")
        if intchange < 0:
            DelayManager(self.machine.delayRegistry).add(callback=self._do_decrement, ms=BonusCountdown.delay)

    def _do_decrement(self):
        if self.machine.game.player.bonuscount > 0:
            self.machine.game.player.bonuscount -= 1
            self.machine.game.player.bonuscountdisplay += 1
        else:
            self.machine.events.post('bonus_subtotal_display',
                                     score=self.machine.game.player.bonuscountdisplay * self.machine.game.player.pds)
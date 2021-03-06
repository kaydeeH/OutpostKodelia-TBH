from mpf.core.scriptlet import Scriptlet
from mpf.core.delays import DelayManager

delay = None  # type: int


class BonusCountdown(Scriptlet):
    def on_load(self):
        self.debug_log("Bonus Countdown scriptlet loaded!")
        self.machine.events.add_handler('bonus_product', self._start_bonus_countdown)
        self.machine.events.add_handler('bonus_countdown_decrement', self._decrement_bonus, 1)
        self.machine.events.add_handler('bonus_countdown_speed_up', self._speed_up_bonus)

    def _start_bonus_countdown(self, **kwargs):
        del kwargs
        if self.machine.game.player.bonuscount > 0:
            BonusCountdown.delay = 1800/self.machine.game.player.bonuscount
            if BonusCountdown.delay > 100:
                BonusCountdown.delay = 100
            self.machine.game.player.bonuscount -= 1
            self.machine.game.player.bonuscountdisplay += 1
            self.machine.events.post('bonus_countdown_decrement')

    def _decrement_bonus(self, **kwargs):
            self.machine.delay.add(callback=self._do_decrement, ms=BonusCountdown.delay)
            if BonusCountdown.delay > 10:
                self.machine.delay.add(callback=self._do_decrement_audio, ms=BonusCountdown.delay)

    def _do_decrement_audio(self, **kwargs):
        self.machine.events.post('bonus_countdown_decrement_audio')

    def _speed_up_bonus(self, **kwargs):
        BonusCountdown.delay = 10

    def _do_decrement(self):
        if self.machine.game.player.bonuscount > 0:
            self.machine.game.player.bonuscount -= 1
            self.machine.game.player.bonuscountdisplay += 1
            self.machine.events.post('bonus_countdown_decrement')
        else:
            self.machine.events.post('bonus_subtotal_display',
                                     score=self.machine.game.player.bonuscountdisplay * self.machine.game.player.pds)

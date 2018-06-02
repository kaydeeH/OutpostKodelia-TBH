from mpf.core.scriptlet import Scriptlet
import time

class BonusCountdown(Scriptlet):
    def on_load(self):
        self.debug_log("Bonus Countdown scriptlet loaded!")
        self.machine.events.add_handler('bonus_product', self._handle_bonus_countdown)
        self.machine.events.add_handler('internal_bonus_shift', self._handle_bonus_shift)

    def _handle_bonus_countdown(self, **kwargs):
        del kwargs
        self.machine.events.post('internal_bonus_shift')

    def _handle_bonus_shift(self, **kwargs):
        del kwargs
        if self.machine.game.player.bonuscount > 0:
            self.machine.game.player.bonuscount = self.machine.game.player.bonuscount - 1
            self.machine.game.player.bonuscountdisplay = self.machine.game.player.bonuscountdisplay + 1
            time.sleep(0.025)
            self.machine.events.post('internal_bonus_shift')
        else:
            self.machine.events.post('bonus_subtotal_display', score=self.machine.game.player.bonuscountdisplay * self.machine.game.player.pds)

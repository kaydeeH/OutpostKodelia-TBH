from mpf.core.scriptlet import Scriptlet

class BonusMultiNotify(Scriptlet):
    def on_load(self):
        self.debug_log("Bonus Multi Notify Loaded")
        self.machine.events.add_handler('player_bonus_multiplier', self._bonus_multi_notify)

    def _bonus_multi_notify(self, **kwargs):
        if self.machine.game.player.bonus_multiplier > 1:
            self.machine.events.post('invoke_notify_by_event', new_text="BONUS\nMULTIPLIER", new_value=str(self.machine.game.player.bonus_multiplier) + "X")

            # self.machine.game.player.bonus_box_new_value = str(self.machine.game.player.bonus_multiplier) + "X"
            # self.machine.game.player.bonus_box_new_text = "BONUS\nMULTIPLIER"
            # self.machine.game.player.bonus_box_counter += 1
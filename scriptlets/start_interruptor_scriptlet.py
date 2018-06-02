from mpf.core.scriptlet import Scriptlet


class StartInterruptor(Scriptlet):
    def on_load(self):
        self.debug_log("Start interruptor scriptlet loaded!")

        self.machine.events.add_handler('player_add_request', self._check_score, 1000)

    def _check_score(self, **kwargs):
        del kwargs
        if self.machine.game.player and self.machine.game.player.score > 0:
            self.debug_log("Scores have been registered. Player add will be ignored.")
            self.machine.events.post('player_add_rejected_scores_exist')
            return False
        elif self.machine.game.player:
            self.debug_log("No scores have been registered. Player add will be allowed.")
            self.machine.events.post('player_add_allowed_no_scores')

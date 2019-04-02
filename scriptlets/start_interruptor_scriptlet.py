from mpf.core.scriptlet import Scriptlet


class StartInterruptor(Scriptlet):
    def on_load(self):
        self.debug_log("Start interruptor scriptlet loaded!")

        self.machine.events.add_handler('player_add_request', self._check_score, 1000)

    def _check_score(self, **kwargs):
        del kwargs
        if self.machine.game.player_list:
            for player in self.machine.game.player_list:
                if player.score > 0:
                    self.debug_log("Scores have been registered. Player add will be ignored.")
                    self.machine.events.post('start_interruptor_player_add_rejected')
                    return False

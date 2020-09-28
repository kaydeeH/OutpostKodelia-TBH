from mpf.core.scriptlet import Scriptlet


class LastGameScores(Scriptlet):

    def on_load(self):
        self.debug_log("Flip delay scriptlet loaded!")

        self.machine.events.add_handler('slide_lastgame_created', self._generate_events, 10000)

    def _generate_events(self, **kwargs):
        del kwargs

        player2 = self.machine.variables.get_machine_var("player2_score")
        player3 = self.machine.variables.get_machine_var("player3_score")
        player4 = self.machine.variables.get_machine_var("player4_score")

        if player2:
            self.machine.events.post('lastgame_player2', score=player2)

        if player3:
            self.machine.events.post('lastgame_player3', score=player3)

        if player4:
            self.machine.events.post('lastgame_player4', score=player4)

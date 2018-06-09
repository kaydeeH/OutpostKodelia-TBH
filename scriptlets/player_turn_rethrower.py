from mpf.core.scriptlet import Scriptlet


class PlayerTurnRethrower(Scriptlet):

    def on_load(self):
        self.debug_log("Player Turn Rethrower scriptlet loaded!")
        self.machine.events.add_handler('player_turn_started', self._player_turn, 10000)

    def _player_turn(self, **kwargs):
        int_player_turn = kwargs.get("number")              # type: int
        int_player_count = self.machine.game.num_players    # type: int

        self.machine.events.post("player_turn_started_out_of", number=int_player_turn, total=int_player_count)

from mpf.core.scriptlet import Scriptlet


class PlayerTurnRethrower(Scriptlet):

    def on_load(self):
        self.debug_log("Player Turn Rethrower scriptlet loaded!")
        self.machine.events.add_handler('player_turn_will_start', self._player_turn_start, 10000)
#        self.machine.events.add_handler('bonus_slide_is_displayed', self._player_turn, 10000)
        self.machine.events.add_handler('ball_will_end', self._player_turn, 10000)

    def _player_turn(self, **kwargs):
        #int_player_turn = kwargs.get("number")               # type: int
        int_player_count = self.machine.game.num_players     # type: int
        int_current_player = self.machine.game.player.number # type: int

        if int_current_player == int_player_count:
            int_player_turn = 1
        else:
            int_player_turn = int_current_player + 1

        self.machine.events.post("player_turn_started_out_of", number=int_player_turn, total=int_player_count)

    def _player_turn_start(self, **kwargs):
        int_player_count = self.machine.game.num_players  # type: int

        if int_player_count > 1:
            self.machine.events.post("multiplayer_game_player_start")

# machine.game.player.number
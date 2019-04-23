from mpf.core.scriptlet import Scriptlet

class EndGameEvents(Scriptlet):

    def on_load(self):
        self.debug_log("End Game Events")
        self.machine.events.add_handler('pre_final_score_p1', self._p1score)
        self.machine.events.add_handler('pre_final_score_p2', self._p2score)
        self.machine.events.add_handler('pre_final_score_p3', self._p3score)
        self.machine.events.add_handler('pre_final_score_p4', self._p4score)
        self.machine.events.add_handler('pre_a_winner_is_you', self._winners)

    def _p1score(self, **kwargs):
        if not(self.machine.game is None):
            if len(self.machine.game.player_list) > 0:
                self.machine.events.post('final_score_p1')

    def _p2score(self, **kwargs):
        if not(self.machine.game is None):
            if len(self.machine.game.player_list) > 1:
                self.machine.events.post('final_score_p2')

    def _p3score(self, **kwargs):
        if not(self.machine.game is None):
            if len(self.machine.game.player_list) > 2:
                self.machine.events.post('final_score_p3')

    def _p4score(self, **kwargs):
        if not(self.machine.game is None):
            if len(self.machine.game.player_list) > 3:
                self.machine.events.post('final_score_p4')

    def _winners(self, **kwargs):
        p1 = 0
        p2 = 0
        p3 = 0
        p4 = 0
        p1r = 0
        p2r = 0
        p3r = 0
        p4r = 0

        if not(self.machine.game is None):
            for py in range(len(self.machine.game.player_list)):
                if py == 0:
                    p1 = self.machine.game.player_list[py].score
                    p1r = 1
                if py == 1:
                    p2 = self.machine.game.player_list[py].score
                    p2r = 1
                    if p2 > p1:
                        p1r += 1
                    else:
                        p2r += 1
                if py == 2:
                    p3 = self.machine.game.player_list[py].score
                    p3r = 1
                    if p3 > p2:
                        p2r += 1
                    else:
                        p3r += 1
                    if p3 > p1:
                        p1r += 1
                    else:
                        p3r += 1
                if py == 3:
                    p4 = self.machine.game.player_list[py].score
                    p4r = 1
                    if p4 > p3:
                       p3r += 1
                    else:
                        p4r += 1
                    if p4 > p2:
                        p2r += 1
                    else:
                        p4r += 1
                    if p4 > p1:
                        p1r += 1
                    else:
                        p4r += 1

        self.machine.events.post('debug_a_winner_is_you', p1=p1, p2=p2, p3=p3, p4=p4, p1r=p1r, p2r=p2r, p3r=p3r, p4r=p4r)

        if p2 > 0:
           self.machine.events.post('final_position_p1', pos=p1r)
           self.machine.events.post('final_position_p2', pos=p2r)
        if p3 > 0:
           self.machine.events.post('final_position_p3', pos=p3r)
        if p4 > 0:
           self.machine.events.post('final_position_p4', pos=p4r)



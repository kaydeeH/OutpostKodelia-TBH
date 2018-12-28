from mpf.core.scriptlet import Scriptlet


class SelectedCheck(Scriptlet):
    def on_load(self):
        self.debug_log("Selected Check scriptlet loaded!")
        self.machine.events.add_handler('check_selected_mode_is_available', self._check_mode)
        self.machine.events.add_handler('mode_selector2_started', self._check_wiz)


    def _check_mode(self, **kwargs):
        del kwargs
        modes = {
            1: "status_untitled_mode_1",
            2: "status_untitled_mode_2",
            3: "status_untitled_mode_3",
            4: "status_untitled_mode_4",
            5: "status_untitled_mode_5",
            6: "status_untitled_mode_6",
            7: "status_untitled_mode_7"
        }
        startedmodes = {
            1: "status_mode_01_started",
            2: "status_mode_02_started",
            3: "status_mode_03_started",
            4: "status_mode_04_started",
            5: "status_mode_05_started",
            6: "status_mode_06_started",
            7: "status_mode_07_started"
        }
        player = self.machine.game.player
        if (player.vars.get(modes.get(player.vars.get("mode_pick"))) == 0) and player.vars.get("mode_pick") != 7:
            self.machine.events.post('selected_mode_is_available')
        if player.vars.get("mode_pick") == 7 and player.vars.get(modes.get(1)) + player.vars.get(modes.get(2)) + player.vars.get(modes.get(3)) + player.vars.get(modes.get(4)) + player.vars.get(modes.get(5)) + player.vars.get(modes.get(6)) > 2:
            self.machine.events.post('selected_mode_is_available')
            self.machine.events.post('wizard_mode_is_available')

    def _check_wiz(self, **kwargs):
        del kwargs
        modes = {
            1: "status_untitled_mode_1",
            2: "status_untitled_mode_2",
            3: "status_untitled_mode_3",
            4: "status_untitled_mode_4",
            5: "status_untitled_mode_5",
            6: "status_untitled_mode_6",
            7: "status_untitled_mode_7"
        }
        startedmodes = {
            1: "status_mode_01_started",
            2: "status_mode_02_started",
            3: "status_mode_03_started",
            4: "status_mode_04_started",
            5: "status_mode_05_started",
            6: "status_mode_06_started",
            7: "status_mode_07_started"
        }
        player = self.machine.game.player

#        if player.vars.get(modes.get(1)) != 0 and player.vars.get(modes.get(2)) != 0 and player.vars.get(modes.get(3)) != 0 and player.vars.get(modes.get(4)) != 0 and player.vars.get(modes.get(5)) != 0 and player.vars.get(modes.get(6)) != 0:
#        if player.vars.get(startedmodes.get(1)) != 0 and player.vars.get(startedmodes.get(2)) != 0 and player.vars.get(startedmodes.get(3)) != 0 and player.vars.get(startedmodes.get(4)) != 0 and player.vars.get(startedmodes.get(5)) != 0 and player.vars.get(startedmodes.get(6)) != 0:

        # if player.vars.get(startedmodes.get(1)) + player.vars.get(startedmodes.get(2)) + player.vars.get(startedmodes.get(3)) + player.vars.get(startedmodes.get(4)) + player.vars.get(startedmodes.get(5)) + player.vars.get(startedmodes.get(6)) > 2:
        #     self.machine.events.post('selector2_mode7_selected')
        # else:
        #     for ourMode in modes:
        #         if player.vars.get(modes.get(ourMode)) != 0:
        #             self.machine.events.post("{}_completed".format(modes.get(ourMode)))

        for ourMode in modes:
             if player.vars.get(modes.get(ourMode)) != 0 and ourMode != "status_untitled_mode_7":
                 self.machine.events.post("{}_completed".format(modes.get(ourMode)))

        if player.vars.get(modes.get(1)) + player.vars.get(modes.get(2)) + player.vars.get(modes.get(3)) + player.vars.get(modes.get(4)) + player.vars.get(modes.get(5)) + player.vars.get(modes.get(6)) < 3:
            self.machine.events.post('wizard_mode_not_available')
            self.machine.events.post('oh-test-no-wiz')


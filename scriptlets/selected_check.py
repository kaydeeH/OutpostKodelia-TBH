from mpf.core.scriptlet import Scriptlet

# set of items in {} is a dictionary
# set of items in [] is a list

class SelectedCheck(Scriptlet):
    def on_load(self):
        self.debug_log("Selected Check scriptlet loaded!")
        self.machine.events.add_handler('check_selected_mode_is_available', self._check_mode)
        self.machine.events.add_handler('mode_selector2_started', self._check_wiz)


    def _check_mode(self, **kwargs):
        del kwargs

        mode_statuses_d = {
            1: self.machine.achievements.untitled_mode_1.state,
            2: self.machine.achievements.untitled_mode_2.state,
            3: self.machine.achievements.untitled_mode_3.state,
            4: self.machine.achievements.untitled_mode_4.state,
            5: self.machine.achievements.untitled_mode_5.state,
            6: self.machine.achievements.untitled_mode_6.state,
            7: self.machine.achievements.untitled_mode_7.state
        }

        mode_complete_count = 0

        for modeStat in mode_statuses_d:
            if mode_statuses_d[modeStat] == "completed":
                mode_complete_count += 1

        player = self.machine.game.player
        if (mode_statuses_d.get(player.vars.get("mode_pick")) != "completed") and player.vars.get("mode_pick") != 7:
            self.machine.events.post('selected_mode_is_available')
        if player.vars.get("mode_pick") == 7 and mode_complete_count > 2:
            self.machine.events.post('selected_mode_is_available')
            self.machine.events.post('wizard_mode_is_available')

    def _check_wiz(self, **kwargs):
        del kwargs

        mode_statuses = [
            self.machine.achievements.untitled_mode_1.state,
            self.machine.achievements.untitled_mode_2.state,
            self.machine.achievements.untitled_mode_3.state,
            self.machine.achievements.untitled_mode_4.state,
            self.machine.achievements.untitled_mode_5.state,
            self.machine.achievements.untitled_mode_6.state,
            self.machine.achievements.untitled_mode_7.state
        ]

        mode_complete_count = 0

        for num, modeStat in enumerate(mode_statuses, 1):
            if modeStat == "completed":
               mode_complete_count += 1
               self.machine.events.post("status_untitled_mode_{}_completed".format(num))

        if mode_complete_count < 3:
            self.machine.events.post('wizard_mode_not_available')

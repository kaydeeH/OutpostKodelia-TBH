# EVENT to set values for infoboard_line_1_text, infoboard_line_2_text, infoboard_line_3_text
# set_infoboard_line_text -   linenbr
#                             text
#                             pts
#                             secs
#                             cycle (instant, scroll, star)
#                             delayms

from mpf.core.scriptlet import Scriptlet
from mpf.core.delays import DelayManager

in_line_number = None    # int
in_text = None           # string
in_pts = 0               # int
in_secs = None           # float
in_cycle = None          # string
in_delayms = None        # int

class infobox(Scriptlet):
    def on_load(self):
        self.debug_log("infobox started!")
        self.machine.events.add_handler('set_infoboard_line_text', self._set_info_text)
        self.machine.events.add_handler('update_info_box_line', self._set_text_line)

    def _set_info_text(self, **kwargs):
        infobox.in_line_number = kwargs.get("linenbr")
        infobox.in_text = kwargs.get("text")

        if infobox.in_text[0:1] == "(" and infobox.in_text[len(infobox.in_text) - 1:len(infobox.in_text)] == ")":
           infobox.in_text = self.machine.game.player.vars.get(infobox.in_text[1:len(infobox.in_text)-1])

        if kwargs.get("pts") != "none":
           infobox.in_pts = self.machine.game.player.vars.get(kwargs.get("pts"))
        else:
           infobox.in_pts = -1

        if kwargs.get("secs") != "none":
           infobox.in_secs = self.machine.game.player.vars.get(kwargs.get("secs"))
        else:
           infobox.in_secs = -1.0

        infobox.in_cycle = kwargs.get("cycle")
        infobox.in_delayms = kwargs.get("delayms")

        newtext = infobox.in_text

        try:
            if infobox.in_pts >= 0:
                newtext = newtext + (" " * (36 - len(newtext) - len('{:,}'.format(infobox.in_pts)))) + '{:,}'.format(
                    infobox.in_pts)
        except:
            newtext = newtext

        try:
            if infobox.in_secs >= 0:
                newtext = newtext + (" " * (36 - len(newtext) - len('{:.2f}'.format(infobox.in_secs)))) + '{:.2f}'.format(
                    infobox.in_secs)
        except:
            newtext = newtext


        if infobox.in_cycle == "instant":
            if infobox.in_line_number == 1:
               self.machine.game.player.infoboard_line_1_text = newtext
            if infobox.in_line_number == 2:
               self.machine.game.player.infoboard_line_2_text = newtext
            if infobox.in_line_number == 3:
               self.machine.game.player.infoboard_line_3_text = newtext

        if infobox.in_cycle == "scroll":
            if infobox.in_line_number == 1:
                oldtext = self.machine.game.player.infoboard_line_1_text
            if infobox.in_line_number == 2:
                oldtext = self.machine.game.player.infoboard_line_2_text
            if infobox.in_line_number == 3:
                oldtext = self.machine.game.player.infoboard_line_3_text

            try:
               oldtext = oldtext + (" " * (36 - len(oldtext)))
            except:
               oldtext = "                              "

            newtext = newtext + (" " * (36 - len(newtext)))
            eventtext = ""

            for x in range(0, 37):
                eventtext = oldtext[x:36] + newtext[0:x]
                DelayManager(self.machine.delayRegistry).add(callback=self._set_text_line,
                                                             ms=infobox.in_delayms * (x + 1),
                                                             eventname="update_info_box_line",
                                                             line=infobox.in_line_number,
                                                             newtext=eventtext)

        if infobox.in_cycle == "star":
            if infobox.in_line_number == 1:
                oldtext = self.machine.game.player.infoboard_line_1_text
            if infobox.in_line_number == 2:
                oldtext = self.machine.game.player.infoboard_line_2_text
            if infobox.in_line_number == 3:
                oldtext = self.machine.game.player.infoboard_line_3_text

            try:
               oldtext = oldtext + (" " * (36 - len(oldtext)))
            except:
               oldtext = "                              "

            newtext = newtext + (" " * (36 - len(newtext)))
            eventtext = ""
            for x in range(0, 36):
                eventtext = newtext[0:x] + "*" + oldtext[x+1:36]
                DelayManager(self.machine.delayRegistry).add(callback=self._set_text_line,
                                                             ms=infobox.in_delayms * (1 + (x * 2)),
                                                             eventname="update_info_box_line",
                                                             line=infobox.in_line_number,
                                                             newtext=eventtext)
                eventtext = newtext[0:x+1] + oldtext[x+1:36]
                DelayManager(self.machine.delayRegistry).add(callback=self._set_text_line,
                                                             ms=infobox.in_delayms * (2 + (x * 2)),
                                                             eventname="update_info_box_line",
                                                             line=infobox.in_line_number,
                                                             newtext=eventtext)


    def _set_text_line(self, **kwargs):
        if kwargs.get("line") == 1:
           self.machine.game.player.infoboard_line_1_text = kwargs.get("newtext")
        if kwargs.get("line") == 2:
           self.machine.game.player.infoboard_line_2_text = kwargs.get("newtext")
        if kwargs.get("line") == 3:
           self.machine.game.player.infoboard_line_3_text = kwargs.get("newtext")

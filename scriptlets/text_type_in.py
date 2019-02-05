#  Set an event of start_text_to_cycle
#
#     set_text_to_cycle:
#        text: "THIS IS THE TEXT I WANT TO DISPLAY"  -- your text
#        delay: 150                                  -- delay between transitions
#        varname: "typed_display_text"               -- variable you'll use for display
#        intermed: "*"                               -- your intermediate character

from mpf.core.scriptlet import Scriptlet
from mpf.core.delays import DelayManager

textValue = None         # string
textDisplay = None       # string
delayMs = None              # int
varName = None           # string
intermediate = None      # string

class TextTypeIn(Scriptlet):
    def on_load(self):
        self.debug_log("text typer started!")
        self.machine.events.add_handler('set_text_to_cycle', self._set_text)
        self.machine.events.add_handler('slide_video_created', self._clear_mach)
        self.machine.events.add_handler('slide_video_removed', self._clear_mach)

    def _clear_mach(self, **kwargs):
        self.machine.set_machine_var(name="thePinExp", value="")
        self.machine.set_machine_var(name="s1", value="")
        self.machine.set_machine_var(name="s2", value="")
        self.machine.set_machine_var(name="s3", value="")
        self.machine.set_machine_var(name="s4", value="")
        self.machine.set_machine_var(name="s5", value="")
        self.machine.set_machine_var(name="s6", value="")

    def _set_text(self, **kwargs):
        TextTypeIn.textValue = kwargs.get("text")

        if TextTypeIn.textValue == "s6":
            #TextTypeIn.textValue = str(self.machine.get_machine_var("score6_label")) + "-" + str(self.machine.get_machine_var("score6_name")) + " " + str(self.machine.get_machine_var("score6_value"))
            TextTypeIn.textValue = str(self.machine.get_machine_var("score6_label")) + "-" + str(self.machine.get_machine_var("score6_name")) + " " + "{:,}".format(self.machine.get_machine_var("score6_value"))

        if TextTypeIn.textValue == "s5":
            TextTypeIn.textValue = str(self.machine.get_machine_var("score5_label")) + "-" + str(self.machine.get_machine_var("score5_name")) + " " + "{:,}".format(self.machine.get_machine_var("score5_value"))

        if TextTypeIn.textValue == "s4":
            TextTypeIn.textValue = str(self.machine.get_machine_var("score4_label")) + "-" + str(self.machine.get_machine_var("score4_name")) + " " + "{:,}".format(self.machine.get_machine_var("score4_value"))

        if TextTypeIn.textValue == "s3":
            TextTypeIn.textValue = str(self.machine.get_machine_var("score3_label")) + "-" + str(self.machine.get_machine_var("score3_name")) + " " + "{:,}".format(self.machine.get_machine_var("score3_value"))

        if TextTypeIn.textValue == "s2":
            TextTypeIn.textValue = str(self.machine.get_machine_var("score2_label")) + "-" + str(self.machine.get_machine_var("score2_name")) + " " + "{:,}".format(self.machine.get_machine_var("score2_value"))

        if TextTypeIn.textValue == "s1":
            TextTypeIn.textValue = str(self.machine.get_machine_var("score1_label")) + "-" + str(self.machine.get_machine_var("score1_name")) + " " + "{:,}".format(self.machine.get_machine_var("score1_value"))

        TextTypeIn.delayMs = kwargs.get("delay")
        TextTypeIn.varName = kwargs.get("varname")
        TextTypeIn.intermediate = kwargs.get("intermed")
        TextTypeIn.textDisplay = TextTypeIn.intermediate
        #self.machine.machine_vars[TextTypeIn.varName] = TextTypeIn.textDisplay
        self.machine.set_machine_var(name=TextTypeIn.varName, value=TextTypeIn.textDisplay)
        DelayManager(self.machine.delayRegistry).add(callback=self._text_timer, ms=TextTypeIn.delayMs)

    def _text_timer(self, **kwargs):
        del kwargs

#        self.machine.events.post('debug_timer', val=TextTypeIn.textValue, tex=TextTypeIn.textDisplay)

        if TextTypeIn.textValue != TextTypeIn.textDisplay:
           strlen = len(TextTypeIn.textDisplay)
           if strlen == 0:
               TextTypeIn.textDisplay = TextTypeIn.intermediate
           elif TextTypeIn.textDisplay[strlen - 1] == TextTypeIn.intermediate:
               if strlen == 1:
                   TextTypeIn.textDisplay = TextTypeIn.textValue[0]
               else:
                   TextTypeIn.textDisplay = TextTypeIn.textDisplay[0:strlen - 1] + TextTypeIn.textValue[strlen - 1]
           else:
               TextTypeIn.textDisplay += TextTypeIn.intermediate

           # self.machine.game.player.typed_display_text = TextTypeIn.textDisplay
#          # self.machine.machine_vars[TextTypeIn.varName] = TextTypeIn.textDisplay
           self.machine.set_machine_var(name=TextTypeIn.varName, value=TextTypeIn.textDisplay)
           DelayManager(self.machine.delayRegistry).add(callback=self._text_timer, ms=TextTypeIn.delayMs)


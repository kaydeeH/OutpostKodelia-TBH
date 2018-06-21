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

    def _set_text(self, **kwargs):
        TextTypeIn.textValue = kwargs.get("text")
        TextTypeIn.delayMs = kwargs.get("delay")
        TextTypeIn.varName = kwargs.get("varname")
        TextTypeIn.intermediate = kwargs.get("intermed")
        TextTypeIn.textDisplay = TextTypeIn.intermediate
        self.machine.game.player[TextTypeIn.varName] = TextTypeIn.textDisplay
        DelayManager(self.machine.delayRegistry).add(callback=self._text_timer, ms=TextTypeIn.delayMs)

    def _text_timer(self, **kwargs):
        del kwargs

        self.machine.events.post('debug_timer', val=TextTypeIn.textValue, tex=TextTypeIn.textDisplay)

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
           self.machine.game.player[TextTypeIn.varName] = TextTypeIn.textDisplay
           DelayManager(self.machine.delayRegistry).add(callback=self._text_timer, ms=TextTypeIn.delayMs)


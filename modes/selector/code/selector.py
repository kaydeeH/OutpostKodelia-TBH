import copy
from mpf.modes.carousel.code.carousel import Carousel

OURMODES = [
  "untitled_mode_1",
  "untitled_mode_2",
  "untitled_mode_3",
  "untitled_mode_4",
  "untitled_mode_5",
  "untitled_mode_6",
  "untitled_mode_7"
]

class selector(Carousel):

  def mode_init(self):
    super().mode_init()
    self.debug_log("STARTING MODE SELECT")
    self.debug_log(" - items: {}".format(self._items))
    self._all_items = copy.copy(self._items)

  def mode_start(self, **kwargs):

    self._items = self._build_items_list()

    self.debug_log("Final list of selectmode options: {}".format(self._items.__str__()))
    super().mode_start(**kwargs)

    # Disable the intro slide after a time
    # self.delay.add(callback=self._remove_intro, ms=3000)

  def _build_items_list(self):
    player = self.machine.game.player

    items = ["intro"]

    for ourMode in OURMODES:
      status = player.vars.get("status_{}".format(ourMode))
      if (status == 0):
        items.append(ourMode)
        thelastmode = ourMode
      else:
        self.machine.events.post("{}_omitted".format(ourMode), selector=ourMode, stat=status)

    items.remove("intro")

    return items

  def _get_available_items(self):
    return self._items

  def _select_item(self, **kwargs):
    super()._select_item()
    selection = self._get_highlighted_item()
    if selection in OURMODES:
      self.machine.events.post("{}_mode_selected".format(self.name), selector=selection)

  def _update_highlighted_item(self, direction):
    h = self._get_highlighted_item()
    self.machine.events.post("{}_{}_highlighted".format(self.name, h), direction=direction)
    if h in OURMODES:
      self.machine.events.post("{}_mode_highlighted".format(self.name), selector=h)
    if (len(self._get_available_items()) == 1):
      self._select_item()

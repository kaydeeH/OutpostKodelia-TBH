from mpf.core.scriptlet import Scriptlet
from mpf.core.delays import DelayManager

green_id = None     # type: int
green_count = None  # type: int
green_delay = None  # type: int
green_sleep = None  # type: int

blue_id = None      # type: int
blue_count = None   # type: int
blue_delay = None   # type: int
blue_sleep = None   # type: int


class LightTimers(Scriptlet):
    def on_load(self):
        self.debug_log("Light Timers scriptlet started!")
        self.machine.events.add_handler('load_one_player_elements', self._start_timers)

    def _start_timers(self, **kwargs):
        del kwargs

        LightTimers.green_id = 0
        LightTimers.green_count = 2
        LightTimers.green_delay = 265
        LightTimers.green_sleep = 5000

        LightTimers.blue_id = 0
        LightTimers.blue_count = 8
        LightTimers.blue_delay = 515
        LightTimers.blue_sleep = 6000

        DelayManager(self.machine.delayRegistry).add(callback=self._green_timer, ms=1000)
        DelayManager(self.machine.delayRegistry).add(callback=self._blue_timer, ms=1000)

    def _green_timer(self):
        self.machine.events.post('green_light_timer_' + str(LightTimers.green_id))

        if LightTimers.green_id < LightTimers.green_count - 1:
            LightTimers.green_id += 1
            DelayManager(self.machine.delayRegistry).add(callback=self._green_timer, ms=LightTimers.green_delay)
        else:
            LightTimers.green_id = 0
            DelayManager(self.machine.delayRegistry).add(callback=self._green_timer, ms=LightTimers.green_sleep)

    def _blue_timer(self):
        self.machine.events.post('blue_light_timer_' + str(LightTimers.blue_id))

        if LightTimers.blue_id < LightTimers.blue_count - 1:
            LightTimers.blue_id += 1
            DelayManager(self.machine.delayRegistry).add(callback=self._blue_timer, ms=LightTimers.blue_delay)
        else:
            LightTimers.blue_id = 0
            DelayManager(self.machine.delayRegistry).add(callback=self._blue_timer, ms=LightTimers.blue_sleep)


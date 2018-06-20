from mpf.core.scriptlet import Scriptlet
from datetime import datetime
from datetime import timedelta

left_time = None    # type: datetime
right_time = None   # type: datetime


class FlipDelay(Scriptlet):

    def on_load(self):
        self.debug_log("Flip delay scriptlet loaded!")
        FlipDelay.left_time = datetime.utcnow()
        FlipDelay.right_time = datetime.utcnow()
        self.machine.events.add_handler('s_flipper_left_active', self._left_delay, 10000)
        self.machine.events.add_handler('s_flipper_right_active', self._right_delay, 10000)

    def _left_delay(self, **kwargs):
        del kwargs

        if datetime.utcnow() >= FlipDelay.left_time + timedelta(milliseconds=300):
            FlipDelay.left_time = datetime.utcnow()
            self.machine.events.post('mode_select_left')

    def _right_delay(self, **kwargs):
        del kwargs

        if datetime.utcnow() >= FlipDelay.right_time + timedelta(milliseconds=300):
            FlipDelay.right_time = datetime.utcnow()
            self.machine.events.post('mode_select_right')

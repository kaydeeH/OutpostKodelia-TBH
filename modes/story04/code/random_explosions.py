from mpf.core.mode import Mode
import random


class RandomExplosions(Mode):
    def mode_start(self, **kwargs):
        self.debug_log("Random explosions mode scriptlet started!")
        self.add_mode_event_handler('start_explosions', self._play_explosion)

    def _play_explosion(self, **kwargs):
        del kwargs
        self.machine.events.post('play_explosion')
        delay = random.randint(5000, 8000)
        self.delay.add(delay, self._play_explosion)

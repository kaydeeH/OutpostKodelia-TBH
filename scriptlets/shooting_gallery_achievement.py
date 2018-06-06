from mpf.core.scriptlet import Scriptlet


class ShootingGalleryAchievement(Scriptlet):

    def on_load(self):
        self.debug_log("Shooting Gallery Achievement scriptlet loaded!")
        self.machine.events.add_handler('timer_gallery_timer_complete', self._evaluate_achievement, 10000)

    def _evaluate_achievement(self, **kwargs):
        del kwargs

        if self.machine.game.player.gallery_targets_hit > 2:
            self.machine.events.post('story_is_about_to_end')
        else:
            self.machine.events.post('story_is_about_to_fail')

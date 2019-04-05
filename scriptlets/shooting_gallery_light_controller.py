from mpf.core.scriptlet import Scriptlet
from mpf.devices.light import Light
from mpf.core.device_manager import DeviceCollection
import random

lights = None                    # type: DeviceCollection[str, Light]
previous_light_num = None        # type: int
curr_count = None                # type: int


class ShootingGalleryLightController(Scriptlet):

    def on_load(self):
        self.debug_log("Shooting Gallery Light Controller scriptlet loaded!")
        ShootingGalleryLightController.lights = self.machine.lights.items_tagged('gallery')
        ShootingGalleryLightController.previous_light_num = 0
        ShootingGalleryLightController.curr_count = 99
        self.machine.events.add_handler('timer_gallery_timer_display_tick', self._count_ticks, 10000)

    def _count_ticks(self, **kwargs):
        del kwargs

        ShootingGalleryLightController.curr_count += 1
        if ShootingGalleryLightController.curr_count == 100:
            ShootingGalleryLightController.curr_count = 0
            self._change_light()

    def _change_light(self):

        colornum = random.randint(1, 3)
        lightnum = random.randint(0, ShootingGalleryLightController.lights.__len__()-1)

        self.machine.events.post('gallery_light_' + str(ShootingGalleryLightController.previous_light_num) + '_off')

        for x in range(colornum):
            self.machine.events.post('gallery_light_' + str(lightnum) + '_change')

        ShootingGalleryLightController.previous_light_num = lightnum

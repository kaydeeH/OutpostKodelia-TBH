from mpf.core.scriptlet import Scriptlet
from mpf.devices.light import Light
from mpf.core.device_manager import DeviceCollectionType
import random

lights = None           # type: DeviceCollectionType[str, Light]


class ShootingGalleryLightController(Scriptlet):

    def on_load(self):
        self.debug_log("Bonus Light Controller scriptlet loaded!")
        ShootingGalleryLightController.lights = self.machine.lights.items_tagged('gallery')
        self.machine.events.add_handler('timer_gallery_timer_tick', self._change_light, 10000)

    def _change_light(self, **kwargs):
        del kwargs
        colors = ["red", "green", "blue"]
        colornum = random.randint(0, 2)
        # random.sample(colors, 1)

        lightnum = random.randint(0, ShootingGalleryLightController.lights.__len__()-1)

        self.machine.events.post('gallery_light_change', lightname=ShootingGalleryLightController.lights[lightnum].name, colorval=colors[colornum])

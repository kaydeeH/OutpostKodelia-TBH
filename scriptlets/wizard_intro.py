from mpf.core.scriptlet import Scriptlet
from mpf.core.delays import DelayManager

delay_time = None  # type: int

class wizardIntro(Scriptlet):
    def on_load(self):
        self.debug_log("Bonus Countdown scriptlet loaded!")
        self.machine.events.add_handler('slide_story_07_intro_slide_active', self._start_display)

    def _start_display(self, **kwargs):
        del kwargs
        player = self.machine.game.player

        modes = {
            1: "status_untitled_mode_1",
            2: "status_untitled_mode_2",
            3: "status_untitled_mode_3",
            4: "status_untitled_mode_4",
            5: "status_untitled_mode_5",
            6: "status_untitled_mode_6"
        }

        scene_count = 0
        crew_count = 0

        wizardIntro.delay_time = 500

        for ourMode in modes:
             if player.vars.get(modes.get(ourMode)) != 0:
                 scene_count += 1
                 DelayManager(self.machine.delayRegistry).add(callback=self._throw_event, ms=wizardIntro.delay_time, eventname="{}_completed".format(modes.get(ourMode)))

                 if scene_count <= 3:
                     DelayManager(self.machine.delayRegistry).add(callback=self._throw_event,
                                                                  ms=wizardIntro.delay_time,
                                                                  eventname="wizard_bonus_increment")
                 else:
                     DelayManager(self.machine.delayRegistry).add(callback=self._throw_event,
                                                                  ms=wizardIntro.delay_time,
                                                                  eventname="wizard_bonus_multiply")
                 wizardIntro.delay_time += 500

        wizardIntro.delay_time += 500

        alex_state = self.machine.achievements.char_alex.state
        bob_state = self.machine.achievements.char_bob.state
        charlie_state = self.machine.achievements.char_charlie.state
        dan_state = self.machine.achievements.char_dan.state
        hanz_state = self.machine.achievements.char_hans.state
        harry_state = self.machine.achievements.char_harry.state
        kate_state = self.machine.achievements.char_kate.state
        vincent_state = self.machine.achievements.char_vincent.state

        if alex_state == "completed":
            DelayManager(self.machine.delayRegistry).add(callback=self._throw_event,
                                                         ms=wizardIntro.delay_time,
                                                         eventname="char_alex_is_complete")
            wizardIntro.delay_time += 500

        if charlie_state == "completed":
            DelayManager(self.machine.delayRegistry).add(callback=self._throw_event,
                                                         ms=wizardIntro.delay_time,
                                                         eventname="char_charlie_is_complete")
            wizardIntro.delay_time += 500

        if dan_state == "completed":
            DelayManager(self.machine.delayRegistry).add(callback=self._throw_event,
                                                         ms=wizardIntro.delay_time,
                                                         eventname="char_dan_is_complete")
            wizardIntro.delay_time += 500

        if kate_state == "completed":
            DelayManager(self.machine.delayRegistry).add(callback=self._throw_event,
                                                         ms=wizardIntro.delay_time,
                                                         eventname="char_kate_is_complete")
            wizardIntro.delay_time += 500

        if harry_state == "completed":
            DelayManager(self.machine.delayRegistry).add(callback=self._throw_event,
                                                         ms=wizardIntro.delay_time,
                                                         eventname="char_harry_is_complete")
            wizardIntro.delay_time += 500

        if hanz_state == "completed":
            DelayManager(self.machine.delayRegistry).add(callback=self._throw_event,
                                                         ms=wizardIntro.delay_time,
                                                         eventname="char_hanz_is_complete")
            wizardIntro.delay_time += 500

        if vincent_state == "completed":
            DelayManager(self.machine.delayRegistry).add(callback=self._throw_event,
                                                         ms=wizardIntro.delay_time,
                                                         eventname="char_vincent_is_complete")
            wizardIntro.delay_time += 500

        if bob_state == "completed":
            DelayManager(self.machine.delayRegistry).add(callback=self._throw_event,
                                                         ms=wizardIntro.delay_time,
                                                         eventname="char_bob_is_complete")
            wizardIntro.delay_time += 500

    def _throw_event(self, **kwargs):
        event_name = kwargs.get("eventname")
        self.machine.events.post(event_name)
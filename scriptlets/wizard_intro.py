from mpf.core.scriptlet import Scriptlet
from mpf.core.delays import DelayManager

delay_time = None  # type: int

class wizardIntro(Scriptlet):
    def on_load(self):
        self.debug_log("Bonus Countdown scriptlet loaded!")
        self.machine.events.add_handler('slide_story_07_intro_slide_active', self._start_display)

    def _start_display(self, **kwargs):
        del kwargs

        mode_statuses = [
            self.machine.achievements.untitled_mode_1.state,
            self.machine.achievements.untitled_mode_2.state,
            self.machine.achievements.untitled_mode_3.state,
            self.machine.achievements.untitled_mode_4.state,
            self.machine.achievements.untitled_mode_5.state,
            self.machine.achievements.untitled_mode_6.state,
            self.machine.achievements.untitled_mode_7.state
        ]

        scene_count = 0

        wizardIntro.delay_time = 500

        for num, modeStat in enumerate(mode_statuses, 1):
            if modeStat == "completed":
                 scene_count += 1
                 self.machine.delay.add(callback=self._throw_event, ms=wizardIntro.delay_time, eventname="status_untitled_mode_{}_completed".format(num))

                 if scene_count <= 3:
                     self.machine.delay.add(callback=self._throw_event,
                                                                  ms=wizardIntro.delay_time,
                                                                  eventname="wizard_bonus_increment")
                 else:
                     self.machine.delay.add(callback=self._throw_event,
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
            self.machine.delay.add(callback=self._throw_event,
                                                         ms=wizardIntro.delay_time,
                                                         eventname="char_alex_is_complete")
            wizardIntro.delay_time += 500

        if charlie_state == "completed":
            self.machine.delay.add(callback=self._throw_event,
                                                         ms=wizardIntro.delay_time,
                                                         eventname="char_charlie_is_complete")
            wizardIntro.delay_time += 500

        if dan_state == "completed":
            self.machine.delay.add(callback=self._throw_event,
                                                         ms=wizardIntro.delay_time,
                                                         eventname="char_dan_is_complete")
            wizardIntro.delay_time += 500

        if kate_state == "completed":
            self.machine.delay.add(callback=self._throw_event,
                                                         ms=wizardIntro.delay_time,
                                                         eventname="char_kate_is_complete")
            wizardIntro.delay_time += 500

        if harry_state == "completed":
            self.machine.delay.add(callback=self._throw_event,
                                                         ms=wizardIntro.delay_time,
                                                         eventname="char_harry_is_complete")
            wizardIntro.delay_time += 500

        if hanz_state == "completed":
            self.machine.delay.add(callback=self._throw_event,
                                                         ms=wizardIntro.delay_time,
                                                         eventname="char_hanz_is_complete")
            wizardIntro.delay_time += 500

        if vincent_state == "completed":
            self.machine.delay.add(callback=self._throw_event,
                                                         ms=wizardIntro.delay_time,
                                                         eventname="char_vincent_is_complete")
            wizardIntro.delay_time += 500

        if bob_state == "completed":
            self.machine.delay.add(callback=self._throw_event,
                                                         ms=wizardIntro.delay_time,
                                                         eventname="char_bob_is_complete")
            wizardIntro.delay_time += 500

        wizardIntro.delay_time += 3000
        self.machine.delay.add(callback=self._throw_event,
                                                     ms=wizardIntro.delay_time,
                                                     eventname="wizard_intro_slide_ready_to_remove")

    def _throw_event(self, **kwargs):
        event_name = kwargs.get("eventname")
        self.machine.events.post(event_name)
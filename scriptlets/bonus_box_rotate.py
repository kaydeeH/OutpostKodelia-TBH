from mpf.core.scriptlet import Scriptlet

newTextList = None        # list
newTextValue = None      # list

class BonusBoxRotate(Scriptlet):
    def on_load(self):
        BonusBoxRotate.newTextList = list()
        BonusBoxRotate.newTextValue = list()

        self.debug_log("Ball Goal Calc!")
        self.machine.events.add_handler('player_bonus_box_counter', self._add_to_box_queue)
        self.machine.events.add_handler('invoke_notify_by_event', self._add_to_box_queue_parms)

#        self.machine.events.add_handler('player_bonus_box_counter', self._new_bonus_box)
        self.machine.events.add_handler('timer_bonus_box_queue_tick', self._new_bonus_box)
        self.machine.events.add_handler('timer_bonus_box_01_timer_complete', self._box01timeout)
        self.machine.events.add_handler('timer_bonus_box_02_timer_complete', self._box02timeout)
        self.machine.events.add_handler('timer_bonus_box_03_timer_complete', self._box03timeout)
        self.machine.events.add_handler('timer_bonus_box_04_timer_complete', self._box04timeout)

    def _add_to_box_queue(self, **kwargs):
        BonusBoxRotate.newTextList.append(self.machine.game.player.bonus_box_new_text)
        BonusBoxRotate.newTextValue.append(self.machine.game.player.bonus_box_new_value)

    def _add_to_box_queue_parms(self, **kwargs):
        newText = kwargs.get("new_text")
        newValue = kwargs.get("new_value")
        BonusBoxRotate.newTextList.append(newText)
        BonusBoxRotate.newTextValue.append(newValue)

    def _new_bonus_box(self, **kwargs):
        # we have a new bonus box to add, so lets use the first "empty" box, move everyone else on the board
        if BonusBoxRotate.newTextList:
          str_new_text = BonusBoxRotate.newTextList.pop(0)
          str_new_value = BonusBoxRotate.newTextValue.pop(0)
          int_use_box = 0
          if self.machine.game.player.bonus_box_01_position == 0:
              int_use_box = 1
              self.machine.game.player.bonus_box_01_text = str_new_text
              self.machine.game.player.bonus_box_01_value = str_new_value
          elif self.machine.game.player.bonus_box_02_position == 0:
              int_use_box = 2
              self.machine.game.player.bonus_box_02_text = str_new_text
              self.machine.game.player.bonus_box_02_value = str_new_value
          elif self.machine.game.player.bonus_box_03_position == 0:
              int_use_box = 3
              self.machine.game.player.bonus_box_03_text = str_new_text
              self.machine.game.player.bonus_box_03_value = str_new_value
          else:
              int_use_box = 4
              self.machine.game.player.bonus_box_04_text = str_new_text
              self.machine.game.player.bonus_box_04_value = str_new_value

          int_curr_total = self.machine.game.player.bonus_box_01_position + self.machine.game.player.bonus_box_02_position + self.machine.game.player.bonus_box_03_position + self.machine.game.player.bonus_box_04_position
          if int_curr_total == 0:
              self.machine.events.post('bonus_box_first')

          if int_use_box == 1 or self.machine.game.player.bonus_box_01_position > 0:
              self.machine.game.player.bonus_box_01_position += 1
              if self.machine.game.player.bonus_box_01_position > 3:
                  self.machine.events.post('bonus_box_remove_01_start')
                  self.machine.game.player.bonus_box_01_position = 0
              elif self.machine.game.player.bonus_box_01_position > 1:
                  self.machine.events.post('bonus_box_rotate', box=1)
              elif self.machine.game.player.bonus_box_01_position == 1:
                   self.machine.events.post('bonus_box_create', box=1)

          if int_use_box == 2 or self.machine.game.player.bonus_box_02_position > 0:
              self.machine.game.player.bonus_box_02_position += 1
              if self.machine.game.player.bonus_box_02_position > 3:
                  self.machine.events.post('bonus_box_remove_02_start')
                  self.machine.game.player.bonus_box_02_position = 0
              elif self.machine.game.player.bonus_box_02_position > 1:
                  self.machine.events.post('bonus_box_rotate', box=2)
              elif self.machine.game.player.bonus_box_02_position == 1:
                   self.machine.events.post('bonus_box_create', box=2)

          if int_use_box == 3 or self.machine.game.player.bonus_box_03_position > 0:
              self.machine.game.player.bonus_box_03_position += 1
              if self.machine.game.player.bonus_box_03_position > 3:
                  self.machine.events.post('bonus_box_remove_03_start')
                  self.machine.game.player.bonus_box_03_position = 0
              elif self.machine.game.player.bonus_box_03_position > 1:
                   self.machine.events.post('bonus_box_rotate', box=3)
              elif self.machine.game.player.bonus_box_03_position == 1:
                   self.machine.events.post('bonus_box_create', box=3)


          if int_use_box == 4 or self.machine.game.player.bonus_box_04_position > 0:
             self.machine.game.player.bonus_box_04_position += 1
             if self.machine.game.player.bonus_box_04_position > 3:
                self.machine.events.post('bonus_box_remove_04_start')
                self.machine.game.player.bonus_box_04_position = 0
             elif self.machine.game.player.bonus_box_04_position > 1:
                self.machine.events.post('bonus_box_rotate', box=4)
             elif self.machine.game.player.bonus_box_04_position == 1:
                self.machine.events.post('bonus_box_create', box=4)

        # self.machine.game.player.bonus_box_new_text = ""
        # self.machine.game.player.bonus_box_new_value = ""

    def _box01timeout(self, **kwargs):
        self.machine.game.player.bonus_box_01_position = 0
        int_curr_total = self.machine.game.player.bonus_box_01_position + self.machine.game.player.bonus_box_02_position + self.machine.game.player.bonus_box_03_position + self.machine.game.player.bonus_box_04_position
        self.machine.events.post('bonus_box_remove_01_start')
        if int_curr_total == 0:
            self.machine.events.post('bonus_box_first_remove')

    def _box02timeout(self, **kwargs):
        self.machine.game.player.bonus_box_02_position = 0
        int_curr_total = self.machine.game.player.bonus_box_01_position + self.machine.game.player.bonus_box_02_position + self.machine.game.player.bonus_box_03_position + self.machine.game.player.bonus_box_04_position
        self.machine.events.post('bonus_box_remove_02_start')
        if int_curr_total == 0:
            self.machine.events.post('bonus_box_first_remove')

    def _box03timeout(self, **kwargs):
        self.machine.game.player.bonus_box_03_position = 0
        int_curr_total = self.machine.game.player.bonus_box_01_position + self.machine.game.player.bonus_box_02_position + self.machine.game.player.bonus_box_03_position + self.machine.game.player.bonus_box_04_position
        self.machine.events.post('bonus_box_remove_03_start')
        if int_curr_total == 0:
            self.machine.events.post('bonus_box_first_remove')

    def _box04timeout(self, **kwargs):
        self.machine.game.player.bonus_box_04_position = 0
        int_curr_total = self.machine.game.player.bonus_box_01_position + self.machine.game.player.bonus_box_02_position + self.machine.game.player.bonus_box_03_position + self.machine.game.player.bonus_box_04_position
        self.machine.events.post('bonus_box_remove_04_start')
        if int_curr_total == 0:
            self.machine.events.post('bonus_box_first_remove')
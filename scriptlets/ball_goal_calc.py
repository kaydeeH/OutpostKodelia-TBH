from mpf.core.scriptlet import Scriptlet

class BallGoalCalc(Scriptlet):
    def on_load(self):
        self.debug_log("Ball Goal Calc!")
        self.machine.events.add_handler('player_gravassist', self._grav_assist_check)
        self.machine.events.add_handler('player_pops', self._grav_pops_check)
        self.machine.events.add_handler('player_lanes', self._grav_lanes_check)
        self.machine.events.add_handler('player_drops', self._grav_drops_check)
        self.machine.events.add_handler('player_spins', self._grav_spins_check)
        self.machine.events.add_handler('ball_goal_has_been_met', self._ball_goal_level_check)

    def _grav_assist_check(self, **kwargs):
        if self.machine.game.player.gravassist > 1 and self.machine.game.player.gravassistLevel > 0:
          if self.machine.game.player.gravassist >= self.machine.game.player.gravassistTarget:
              self.machine.game.player.pds += 100 * self.machine.game.player.gravassistLevel
              self.machine.game.player.gravassistLevel += 1
              self.machine.game.player.gravassistTarget += int(self.machine.game.player.gravassistTarget / (self.machine.game.player.gravassistLevel - 1))
              self._ball_goal_notify("GRAVITY\nASSIST", "LEVEL ", self.machine.game.player.gravassistLevel)
              self.machine.events.post('ball_goal_has_been_met')
              self.machine.events.post('ball_goal_gravity_assist_met', level=self.machine.game.player.gravassistLevel)

    def _grav_pops_check(self, **kwargs):
        if self.machine.game.player.pops > 1 and self.machine.game.player.popsLevel > 0:
          if self.machine.game.player.pops >= self.machine.game.player.popsTarget:
              self.machine.game.player.pds += 100 * self.machine.game.player.popsLevel
              self.machine.game.player.popsLevel += 1
              self.machine.game.player.popsTarget += int(self.machine.game.player.popsTarget / (self.machine.game.player.popsLevel - 1))
              self._ball_goal_notify("INERTIAL\nBOOST", "LEVEL ", self.machine.game.player.popsLevel)
              self.machine.events.post('ball_goal_has_been_met')
              self.machine.events.post('ball_goal_inertial_boost_met', level=self.machine.game.player.popsLevel)


    def _grav_lanes_check(self, **kwargs):
        if self.machine.game.player.lanes > 1 and self.machine.game.player.lanesLevel > 0:
          if self.machine.game.player.lanes >= self.machine.game.player.lanesTarget:
              self.machine.game.player.pds += 100 * self.machine.game.player.lanesLevel
              self.machine.game.player.lanesLevel += 1
              self.machine.game.player.lanesTarget += int(self.machine.game.player.lanesTarget / (self.machine.game.player.lanesLevel - 1))
              self._ball_goal_notify("COORDINATES\nLOCK", "LEVEL ", self.machine.game.player.lanesLevel)
              self.machine.events.post('ball_goal_has_been_met')
              self.machine.events.post('ball_goal_coordinate_locks_met', level=self.machine.game.player.lanesLevel)


    def _grav_drops_check(self, **kwargs):
        if self.machine.game.player.drops > 1 and self.machine.game.player.dropsLevel > 0:
          if self.machine.game.player.drops >= self.machine.game.player.dropsTarget:
              self.machine.game.player.pds += 100 * self.machine.game.player.dropsLevel
              self.machine.game.player.dropsLevel += 1
              self.machine.game.player.dropsTarget += int(self.machine.game.player.dropsTarget / (self.machine.game.player.dropsLevel - 1))
              self._ball_goal_notify("ROBOTS\nDESTROYED", "LEVEL ", self.machine.game.player.dropsLevel)
              self.machine.events.post('ball_goal_has_been_met')
              self.machine.events.post('ball_goal_robots_met', level=self.machine.game.player.dropsLevel)

    def _grav_spins_check(self, **kwargs):
        if self.machine.game.player.spins > 1 and self.machine.game.player.spinsLevel > 0:
          if self.machine.game.player.spins >= self.machine.game.player.spinsTarget:
              self.machine.game.player.pds += 100 * self.machine.game.player.spinsLevel
              self.machine.game.player.spinsLevel += 1
              self.machine.game.player.spinsTarget += int(self.machine.game.player.spinsTarget / (self.machine.game.player.spinsLevel - 1))
              self._ball_goal_notify("GYROSCOPE\nROTATION", "LEVEL ", self.machine.game.player.spinsLevel)
              self.machine.events.post('ball_goal_has_been_met')
              self.machine.events.post('ball_goal_spins_met', level=self.machine.game.player.spinsLevel)

    def _ball_goal_level_check(self, **kwargs):
            if self.machine.game.player.spinsLevel > 1:
              if self.machine.game.player.spinsLevel == self.machine.game.player.gravassistLevel and self.machine.game.player.spinsLevel == self.machine.game.player.popsLevel and self.machine.game.player.spinsLevel == self.machine.game.player.lanesLevel and self.machine.game.player.spinsLevel == self.machine.game.player.dropsLevel:
                  self.machine.game.player.pds += 1000
                  self.machine.events.post('ball_goal_level_up_sync_bonus', level=self.machine.game.player.spinsLevel)

            # self._ball_goal_notify("BONUS VALUE\nBOOST", "", self.machine.game.player.pds)

    def _ball_goal_notify(self, strText, strValue, intLevel):
        self.machine.events.post('invoke_notify_by_event', new_text=strText, new_value=strValue + str(intLevel))
        # self.machine.game.player.bonus_box_new_value = strValue + str(intLevel)
        # self.machine.game.player.bonus_box_new_text = strText
        # self.machine.game.player.bonus_box_counter += 1
"""
core/game_state.py

Stores information about what has happened during the current game.
"""


class GameState:
    def __init__(self):
        self.current_operation = 1
        self.current_mission = 1
        self.deaths = 0

        self.completed_missions = []

        self.visits = {
            "hall_of_embers": 0,
            "mission_planning": 0,
            "armory": 0,
            "med_bay": 0,
            "hangar_bay": 0,
        }

        self.flags = {
            "met_tiberius": False,
            "met_caz": False,
            "met_armorers": False,
            "heard_brexor_ship_story": False,

            "rescued_seaf": False,
            "recovered_beacon": False,
            "collapsed_hive": False,
            "held_the_line": False,
        }

    def record_visit(self, location):
        if location not in self.visits:
            self.visits[location] = 0

        self.visits[location] += 1

    def visit_count(self, location):
        return self.visits.get(location, 0)

    def set_flag(self, flag_name, value=True):
        self.flags[flag_name] = value

    def has_flag(self, flag_name):
        return self.flags.get(flag_name, False)

    def complete_mission(self, mission_number):
        if mission_number not in self.completed_missions:
            self.completed_missions.append(mission_number)

        self.current_mission = mission_number + 1

    def record_death(self):
        self.deaths += 1
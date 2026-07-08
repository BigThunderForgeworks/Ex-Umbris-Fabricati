"""
player.py

Stores and manages all information about the current player.

As the game grows this file will eventually contain:
- Callsign
- Class
- Rank
- XP
- Reputation
- Inventory
- Stratagems
- Medals
- Codex Progress
"""

from core.classes import choose_class


class Player:
    def __init__(self):
        self.callsign = ""
        self.player_class = None

        # Future Systems
        self.rank = "Recruit"
        self.xp = 0

        self.reputation = {
            "honor": 0,
            "courage": 0,
            "knowledge": 0,
            "sacrifice": 0
        }

        self.medals = []
        self.codex = []

        self.inventory = []
        self.stratagems = []

    # --------------------------------------------------------
    # Character Creation
    # --------------------------------------------------------

    def create_character(self):
        self.callsign = input("Enter your callsign: ").strip()

        if not self.callsign:
            self.callsign = "Unnamed Specter"

        print()

        self.player_class = choose_class()

    # --------------------------------------------------------
    # Convenience Getters
    # --------------------------------------------------------

    @property
    def class_name(self):
        if self.player_class:
            return self.player_class["title"]
        return "Unknown"

    @property
    def class_flavor(self):
        if self.player_class:
            return self.player_class["flavor"]
        return ""

    # --------------------------------------------------------
    # XP
    # --------------------------------------------------------

    def add_xp(self, amount):
        self.xp += amount

    # --------------------------------------------------------
    # Reputation
    # --------------------------------------------------------

    def add_reputation(self, category, amount):

        if category in self.reputation:
            self.reputation[category] += amount

    # --------------------------------------------------------
    # Medals
    # --------------------------------------------------------

    def award_medal(self, medal):

        if medal not in self.medals:
            self.medals.append(medal)

    # --------------------------------------------------------
    # Codex
    # --------------------------------------------------------

    def unlock_codex(self, entry):

        if entry not in self.codex:
            self.codex.append(entry)

    # --------------------------------------------------------
    # Inventory
    # --------------------------------------------------------

    def add_item(self, item):
        self.inventory.append(item)

    def add_stratagem(self, stratagem):

        if stratagem not in self.stratagems:
            self.stratagems.append(stratagem)
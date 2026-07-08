"""
utils.py

General helper functions for the EUF text game.

This file is intentionally small for now. As the project grows, place reusable
helpers here when they do not clearly belong to text.py, player.py, save.py,
or a specific story module.
"""

from core.text import say, blank


# ------------------------------------------------------------
# Choice Helpers
# ------------------------------------------------------------

def get_number_choice(prompt_text, minimum, maximum):
    """
    Ask the player for a number between minimum and maximum.
    Keeps asking until a valid choice is entered.
    """
    while True:
        choice = input(prompt_text).strip()

        if choice.isdigit():
            number = int(choice)
            if minimum <= number <= maximum:
                return number

        print(f"Invalid selection. Choose a number from {minimum} to {maximum}.")


# ------------------------------------------------------------
# Simple Menu Display
# ------------------------------------------------------------

def show_menu(title, options):
    """
    Prints a numbered menu and returns the selected number.

    Example:
        choice = show_menu("Choose your objective:", [
            "Assault the hive.",
            "Search the outpost.",
            "Scout the ridge."
        ])
    """
    blank()
    print(title)

    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    blank()
    return get_number_choice("Choose your action: ", 1, len(options))


# ------------------------------------------------------------
# Ending / Status Helpers
# ------------------------------------------------------------

def mission_complete():
    blank()
    say("MISSION COMPLETE", 2)


def mission_failed():
    blank()
    say("MISSION FAILED", 2)


# ------------------------------------------------------------
# Debug Helpers
# ------------------------------------------------------------

def debug_player(player):
    """
    Prints current player info. Useful while testing.
    Remove or ignore later if you do not need it.
    """
    blank()
    print("DEBUG PLAYER DATA")
    print("-----------------")
    print(f"Callsign: {player.callsign}")
    print(f"Class: {player.class_name}")
    print(f"Rank: {player.rank}")
    print(f"XP: {player.xp}")
    print(f"Reputation: {player.reputation}")
    print(f"Medals: {player.medals}")
    print(f"Codex: {player.codex}")
    print(f"Inventory: {player.inventory}")
    print(f"Stratagems: {player.stratagems}")
    blank()

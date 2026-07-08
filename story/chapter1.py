"""
story/chapter1.py

Mission 01 gameplay scenes for Ex Umbris Fabricati.

This file contains the current terminal-game mission flow:
- Initial landing choice
- Primary objective branch
- Secondary objective branch
- Bile Titan encounter
- Mission resolution
"""

from core.text import say, narrate, radio, computer, blank
from core.responses import class_response
from core.utils import show_menu
from story.endings import final_words, thank_you


# ------------------------------------------------------------
# Chapter Entry Point
# ------------------------------------------------------------

def start_chapter_one(player):
    """Starts Mission 01 after the intro briefing."""
    first_choice(player)


# ------------------------------------------------------------
# First Branch: Landing Zone
# ------------------------------------------------------------

def first_choice(player):
    blank()
    narrate("Your squad descends through clouds of ash and amber spores.", delay=1.5)
    computer("[TACTICAL] Feeds updating with telemetry on enemy movement.", delay=0.75)
    radio("Primary objective: purge the nest network.", delay=0.75)
    radio("Secondary priorities: recover fallen guild markings and save as many SEAF personnel as possible.", delay=1)

    choice = show_menu("What do you do?", [
        "Land near the main hive and strike fast.",
        "Land near the ruined outpost and search for survivors.",
        "Land on the ridge and scout enemy movement first."
    ])

    if choice == 1:
        assault_hive(player)
    elif choice == 2:
        search_outpost(player)
    elif choice == 3:
        scout_ridge(player)


def assault_hive(player):
    blank()
    narrate("You slam into the earth beside the main hive.", delay=1.5)
    narrate("The impact crater steams around your pod as the locks release.", delay=1.5)
    narrate("Terminids surge from the tunnels in a living tide.", delay=1.75)
    blank()

    class_response(player, "assault_hive")

    blank()
    narrate("The first hive node collapses beneath coordinated fire and judicious use of grenades.", delay=2)
    second_choice(player)


def search_outpost(player):
    blank()
    narrate("Retro-thrusters fire as you divert toward the ruined outpost.", delay=1.5)
    narrate("Half-buried walls jut from the soil like broken teeth.", delay=1.5)
    narrate("Inside, you find scorched guild markings carved into a supply crate.", delay=1.75)
    narrate("Someone from the Sanctum was here.", delay=1.75)
    blank()

    class_response(player, "search_outpost")

    blank()
    computer("[SIGNAL] Hidden distress beacon detected beneath the rubble.", delay=0.75)
    second_choice(player)


def scout_ridge(player):
    blank()
    narrate("You land high above the valley.", delay=1.5)
    narrate("From the ridge, the hive network spreads below like a wound across the planet.", delay=1.75)
    narrate("You see three major tunnels feeding the swarm.", delay=1.5)
    narrate("Destroying them could cripple the entire infestation.", delay=1.75)
    blank()

    class_response(player, "scout_ridge")

    blank()
    narrate("The ridge becomes your staging ground.", delay=1.75)
    second_choice(player)


# ------------------------------------------------------------
# Second Branch: Primary Objective
# ------------------------------------------------------------

def second_choice(player):
    blank()
    narrate("The operation continues.", delay=1.25)
    narrate("Across the battlefield, more pods fall from orbit.", delay=1.5)
    narrate("Each one carries another voice of the Sanctum.", delay=1.5)
    blank()
    narrate("The Terminids respond with claws, acid, and endless hunger.", delay=1.5)
    narrate("Ex Umbris Fabricati answers with fire.", delay=1.75)

    choice = show_menu("Choose the next objective:", [
        "Collapse the hive tunnels.",
        "Recover the lost guild beacon.",
        "Hold position until reinforcements arrive."
    ])

    if choice == 1:
        collapse_hive(player)
    elif choice == 2:
        recover_beacon(player)
    elif choice == 3:
        line_hold(player)


def collapse_hive(player):
    blank()
    narrate("Charges are planted deep within the hive tunnels.", delay=1.5)
    narrate("For one breath, the whole world seems to hold still.", delay=2)
    blank()

    class_response(player, "collapse_hive")

    blank()
    narrate("Then the earth splits open with fire.", delay=1.5)
    narrate("The swarm screams beneath the soil.", delay=1.5)
    narrate("The nest network is broken.", delay=2)
    third_choice(player)


def recover_beacon(player):
    blank()
    narrate("You recover the lost guild beacon from beneath a mound of chitin and ash.", delay=1.75)
    narrate("Its signal is weak, but alive.", delay=1.5)
    blank()

    class_response(player, "recover_beacon")

    blank()
    computer("[BEACON] Partial registry recovered.", delay=0.75)
    narrate("Names scroll across the cracked display.", delay=1.5)
    narrate("Fallen members. Forgotten patrols. Voices waiting to be carried home.", delay=2)
    narrate("The Sanctum will remember them.", delay=2)
    third_choice(player)


def line_hold(player):
    blank()
    narrate("You hold the line as the swarm crashes against your position.", delay=1.5)
    narrate("Ammunition runs low. Armor cracks. The ground burns.", delay=1.75)
    blank()

    class_response(player, "line_hold")

    blank()
    narrate("Then the sky opens.", delay=1.5)
    narrate("Reinforcements descend in a storm of fire and steel.", delay=1.75)
    narrate("The line holds.", delay=2)
    third_choice(player)


# ------------------------------------------------------------
# Third Branch: Secondary Objective
# ------------------------------------------------------------

def third_choice(player):
    blank()
    computer("[HUD] Mission Success.", delay=0.75)
    narrate("A brief respite settles in.", delay=1.5)
    narrate("Then reality returns.", delay=1.5)
    narrate("You load a fresh magazine and begin your secondary objectives.", delay=1.75)

    choice = show_menu("Choose the next objective:", [
        "Push on to support the SEAF.",
        "Call down additional resources and establish a base.",
        "Scout for enemy patrols."
    ])

    if choice == 1:
        save_seaf(player)
    elif choice == 2:
        set_base(player)
    elif choice == 3:
        continue_scout(player)


def save_seaf(player):
    blank()
    narrate("As the fires around you smolder and begin to die out...", delay=1.5)
    narrate("...distant gunfire echoes across the battlefield.", delay=1.5)
    narrate("Your squad collects whatever remaining resources can be found.", delay=1.5)
    computer("[IFF] Friendly IDs detected near your location.", delay=0.75)
    blank()

    class_response(player, "save_seaf")

    blank()
    narrate("Marking the position, you press on.", delay=1.5)
    narrate("Cresting the ridge ahead, the scene sprawls out before you.", delay=1.75)
    narrate("An embattled SEAF squad is hanging by a thread against a large Terminid patrol.", delay=2)
    narrate("As you descend the ridge to render aid, the ground violently shakes...", delay=1.75)
    narrate("Debris flies through the air as a Charger appears!", delay=1.5)
    blank()
    narrate("Thoughts of your squad flash through your head...", delay=1.5)
    narrate("...thoughts of those SEAF soldiers and everything they have been through...", delay=1.75)
    narrate("...you prime your last grenade...", delay=1.5)
    narrate("...one last whisper on your lips: 'The Flame Endures.'", delay=2)
    narrate("You charge forward, sounds of glory echoing in your ears.", delay=2)

    bad_ending(player)


def set_base(player):
    blank()
    narrate("Sporadic gunfire and the smell of bug ichor permeate through your mask filters.", delay=1.75)
    narrate("Taking stock of the surroundings, the squad begins setting up landing beacons and shoring up defenses.", delay=2)
    blank()

    class_response(player, "set_base")

    blank()
    computer("[REQUISITION] Orders sent to fleet assets.", delay=0.75)
    narrate("The weight of the mission lifts ever so slightly.", delay=1.5)
    narrate("FRVs and mechs land nearby.", delay=1.5)
    narrate("Supply pods and heavy ordnance drop at key choke points.", delay=1.75)
    narrate("As the sun filters through the clouds, you see purple and gray colors lifting your heart.", delay=2)
    narrate("Then, just as you are about to hunker down for the night, the ground violently shakes!", delay=2)

    fourth_choice(player)


def continue_scout(player):
    blank()
    narrate("Once again, the squad readies up, doing final checks before setting out.", delay=1.5)
    narrate("Picking out a ridge in the distance, you continue your scouting mission.", delay=1.5)
    blank()

    class_response(player, "continue_scout")

    blank()
    narrate("Picking your way between heavily shelled ground makes for a rough advance.", delay=1.5)
    narrate("Yet you persevere, determined to ensure the safety of incoming reinforcements.", delay=1.75)
    narrate("Just as you reach the top of the ridge, an earsplitting howl tears through the air.", delay=1.75)
    narrate("Looking back on the area you just cleared... the ground opens up!", delay=1.5)
    narrate("A large Terminid hole has opened in the middle of the field.", delay=1.5)
    narrate("What you see crawling from inside ties your stomach in knots.", delay=1.75)
    narrate("You begin rushing back to understand what happened.", delay=1.5)

    fourth_choice(player)


# ------------------------------------------------------------
# Fourth Branch: Bile Titan Encounter
# ------------------------------------------------------------

def fourth_choice(player):
    blank()
    narrate("As the ground continues to shake, the piercing howl grows even louder.", delay=1.5)
    narrate("Like a creature torn from nightmare, a Bile Titan towers above you!", delay=2)
    blank()

    class_response(player, "fourth_choice")

    blank()
    narrate("Frantically, you search for some response to this awesome sight of living destruction.", delay=1.75)
    narrate("Soldiers all around you are busy evacuating or firing small arms to no effect.", delay=1.75)
    narrate("Then you see it: a behemoth of steel and gunpowder... an empty mech.", delay=2)

    choice = show_menu("Choose the next step:", [
        "Jump into the mech.",
        "Run for cover while pinging the mech for someone else to take it."
    ])

    if choice == 1:
        load_mech(player)
    elif choice == 2:
        run_cover(player)


def load_mech(player):
    blank()
    narrate("As you climb in, you feel the energy surge as the mech powers up.", delay=1.5)
    narrate("'Awesome,' you whisper to yourself, then begin configuring the controls.", delay=1.5)
    blank()

    class_response(player, "load_mech")

    blank()
    narrate("Angling the weapons toward the Bile Titan, you unleash all of your frustration at the behemoth.", delay=2)
    narrate("It struggles against the onslaught before collapsing under your fire, opening the way for your squad's counterattack.", delay=2.25)
    narrate("As mop-up operations begin, you finally take a long rest... with one eye open.", delay=2)

    final_words()
    thank_you()


def run_cover(player):
    blank()
    narrate("After a moment's hesitation, you realize your squadmate is closer than you are to the mech.", delay=1.75)
    narrate("After a quick ping for him to pilot it, you run for the nearest cover.", delay=1.5)
    blank()

    class_response(player, "run_cover")

    blank()
    narrate("He unleashes hellfire into the behemoth while the rest of you struggle to keep your heads down.", delay=1.75)
    narrate("With the beast brought low, you rise and command the countercharge!", delay=1.75)
    narrate("As mop-up operations begin, you finally take a long rest... with one eye open.", delay=2)

    final_words()
    thank_you()


# ------------------------------------------------------------
# Sacrifice Ending Branch
# ------------------------------------------------------------

def bad_ending(player):
    blank()
    narrate("The Codex is often written in the blood of the Sanctum.", delay=2)
    narrate("This story is no different.", delay=2)
    blank()

    class_response(player, "bad_ending")

    blank()
    narrate("Yet just as every ember continues to glow, this sacrifice feeds the flame...", delay=2)
    narrate("...making it burn just a little brighter.", delay=2)

    final_words()
    thank_you()

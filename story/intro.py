"""
story/intro.py

Opening story and mission briefing for Ex Umbris Fabricati.
"""

from core.text import say, narrate, computer, marshal, title_card, divider, blank


def opening():
    title_card(
        "EX UMBRIS FABRICATI",
        "Forged in Shadow. Sealed in Flame."
    )

    narrate("Before your story can be told...")
    narrate("...you must first understand ours.", delay=2.5)

    blank()
    narrate("There was a time when the stars themselves grew weary of war.", delay=2.5)
    narrate("The once-proud 286th Division carried its banners across countless worlds.", delay=2.5)
    narrate("But even the strongest steel fractures when the hammer never rests.", delay=3)

    blank()
    narrate("Campaign after campaign wore away more than armor.", delay=2)
    narrate("It wore away brotherhood.", delay=2)
    narrate("Squads drifted apart.", delay=1.75)
    narrate("Voices grew silent.", delay=2)
    narrate("And the legacy of the 286th began to fade into memory.", delay=3)

    blank()
    narrate("Most accepted the end as inevitable.", delay=2)
    narrate("One did not.", delay=2.5)

    blank()
    marshal("His name was Tiberius.", delay=2.5)
    marshal("History would remember him as the Marshal of Shadows.", delay=3)

    blank()
    narrate("Where others saw only ashes, he saw embers waiting to burn once more.", delay=3)
    narrate("From the ruins of the old division, he forged something new.", delay=2.5)

    blank()
    marshal("Not another division.", delay=2)
    marshal("Not another army.", delay=2)
    marshal("A Sanctum.", delay=3)

    blank()
    narrate("Ex Umbris Fabricati.", delay=2.5)
    narrate("Forged from the Shadows.", delay=3)

    blank()
    narrate("It was built not upon command, but upon purpose.", delay=2.5)
    narrate("A refuge for wanderers.", delay=2)
    narrate("A forge for builders.", delay=2)
    narrate("A hearth where stories would not be lost to silence.", delay=3)

    blank()
    narrate("The war continues.", delay=2)
    narrate("Worlds still burn.", delay=2)
    narrate("But Ex Umbris Fabricati endures.", delay=3)

    blank()
    marshal("Its story has already begun.", delay=2.5)
    marshal("Now...", delay=2)
    marshal("it is time to write yours.", delay=3)

    divider(1)


def sanctum_registration():
    blank()
    computer("[SYS] Establishing uplink...", delay=0.75)
    computer("[OK] Uplink stable.", delay=0.75)
    computer("[SYS] Accessing Sanctum Archives...", delay=0.75)
    computer("[OK] Archive accepted.", delay=0.75)
    computer("[SYS] Authenticating operative profile...", delay=0.75)
    computer("[AUTHORIZED] The Council has approved a new operative.", delay=1.25)
    computer("[SYS] Initializing Codex...", delay=1)
    blank()


def mission_intro(player):
    blank()
    title_card(
        "MISSION 01",
        "TERMINID FRONT"
    )

    narrate("From the Hall of Embers, beneath banners darkened by memory,", delay=2)
    narrate("the Council of Shadows issues a new decree.", delay=2.5)

    blank()
    narrate(f"{player.callsign}, {player.class_name} of the Sanctum, has been called to the front.", delay=2.5)
    narrate(player.class_flavor, delay=3)

    blank()
    computer("[BRIEFING] Target theater: Eastern Front.", delay=0.75)
    computer("[BRIEFING] Enemy presence: Terminid infestation confirmed.", delay=0.75)
    computer("[BRIEFING] Operational priority: Purge hive network.", delay=0.75)
    computer("[BRIEFING] Secondary priority: Recover guild markings and aid SEAF personnel.", delay=1.25)

    blank()
    narrate("The target worlds are places of black soil, burning spores, and endless movement beneath the ground.", delay=3)
    narrate("The fleet gathers.", delay=2)
    narrate("Drop pods fire.", delay=2)
    narrate("The forge opens.", delay=3)
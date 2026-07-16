"""
story/chapter2.py

Chapter 02 for Ex Umbris Fabricati.

Operation: HOLLOW CROWN
Front: Terminid
Purpose:
- Continues the Terminid campaign after Chapter 01
- Contains four major decision points
- Provides unique class-specific responses for all ten classes
- Remains compatible with the current Player-only architecture
- GameState support will be added later
"""

from core.text import (
    say,
    narrate,
    computer,
    radio,
    npc,
    title_card,
    blank,
)

MISSION_NAME = "OPERATION HOLLOW CROWN"
MISSION_FRONT = "TERMINID FRONT"
MISSION_PLANET = "KHEPRI'S VEIL"

CLASS_RESPONSES = {
    "spore_canyon": {
        "Voidrunner": [
            "You move ahead before the squad can question the route.",
            "The canyon twists like a wound, but every broken ledge becomes another path."
        ],
        "Grimshield": [
            "You take point where the canyon narrows.",
            "If the spores conceal an ambush, the swarm will meet your armor first."
        ],
        "Ashreaver": [
            "The thick spores cling to your armor and hiss against heated metal.",
            "You tighten your grip. If the canyon wants fire, you will oblige."
        ],
        "Nightreaper": [
            "The haze swallows your outline almost immediately.",
            "For once, the planet itself seems eager to hide you."
        ],
        "Umbracaster": [
            "The drifting spores distort distance and sound.",
            "To others it is confusion. To you it is a language waiting to be read." #reads awkwardly
        ],
        "Ritesmith": [
            "You mark anchor points along the canyon walls as you descend.",
            "A retreat route is only useful if someone prepares it before panic begins."
        ],
        "Oathkeeper": [
            "You check every squad seal before entering the haze.",
            "The enemy may be unseen, but suffocation is no less lethal than claws."
        ],
        "Fluxhunter": [
            "You study the changing currents and identify movement beneath the fog.",
            "The canyon hides many things, but not from a patient eye."
        ],
        "Fumebinder": [
            "The canyon's natural haze bends around your own smoke canisters.",
            "Within moments, you control which shadows belong to the planet and which belong to you."
        ],
        "Emberbrand": [
            "Amber spores drift across your visor like sparks from a dying forge.",
            "You step into them without hesitation."
        ],
    },
    "shattered_ridge": {
        "Voidrunner": [
            "The broken ridge offers speed, height, and a dozen impossible jumps.",
            "You choose the fastest route and trust the others to keep up."
        ],
        "Grimshield": [
            "You move across the exposed ridge with deliberate steps.",
            "There is no cover, so you become it."
        ],
        "Ashreaver": [
            "From the ridge, every hive opening below looks like a target marker.",
            "You begin deciding which one deserves to burn first."
        ],
        "Nightreaper": [
            "Open ground is rarely your preference.",
            "Still, every shard of stone casts a shadow, and every shadow is enough."
        ],
        "Umbracaster": [
            "The ridge reveals the infestation's scale.",
            "Patterns emerge in the movement below, vast and almost ritualistic."
        ],
        "Ritesmith": [
            "You test each fractured plate of stone before the squad crosses.",
            "The ridge is unstable, but instability can be measured."
        ],
        "Oathkeeper": [
            "You keep the squad tightly spaced and watch every step.",
            "One fall would be as deadly as any Terminid."
        ],
        "Fluxhunter": [
            "The height gives you what you need: distance, angle, and time.",
            "Below, patrol routes become clean lines waiting to be broken."
        ],
        "Fumebinder": [
            "There is nowhere to hide on the ridge.",
            "You answer by creating concealment where none existed."
        ],
        "Emberbrand": [
            "Wind tears at your cape as the battlefield opens beneath you.",
            "The sight does not diminish your resolve. It feeds it."
        ],
    },
    "destroy_roost": {
        "Voidrunner": [
            "You sprint beneath the circling swarm, changing direction before each dive.",
            "By the time the Shriekers commit, you are already beneath their nest."
        ],
        "Grimshield": [
            "Wings hammer against your armor as you hold the approach.",
            "Every impact buys the demolition team another second."
        ],
        "Ashreaver": [
            "You answer the sky with fire.",
            "Burning wings spiral downward while the roost begins to collapse."
        ],
        "Nightreaper": [
            "You time each movement between the Shriekers' passes.",
            "The nest never understands how death reached its center."
        ],
        "Umbracaster": [
            "You track the rhythm of each diving wave.",
            "A pattern this precise only needs to be disrupted once."
        ],
        "Ritesmith": [
            "Charges lock into the roost's support columns with ritual precision.",
            "The structure will fall inward, burying its brood beneath it."
        ],
        "Oathkeeper": [
            "You keep one hand near your stim pistol while firing with the other.",
            "No one is dragged into the sky while you still stand."
        ],
        "Fluxhunter": [
            "You pick Shriekers from the air one by one.",
            "Each shot opens another safe second for the squad below."
        ],
        "Fumebinder": [
            "Smoke spreads through the roost's lower chambers.",
            "The Shriekers descend blind and find prepared weapons waiting."
        ],
        "Emberbrand": [
            "The nest ignites from within.",
            "For a moment, the whole ridge wears a crown of flame."
        ],
    },
    "rescue_surveyors": {
        "Voidrunner": [
            "You find the shortest line through the swarm and take it at full speed.",
            "The trapped surveyors see you only seconds before rescue arrives."
        ],
        "Grimshield": [
            "You plant yourself between the survey team and the advancing bugs.",
            "Their retreat begins behind the certainty of your armor."
        ],
        "Ashreaver": [
            "You carve a corridor through the infestation with brutal efficiency.",
            "The surveyors do not ask what happened to the bugs in your path."
        ],
        "Nightreaper": [
            "You appear beside the trapped team without warning.",
            "The first sign of rescue is the sound of their pursuers falling."
        ],
        "Umbracaster": [
            "You redirect the swarm with false movement and scattered signals.",
            "The surveyors escape while the enemy hunts ghosts."
        ],
        "Ritesmith": [
            "You stabilize the survey beacon and restore its damaged locator.",
            "A rescue becomes far easier once the lost can finally be seen."
        ],
        "Oathkeeper": [
            "You reach the wounded first.",
            "The mission can wait long enough for a pulse to be preserved."
        ],
        "Fluxhunter": [
            "You remove the largest threats before the surveyors begin moving.",
            "Precision turns a desperate retreat into an orderly extraction."
        ],
        "Fumebinder": [
            "A smoke corridor forms between the survey team and your position.",
            "They vanish from the swarm's sight and reappear behind your line."
        ],
        "Emberbrand": [
            "You raise a wall of flame behind the retreating surveyors.",
            "The bugs recoil, and hope moves through the opening."
        ],
    },
    "plant_charges": {
        "Voidrunner": [
            "You carry the final charge deeper than the plan requires.",
            "The best collapse begins where the enemy feels safest."
        ],
        "Grimshield": [
            "You brace the tunnel while the others work.",
            "Stone falls, claws scrape closer, and still you do not move."
        ],
        "Ashreaver": [
            "The charge indicator turns green beneath your hand.",
            "You almost pity the hive for what comes next."
        ],
        "Nightreaper": [
            "You slip past sleeping brood chambers to place the detonator.",
            "Silence holds until the instant it no longer matters."
        ],
        "Umbracaster": [
            "You feel the hive's pulse through the tunnel walls.",
            "The charges are not merely explosives now. They are interruptions in a living rhythm."
        ],
        "Ritesmith": [
            "Every charge is aligned to the fault lines beneath the hive.",
            "When the pattern completes, the underground kingdom will fold into itself."
        ],
        "Oathkeeper": [
            "You count the squad twice before arming the sequence.",
            "No detonation begins until every living voice answers."
        ],
        "Fluxhunter": [
            "You wait for the brood mass to gather over the weakest section.",
            "One trigger will achieve what thousands of rounds could not."
        ],
        "Fumebinder": [
            "You flood the tunnels with smoke before withdrawal.",
            "The pursuing swarm runs blind toward the armed charges."
        ],
        "Emberbrand": [
            "Red lights blink along the cavern walls.",
            "To you, they look like embers waiting for breath."
        ],
    },
    "recover_intel": {
        "Voidrunner": [
            "You reach the brood archive before the swarm closes the route.",
            "The data core is in your hands before the danger fully understands you were there."
        ],
        "Grimshield": [
            "You stand over the extraction team as the hive converges.",
            "Information is fragile. Your defense is not."
        ],
        "Ashreaver": [
            "The organic archive disgusts you.",
            "You take what the Sanctum needs and promise the rest to the flames."
        ],
        "Nightreaper": [
            "You move among dormant brood sacs without disturbing a single membrane.",
            "The hive yields its secrets without ever seeing your face."
        ],
        "Umbracaster": [
            "The patterns inside the brood archive are alien but not meaningless.",
            "For a moment, you glimpse how the infestation thinks."
        ],
        "Ritesmith": [
            "You adapt the survey team's scanner to read organic memory tissue.",
            "A tool built for stone now extracts the history of a species."
        ],
        "Oathkeeper": [
            "You guard the technicians while they work.",
            "Knowledge may save future lives, and that makes it worth defending."
        ],
        "Fluxhunter": [
            "You identify the one brood cluster carrying command markers.",
            "The hive hid its intelligence among thousands. You needed only one."
        ],
        "Fumebinder": [
            "A controlled haze masks the technicians' heat signatures.",
            "The hive searches within arm's reach and finds nothing."
        ],
        "Emberbrand": [
            "The brood archive throbs beneath your hand.",
            "You resist the urge to burn it until the final data packet clears."
        ],
    },
    "collapse_queen": {
        "Voidrunner": [
            "You race the collapse itself, leaping over widening fractures.",
            "The Queen's final roar follows you into daylight."
        ],
        "Grimshield": [
            "You remain at the rear until every squadmate clears the chamber.",
            "Only then do you turn from the falling mountain."
        ],
        "Ashreaver": [
            "You trigger the charges with satisfaction.",
            "The Queen is buried beneath fire, stone, and the weight of her own empire."
        ],
        "Nightreaper": [
            "You leave the final detonator at the Queen's feet.",
            "She never sees who condemns her throne."
        ],
        "Umbracaster": [
            "The chamber's living rhythm fractures all at once.",
            "The hive's song ends beneath a continent of stone."
        ],
        "Ritesmith": [
            "The collapse follows the exact geometry you designed.",
            "A kingdom dies according to blueprint."
        ],
        "Oathkeeper": [
            "You confirm every heartbeat before pressing the trigger.",
            "The chamber falls only after the living are safely beyond it."
        ],
        "Fluxhunter": [
            "You fire into the final support column at precisely the right moment.",
            "The entire chamber answers that single shot."
        ],
        "Fumebinder": [
            "Smoke hides the squad's retreat from the enraged brood.",
            "They chase shadows until the ceiling becomes their grave."
        ],
        "Emberbrand": [
            "Flame races through the fault lines before the chamber falls.",
            "The Queen's crown becomes a funeral pyre."
        ],
    },
    "fight_queen": {
        "Voidrunner": [
            "You circle the Queen faster than her claws can follow.",
            "Every missed strike exposes another piece of her armor."
        ],
        "Grimshield": [
            "You take the Queen's charge head-on.",
            "The impact drives you backward, but it does not break the line."
        ],
        "Ashreaver": [
            "You meet the Queen with overwhelming violence.",
            "Her chamber becomes an altar to ammunition and flame."
        ],
        "Nightreaper": [
            "You strike beneath the plates protecting her throat.",
            "Even a Queen has places the dark can reach."
        ],
        "Umbracaster": [
            "You read the Queen's fury before each attack begins.",
            "Her rage makes her powerful. It also makes her predictable."
        ],
        "Ritesmith": [
            "You redirect damaged equipment into a crude containment rig.",
            "The Queen dies, and the sample survives because you planned for both."
        ],
        "Oathkeeper": [
            "You keep the squad standing through every acid wave and crushing impact.",
            "The Queen cannot outlast a team that refuses to remain wounded."
        ],
        "Fluxhunter": [
            "You wait until the Queen lifts her armored crown.",
            "One shot enters the exposed nerve cluster, and the throne collapses."
        ],
        "Fumebinder": [
            "Smoke and corrosive mist fill the chamber.",
            "The Queen attacks shapes that no longer exist while the real squad closes in."
        ],
        "Emberbrand": [
            "You set the Queen ablaze and refuse to let the fire die.",
            "When she falls, the entire chamber glows."
        ],
    },
}


def class_response(player, response_key):
    """Print the response associated with the player's class."""
    class_name = player.class_name
    response_group = CLASS_RESPONSES.get(response_key, {})
    lines = response_group.get(
        class_name,
        [
            "You steady yourself and move with the squad.",
            "Whatever waits ahead, the mission continues."
        ],
    )

    for line in lines:
        narrate(line)


def get_choice(prompt, options):
    """Display a numbered menu until the player makes a valid choice."""
    while True:
        blank()
        print(prompt)
        print()

        for index, option in enumerate(options, start=1):
            print(f"[{index}] {option}")

        print()
        choice = input("Select an option: ").strip()

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(options):
                return number

        say("Invalid selection. Choose one of the available options.")


def start_mission_02(player, state):
    """Begin Mission 02."""
    mission_briefing(player, state)
    decision_one(player, state)


def mission_briefing(player, state):
    title_card(MISSION_NAME, MISSION_FRONT)

    computer(f"[PLANET] {MISSION_PLANET}", delay=0.7)
    computer("[THREAT] TERMINID SUPER-COLONY CONFIRMED", delay=0.7)
    computer("[PRIMARY] LOCATE AND DESTROY SUBTERRANEAN QUEEN", delay=0.7)
    computer("[SECONDARY] RECOVER SEAF SURVEY DATA", delay=0.7)
    computer("[WARNING] MASSIVE UNDERGROUND MOVEMENT DETECTED", delay=1)

    blank()
    radio("[COMMAND CHANNEL]", delay=0.5)

    npc("Tiberius", "The nest destroyed during your last deployment was not the infestation's center.")
    npc("Tiberius", "It was a doorway.")

    blank()

    narrate("Deep beneath Khepri's Veil, the surviving tunnels converge around a single organism.")
    narrate("A Terminid Queen has transformed the planet's crust into a breeding ground.")
    narrate("If she survives, every victory on this front becomes temporary.")

    blank()

    npc("Tiberius", f"{player.callsign}, descend into the hive.")
    npc("Tiberius", "Break the crown.")
    npc("Tiberius", "Return with whoever still draws breath.")

    blank()

    computer(">> DROP VECTOR LOCKED", delay=0.6)
    computer(">> ATMOSPHERIC ENTRY CONFIRMED", delay=0.6)
    computer(">> IMPACT IN 5...", delay=0.5)
    computer(">> 4...", delay=0.5)
    computer(">> 3...", delay=0.5)
    computer(">> 2...", delay=0.5)
    computer(">> 1...", delay=0.8)

    blank()
    say("IMPACT", delay=1)
    blank()

    narrate("Your drop pod strikes the surface of Khepri's Veil hard enough to split the black soil around it.")
    narrate("The hatch blows open into a world of amber spores, broken stone, and distant inhuman cries.")


def decision_one(player, state):
    choice = get_choice(
        "The hive entrance lies beyond two possible approaches.",
        [
            "Descend through the spore canyon.",
            "Advance across the shattered ridge.",
        ],
    )

    if choice == 1:
        route_spore_canyon(player, state)
    else:
        route_shattered_ridge(player, state)


def route_spore_canyon(player, state):
    blank()
    title_card("APPROACH", "SPORE CANYON")

    narrate("The squad descends into a narrow canyon where the air glows with drifting Terminid spores.")
    narrate("Visibility falls to a few meters. Every sound returns from the stone in distorted echoes.")

    blank()
    class_response(player, state, "spore_canyon")
    blank()

    narrate("Halfway through the canyon, a patrol erupts from the haze.")
    narrate("The fight is close, confused, and brutal, but the squad reaches the far side intact.")
    narrate("Ahead, the canyon opens beneath the shadow of a massive Shrieker roost.")

    decision_two(player, state)


def route_shattered_ridge(player, state):
    blank()
    title_card("APPROACH", "SHATTERED RIDGE")

    narrate("The squad climbs onto a ridge broken by orbital bombardment.")
    narrate("Below, the infestation stretches across the valley in pulsing mounds of chitin and earth.")

    blank()
    class_response(player, state, "shattered_ridge")
    blank()

    narrate("The height reveals two urgent signals.")
    narrate("A Shrieker roost dominates the airspace, while a damaged SEAF survey beacon flashes from the valley floor.")

    decision_two(player, state)


def decision_two(player, state):
    choice = get_choice(
        "Both objectives matter, but the hive is already reacting to your arrival.",
        [
            "Destroy the Shrieker roost.",
            "Rescue the trapped SEAF survey team.",
        ],
    )

    if choice == 1:
        destroy_shrieker_roost(player, state)
    else:
        rescue_seaf_surveyors(player, state)


def destroy_shrieker_roost(player, state):
    blank()
    title_card("SECONDARY OBJECTIVE", "DESTROY SHRIEKER ROOST")

    narrate("The roost rises from the valley like a tower of hardened flesh.")
    narrate("Shriekers pour from its openings, blotting out pieces of the sky.")

    blank()
    class_response(player, state, "destroy_roost")
    blank()

    narrate("The final charges detonate beneath the structure.")
    narrate("The roost folds inward, dragging burning wings and shattered brood chambers into the valley.")

    computer("[OBJECTIVE COMPLETE] SHRIEKER ROOST DESTROYED", delay=1)

    blank()

    narrate("Among the debris, you recover a damaged survey transponder.")
    narrate("Its final coordinates point toward a concealed opening beneath the hive.")

    decision_three(player, state)


def rescue_seaf_surveyors(player, state):
    blank()
    title_card("SECONDARY OBJECTIVE", "RESCUE SEAF SURVEY TEAM")

    narrate("The survey team has barricaded itself inside the remains of a geological station.")
    narrate("Terminids batter the outer walls while a wounded technician tries to keep the beacon alive.")

    blank()
    class_response(player, "rescue_surveyors")
    blank()

    narrate("The final survivor crosses into your line moments before the station collapses beneath the swarm.")

    npc("Survey Lead", "We found something below the main nest.")
    npc("Survey Lead", "A chamber large enough to contain an organism we've never recorded.")

    blank()

    computer("[OBJECTIVE COMPLETE] SEAF SURVEY TEAM RECOVERED", delay=1)

    blank()

    narrate("The survey data reveals a hidden descent route leading directly into the lower hive.")

    decision_three(player, state)


def decision_three(player, state):
    blank()

    narrate("The hidden entrance descends beneath the planet's crust.")
    narrate("The walls pulse faintly around you, warm with the movement of countless organisms.")

    choice = get_choice(
        "The lower hive contains both a structural fault and an organic data archive.",
        [
            "Plant seismic charges along the fault.",
            "Recover the brood intelligence archive.",
        ],
    )

    if choice == 1:
        plant_seismic_charges(player, state)
    else:
        recover_brood_intelligence(player, state)


def plant_seismic_charges(player, state):
    blank()
    title_card("LOWER HIVE", "SEISMIC FAULT")

    narrate("The fault cuts through the hive like a dark seam.")
    narrate("Each seismic charge must be carried deeper while the brood closes behind you.")

    blank()
    class_response(player, "plant_charges")
    blank()

    computer(">> SEISMIC CHARGE 01 ARMED", delay=0.5)
    computer(">> SEISMIC CHARGE 02 ARMED", delay=0.5)
    computer(">> SEISMIC CHARGE 03 ARMED", delay=0.5)
    computer(">> REMOTE DETONATION LINK ACTIVE", delay=0.8)

    blank()

    narrate("The charges can destroy the lower hive, but only if the Queen remains inside when they detonate.")

    decision_four(player, state)


def recover_brood_intelligence(player, state):
    blank()
    title_card("LOWER HIVE", "BROOD ARCHIVE")

    narrate("The archive is not a machine.")
    narrate("It is a living cluster of membranes, nerve fibers, and preserved genetic memory.")

    blank()
    class_response(player, "recover_intel")
    blank()

    computer(">> ORGANIC DATA LINK ESTABLISHED", delay=0.6)
    computer(">> BROOD PATTERNS DOWNLOADING...", delay=0.8)
    computer(">> QUEEN SIGNAL IDENTIFIED", delay=0.8)
    computer(">> ARCHIVE RECOVERY COMPLETE", delay=1)

    blank()

    narrate("The recovered data reveals the Queen's location and something worse:")
    narrate("she has already produced another generation of command-brood eggs.")

    decision_four(player, state)


def decision_four(player, state):
    blank()

    narrate("The tunnel opens into a chamber vast enough to swallow a city block.")
    narrate("At its center rises the Terminid Queen, plated in scarred armor and surrounded by rows of command-brood eggs.")

    blank()

    narrate("Her roar shakes dust from the cavern roof.")
    narrate("Every tunnel behind you erupts with the sound of the approaching swarm.")

    choice = get_choice(
        "The Hollow Crown must end here.",
        [
            "Collapse the Queen's chamber and bury everything.",
            "Kill the Queen directly and recover a command-brood sample.",
        ],
    )

    if choice == 1:
        collapse_queens_chamber(player, state)
    else:
        fight_queen_for_sample(player, state)


def collapse_queens_chamber(player, state):
    blank()
    title_card("FINAL OBJECTIVE", "BREAK THE CROWN")

    narrate("The squad retreats toward the structural fault while the Queen and her brood pursue.")
    narrate("The remote detonator flashes in your hand.")

    blank()
    class_response(player, "collapse_queen")
    blank()

    say("DETONATE", delay=0.8)

    blank()

    narrate("The seismic charges fire in sequence.")
    narrate("The chamber twists, fractures, and disappears beneath millions of tons of stone.")
    narrate("The Queen's roar becomes a distant vibration, then nothing.")

    computer("[PRIMARY OBJECTIVE COMPLETE] QUEEN ELIMINATED", delay=0.8)
    computer("[HIVE STATUS] CATASTROPHIC COLLAPSE CONFIRMED", delay=0.8)

    mission_extraction(player, outcome="collapse")


def fight_queen_for_sample(player, state):
    blank()
    title_card("FINAL OBJECTIVE", "TAKE THE CROWN")

    narrate("The squad enters the chamber instead of retreating.")
    narrate("The Queen lowers her armored head and charges.")

    blank()
    class_response(player, "fight_queen")
    blank()

    narrate("The battle tears through the chamber.")
    narrate("Acid floods the stone. Armor breaks. Ammunition counters fall toward empty.")
    narrate("At last, the Queen crashes beside her ruined throne.")

    computer("[PRIMARY OBJECTIVE COMPLETE] QUEEN ELIMINATED", delay=0.8)
    computer("[SAMPLE] COMMAND-BROOD TISSUE SECURED", delay=0.8)

    mission_extraction(player, outcome="sample")


def mission_extraction(player, state, outcome):
    blank()

    radio("[EXTRACTION CHANNEL]", delay=0.5)
    npc("Pelican Pilot", "Extraction beacon received.")
    npc("Pelican Pilot", "You have two minutes before the whole valley wakes up.")

    blank()

    narrate("You emerge from the lower hive beneath a sky darkened by spores.")
    narrate("The ground behind you ruptures as surviving Terminids pour from every remaining tunnel.")

    blank()

    narrate("The Pelican descends through the swarm with weapons firing.")
    narrate("The ramp strikes the ground, and the squad boards beneath a storm of claws, smoke, and tracer fire.")

    blank()

    npc("Pelican Pilot", "You're all aboard.")
    npc("Pelican Pilot", "That already makes this a better day than most.")

    blank()

    computer(">> EXTRACTION CONFIRMED", delay=0.8)
    computer(f">> OPERATIVE VERIFIED: {player.callsign.upper()}", delay=0.8)

    blank()

    if outcome == "collapse":
        narrate("From the rising Pelican, you watch the valley sink inward.")
        narrate("The Hollow Crown is gone, buried with its Queen beneath the planet.")
        npc("Tiberius", "The infestation has lost its center. The front will remember this victory.")
    else:
        narrate("The containment case pulses faintly beside you.")
        narrate("The Queen is dead, but part of her command-brood now travels toward the Sanctum laboratories.")
        npc("Tiberius", "The sample may save lives in battles we have not yet fought.")
        npc("Tiberius", "Ensure it remains contained.")

    blank()

    title_card("MISSION COMPLETE", MISSION_NAME)

    computer("[STATUS] TERMINID QUEEN ELIMINATED", delay=0.6)
    computer("[STATUS] LOWER HIVE NEUTRALIZED", delay=0.6)
    computer("[STATUS] OPERATIVE RETURNING TO THE SPEAR OF TARTARUS", delay=1)

    blank()

    npc("Caz", "You came back standing.")
    npc("Caz", "I appreciate professional courtesy.")

    blank()

    npc("Brexor", "Another victory for the ship I named.")

    blank()

    npc("Unknown Crew Member", "You still did not name it.")

    blank()

    npc("Brexor", "The truth survives another mission.")

    blank()

    narrate("Khepri's Veil disappears beneath the clouds.")
    narrate("The Terminid front is quieter than it was before your arrival.")
    narrate("For now, that is enough.")

    blank()


#if __name__ == "__main__":
#    print("Mission 02 is intended to be launched through the main game with a valid Player object.")

#Run below code as a helper to test the individual mission | change the class type to test out different text from each class
if __name__ == "__main__":
    from core.player import Player
    from core.classes import CLASSES

    test_player = Player()

    test_player.callsign = "TEST DIVER"
    test_player.player_class = CLASSES["fluxhunter"]

    start_mission_02(test_player)
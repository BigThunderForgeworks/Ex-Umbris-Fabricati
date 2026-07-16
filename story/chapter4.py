"""
story/mission_04_automatons.py

Mission 04 for Ex Umbris Fabricati.

Operation: BLACK FURNACE
Front: Automaton
Purpose:
- Continues the Automaton campaign after Operation Iron Echo
- Contains four major decision points
- Provides unique class-specific responses for all ten classes
- Includes two distinct final outcomes
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


# ============================================================
# Mission Configuration
# ============================================================

MISSION_NAME = "OPERATION BLACK FURNACE"
MISSION_FRONT = "AUTOMATON FRONT"
MISSION_PLANET = "MORDREN'S WAKE"


# ============================================================
# Class-Specific Responses
#
# Each major branch has a response for every playable class.
# This keeps the mission logic separate from class flavor text.
# ============================================================

CLASS_RESPONSES = {
    # --------------------------------------------------------
    # Decision 1A: Cross the ash fields
    # --------------------------------------------------------
    "ash_fields": {
        "Voidrunner": [
            "You sprint between impact craters while ash storms erase your trail.",
            "The open ground becomes a race the machines were never built to win."
        ],
        "Grimshield": [
            "You advance through the ash with your weapon raised and armor forward.",
            "The squad follows the moving wall you create."
        ],
        "Ashreaver": [
            "The ash fields feel familiar in the worst possible way.",
            "You answer the ruined horizon with ruin of your own."
        ],
        "Nightreaper": [
            "Smoke and drifting soot hide every movement.",
            "You become another shadow in a landscape already made of darkness."
        ],
        "Umbracaster": [
            "The ash storm scatters signal returns and bends distance.",
            "The enemy sees uncertainty. You see opportunity."
        ],
        "Ritesmith": [
            "You test the magnetic interference in the soil before moving.",
            "The field is dangerous, but its danger has a measurable pattern."
        ],
        "Oathkeeper": [
            "You keep the squad close enough to reach, but far enough apart to survive artillery.",
            "Every step is taken with the living in mind."
        ],
        "Fluxhunter": [
            "You watch the horizon through thermal distortion.",
            "Red optics flicker in the ash, and each one becomes a target."
        ],
        "Fumebinder": [
            "You add controlled smoke to the natural ash cloud.",
            "The battlefield becomes yours long before the machines understand they have lost sight of it."
        ],
        "Emberbrand": [
            "Orange light pulses through the storm like a buried furnace.",
            "You walk toward it as though answering a challenge."
        ],
    },

    # --------------------------------------------------------
    # Decision 1B: Infiltrate the mag-rail tunnel
    # --------------------------------------------------------
    "mag_rail_tunnel": {
        "Voidrunner": [
            "You move along the maintenance ledges without slowing.",
            "The tunnel was built for trains, not for someone willing to ignore the intended path."
        ],
        "Grimshield": [
            "You lead the squad through the narrow tunnel.",
            "If anything emerges from the dark, it will meet you first."
        ],
        "Ashreaver": [
            "The tunnel amplifies every gunshot into thunder.",
            "You seem entirely pleased by the arrangement."
        ],
        "Nightreaper": [
            "The darkness is complete between passing power surges.",
            "You time every movement to the black intervals."
        ],
        "Umbracaster": [
            "The tunnel's signal repeaters speak to one another in machine pulses.",
            "You begin altering the conversation."
        ],
        "Ritesmith": [
            "You identify the rail's emergency power couplings.",
            "The tunnel can become a weapon if the system is persuaded to cooperate."
        ],
        "Oathkeeper": [
            "You check the squad's footing and oxygen seals before advancing.",
            "A rescue tunnel becomes a grave if one mistake is ignored."
        ],
        "Fluxhunter": [
            "The tunnel offers long, clean sight lines.",
            "Every approaching patrol announces itself far too early."
        ],
        "Fumebinder": [
            "A low smoke layer rolls between the rails.",
            "Automaton optics detect motion everywhere and certainty nowhere."
        ],
        "Emberbrand": [
            "Blue current crawls across the rails beneath your boots.",
            "The tunnel feels like a forge that has forgotten how to burn."
        ],
    },

    # --------------------------------------------------------
    # Decision 2A: Destroy the anti-air nexus
    # --------------------------------------------------------
    "destroy_aa_nexus": {
        "Voidrunner": [
            "You move beneath the tracking arcs before the batteries finish rotating.",
            "The nexus cannot target what it cannot keep centered."
        ],
        "Grimshield": [
            "You draw the batteries' fire while the demolition team closes in.",
            "The guns spend their last moments shooting at the one target that refuses to fall."
        ],
        "Ashreaver": [
            "You turn the nexus into a chain reaction.",
            "One ammunition rack ignites the next until the entire platform tears itself apart."
        ],
        "Nightreaper": [
            "You reach the control bunker through a drainage channel.",
            "The batteries die without firing a final warning."
        ],
        "Umbracaster": [
            "You corrupt the tracking logic and assign every battery the same false target.",
            "The nexus destroys its own command mast."
        ],
        "Ritesmith": [
            "You reverse the ammunition-feed safeties.",
            "The system loads, cycles, and detonates exactly as designed—just not as intended."
        ],
        "Oathkeeper": [
            "You keep the assault team standing while flak bursts around the platform.",
            "The nexus falls because nobody is lost before the charges are placed."
        ],
        "Fluxhunter": [
            "You target the fire-control relays in sequence.",
            "The entire network goes blind one precise shot at a time."
        ],
        "Fumebinder": [
            "Smoke hides the approach beneath the anti-air radar horizon.",
            "The first warning the nexus receives is the sound of charges locking into place."
        ],
        "Emberbrand": [
            "The ammunition towers erupt in columns of flame.",
            "For a moment, the entire sky belongs to you."
        ],
    },

    # --------------------------------------------------------
    # Decision 2B: Reactivate the SEAF orbital beacon
    # --------------------------------------------------------
    "reactivate_beacon": {
        "Voidrunner": [
            "You cross the ruined relay station before the patrol can surround it.",
            "The beacon is online while the enemy still believes the site abandoned."
        ],
        "Grimshield": [
            "You hold the relay platform while the beacon cycles.",
            "Every incoming round is one less aimed at the technician behind you."
        ],
        "Ashreaver": [
            "You clear the relay yard with brutal speed.",
            "The beacon rises over a field of broken machines."
        ],
        "Nightreaper": [
            "You eliminate the spotters first.",
            "The beacon returns to life without ever drawing the larger force's attention."
        ],
        "Umbracaster": [
            "You disguise the beacon's signal as Automaton maintenance traffic.",
            "The fleet receives the coordinates while the machines ignore them."
        ],
        "Ritesmith": [
            "You rebuild the transmitter from scorched components and a spare targeting module.",
            "The beacon works because you refuse to accept that it should not."
        ],
        "Oathkeeper": [
            "You stabilize the wounded relay operator before restoring the signal.",
            "The beacon returns because the person who knew its codes survives."
        ],
        "Fluxhunter": [
            "You pick apart the patrol guarding the station from the ridge.",
            "The technicians work under a silence created by your aim."
        ],
        "Fumebinder": [
            "Smoke conceals the beacon's heat signature during startup.",
            "By the time the enemy detects it, the signal is already in orbit."
        ],
        "Emberbrand": [
            "You cauterize a ruptured conduit with controlled heat.",
            "The beacon answers with a column of white light."
        ],
    },

    # --------------------------------------------------------
    # Decision 3A: Sabotage the geothermal extractors
    # --------------------------------------------------------
    "sabotage_extractors": {
        "Voidrunner": [
            "You leap between extractor platforms above the molten channels.",
            "Charges appear across the network before the guards can predict your route."
        ],
        "Grimshield": [
            "You brace the main access bridge while the sabotage team works.",
            "Heat and gunfire build around you, but the crossing remains secure."
        ],
        "Ashreaver": [
            "You rupture the fuel regulators and let pressure do the rest.",
            "The extraction complex begins dying from the inside."
        ],
        "Nightreaper": [
            "You move through service ducts beneath the machinery.",
            "The extractors fail before anyone sees an intruder."
        ],
        "Umbracaster": [
            "You falsify pressure readings across the network.",
            "The machines continue feeding energy into a system already beyond recovery."
        ],
        "Ritesmith": [
            "You reconfigure the geothermal governors into a destructive feedback loop.",
            "The planet's own heat becomes the weapon."
        ],
        "Oathkeeper": [
            "You keep the engineers alive through every breach and counterattack.",
            "The sabotage succeeds because none of the specialists fall."
        ],
        "Fluxhunter": [
            "You fire through the exposed regulator housings.",
            "Each shot disables one more extractor without touching the molten channels."
        ],
        "Fumebinder": [
            "Steam and smoke merge across the platforms.",
            "The defenders lose the entire facility in a cloud they cannot read."
        ],
        "Emberbrand": [
            "The extractors begin to glow from within.",
            "You watch the machinery become a furnace worthy of the operation's name."
        ],
    },

    # --------------------------------------------------------
    # Decision 3B: Seize the armored supply convoy
    # --------------------------------------------------------
    "seize_convoy": {
        "Voidrunner": [
            "You reach the lead transport and board it at full speed.",
            "The convoy changes ownership before the rear vehicles understand the attack has begun."
        ],
        "Grimshield": [
            "You stand in the road and force the convoy to stop.",
            "The machines discover that momentum means little against something that will not move."
        ],
        "Ashreaver": [
            "You destroy the escort vehicles and leave the supply carriers intact.",
            "Restraint lasts exactly as long as the objective requires."
        ],
        "Nightreaper": [
            "You remove the drivers and gunners before the convoy reaches the ambush point.",
            "The vehicles roll into your hands under their own power."
        ],
        "Umbracaster": [
            "You inject a false route update into the convoy network.",
            "The machines deliver their supplies directly to the Sanctum."
        ],
        "Ritesmith": [
            "You override the transport locks and rewrite the vehicle controls.",
            "The convoy becomes useful the moment you understand how it was built."
        ],
        "Oathkeeper": [
            "You protect the captured drivers and wounded scouts during the seizure.",
            "The mission gains supplies without sacrificing the people who secured them."
        ],
        "Fluxhunter": [
            "You disable the escort optics and wheel assemblies in sequence.",
            "The convoy stops exactly where you intended."
        ],
        "Fumebinder": [
            "Smoke engulfs the road while false engine signatures appear on both flanks.",
            "The convoy drives into the ambush without ever identifying it."
        ],
        "Emberbrand": [
            "You burn through the final escort and leave the cargo untouched.",
            "The supplies are captured beneath a halo of fire."
        ],
    },

    # --------------------------------------------------------
    # Decision 4A: Overload the Black Furnace
    # --------------------------------------------------------
    "overload_furnace": {
        "Voidrunner": [
            "You race across collapsing catwalks to reach the manual override.",
            "The furnace begins to overload as the floor disappears behind you."
        ],
        "Grimshield": [
            "You hold the reactor bridge against the final defensive wave.",
            "The overload completes because nothing forces you from the line."
        ],
        "Ashreaver": [
            "You feed the furnace every explosive charge still available.",
            "The core answers with a roar that drowns out the entire complex."
        ],
        "Nightreaper": [
            "You enter the control chamber through the coolant vents.",
            "The reactor dies without ever identifying the hand that killed it."
        ],
        "Umbracaster": [
            "You lock the furnace into contradictory emergency states.",
            "The core tears itself apart trying to obey every command at once."
        ],
        "Ritesmith": [
            "You disable the containment safeties in the exact order required.",
            "The furnace becomes a weapon assembled from its own design."
        ],
        "Oathkeeper": [
            "You drag the wounded engineer to the override panel and keep them conscious.",
            "The final sequence completes because one more life refuses to end."
        ],
        "Fluxhunter": [
            "You fire into the exposed containment relay at the precise moment of maximum pressure.",
            "One shot turns the reactor unstable."
        ],
        "Fumebinder": [
            "Smoke fills the control level and blinds the final defenders.",
            "They never see the overload sequence begin."
        ],
        "Emberbrand": [
            "The furnace burns brighter than the sun beneath the planet.",
            "You stand before it without looking away."
        ],
    },

    # --------------------------------------------------------
    # Decision 4B: Capture the prototype siege walker
    # --------------------------------------------------------
    "capture_siege_walker": {
        "Voidrunner": [
            "You climb the moving walker and reach the command hatch before it completes its first firing cycle.",
            "The machine is captured while still trying to understand how you boarded it."
        ],
        "Grimshield": [
            "You endure the walker's opening barrage and force your way beneath its guns.",
            "The machine's size means nothing once you reach the hull."
        ],
        "Ashreaver": [
            "You destroy every external weapon without rupturing the core.",
            "The walker survives only because the objective demands it."
        ],
        "Nightreaper": [
            "You enter through a maintenance seam beneath the rear plating.",
            "The crew is gone before the machine realizes it has been breached."
        ],
        "Umbracaster": [
            "You flood the walker's command system with false terrain and phantom targets.",
            "It kneels to engage enemies that do not exist."
        ],
        "Ritesmith": [
            "You bypass the command lock and rewrite the movement controls.",
            "The siege walker becomes yours because machines ultimately answer to structure."
        ],
        "Oathkeeper": [
            "You keep the boarding team alive through the machine's defensive countermeasures.",
            "The walker is taken without leaving anyone behind inside it."
        ],
        "Fluxhunter": [
            "You disable the walker's optic clusters and leg actuators in sequence.",
            "The machine falls intact exactly where the capture team needs it."
        ],
        "Fumebinder": [
            "Smoke blinds the walker while false heat signatures surround it.",
            "The machine fires at decoys until the boarding team is already inside."
        ],
        "Emberbrand": [
            "You burn through the access plating with controlled flame.",
            "The walker emerges from the smoke bearing the marks of its capture."
        ],
    },
}


# ============================================================
# Shared Helpers
# ============================================================

def class_response(player, response_key):
    """Print the selected class response for the current branch."""
    class_name = player.class_name
    response_group = CLASS_RESPONSES.get(response_key, {})
    lines = response_group.get(
        class_name,
        [
            "You steady yourself and continue with the squad.",
            "The Black Furnace will not silence itself."
        ],
    )

    for line in lines:
        narrate(line)


def get_choice(prompt, options):
    """Display a validated numbered menu and return the selected option."""
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


# ============================================================
# Mission Entry Point
# ============================================================

def start_mission_04(player, state):
    mission_briefing(player, state)
    decision_one(player, state)


# ============================================================
# Mission Briefing
# ============================================================

def mission_briefing(player, state):
    title_card(
        MISSION_NAME,
        MISSION_FRONT
    )

    computer(f"[PLANET] {MISSION_PLANET}", delay=0.7)
    computer("[THREAT] AUTOMATON HEAVY INDUSTRIAL COMPLEX", delay=0.7)
    computer("[PRIMARY] DESTROY THE BLACK FURNACE", delay=0.7)
    computer("[SECONDARY] RESTORE ORBITAL ACCESS", delay=0.7)
    computer("[WARNING] PROTOTYPE SIEGE WALKER DETECTED", delay=1)

    blank()

    radio("[COMMAND CHANNEL]", delay=0.5)

    npc(
        "Tiberius",
        "The command network on Varylia Prime is broken."
    )
    npc(
        "Tiberius",
        "Now we strike the industry that supplied it."
    )

    blank()

    narrate(
        "Mordren's Wake is an ash-covered refinery world built around a "
        "single geothermal manufacturing complex."
    )
    narrate(
        "The Automatons call it nothing. Our intelligence has given it a name."
    )

    blank()

    npc("Tiberius", "The Black Furnace.")
    npc(
        "Tiberius",
        "It produces armor, artillery, and siege walkers faster than the front can destroy them."
    )

    blank()

    npc("Tiberius", f"{player.callsign}, shut it down.")
    npc("Tiberius", "Whether it burns or belongs to us afterward is your decision.")

    blank()

    computer(">> DROP VECTOR LOCKED", delay=0.6)
    computer(">> ASH STORM INTERFERENCE DETECTED", delay=0.6)
    computer(">> LOW-ALTITUDE ENTRY AUTHORIZED", delay=0.8)

    blank()

    narrate(
        "The drop pod descends beneath an ash storm thick enough to hide the stars."
    )
    narrate(
        "It impacts near a ruined mag-rail junction overlooking the industrial basin."
    )
    narrate(
        "Beyond the ridge, the Black Furnace glows beneath the planet like an open wound."
    )


# ============================================================
# Decision Point 1
# Choose the initial route into the industrial basin.
# ============================================================

def decision_one(player, state):
    choice = get_choice(
        "Two routes lead toward the Black Furnace.",
        [
            "Cross the exposed ash fields.",
            "Infiltrate through the abandoned mag-rail tunnel.",
        ],
    )

    if choice == 1:
        cross_ash_fields(player, state)
    else:
        infiltrate_mag_rail_tunnel(player, state)


def cross_ash_fields(player, state):
    blank()

    title_card(
        "APPROACH",
        "ASH FIELDS"
    )

    narrate(
        "The ash fields stretch across open ground beneath artillery towers."
    )
    narrate(
        "Every gust exposes buried machines, shattered armor, and the remains of earlier assaults."
    )

    blank()

    class_response(player, "ash_fields")

    blank()

    narrate(
        "The squad reaches the far ridge under intermittent bombardment."
    )
    narrate(
        "From there, you identify two ways to restore orbital support: "
        "destroy the anti-air nexus or reactivate a damaged SEAF beacon."
    )

    decision_two(player, state)


def infiltrate_mag_rail_tunnel(player, state):
    blank()

    title_card(
        "APPROACH",
        "MAG-RAIL TUNNEL"
    )

    narrate(
        "The tunnel descends beneath the ash fields through a line of dead transport stations."
    )
    narrate(
        "Emergency lights flash red along rails still carrying dangerous current."
    )

    blank()

    class_response(player, "mag_rail_tunnel")

    blank()

    narrate(
        "At the final junction, the tunnel splits beneath an anti-air nexus "
        "and a damaged SEAF orbital beacon."
    )
    narrate(
        "Either target could reopen the sky, but there is time to secure only one."
    )

    decision_two(player, state)


# ============================================================
# Decision Point 2
# Restore access to orbital support.
# ============================================================

def decision_two(player, state):
    choice = get_choice(
        "The fleet cannot support the assault while the basin remains isolated.",
        [
            "Destroy the Automaton anti-air nexus.",
            "Reactivate the SEAF orbital beacon.",
        ],
    )

    if choice == 1:
        destroy_anti_air_nexus(player, state)
    else:
        reactivate_orbital_beacon(player, state)


def destroy_anti_air_nexus(player, state):
    blank()

    title_card(
        "SECONDARY OBJECTIVE",
        "DESTROY ANTI-AIR NEXUS"
    )

    narrate(
        "The nexus occupies a fortified plateau above the refinery."
    )
    narrate(
        "Multiple batteries rotate toward the sky while ground defenses guard the command mast."
    )

    blank()

    class_response(player, "destroy_aa_nexus")

    blank()

    say("DETONATE", delay=0.8)

    blank()

    narrate(
        "The command mast folds into the nearest ammunition tower."
    )
    narrate(
        "A chain of explosions rolls across the plateau until every battery falls silent."
    )

    computer(">> ANTI-AIR NEXUS DESTROYED", delay=0.6)
    computer(">> ORBITAL SUPPORT WINDOW OPEN", delay=0.8)

    blank()

    radio("[FLEET CHANNEL]", delay=0.5)
    npc("Fleet Control", "Airspace opening. Limited support is available.")

    blank()

    narrate(
        "Reconnaissance identifies two vulnerabilities deeper in the basin: "
        "the geothermal extractor network and an armored supply convoy."
    )

    decision_three(player, state)


def reactivate_orbital_beacon(player, state):
    blank()

    title_card(
        "SECONDARY OBJECTIVE",
        "REACTIVATE ORBITAL BEACON"
    )

    narrate(
        "The beacon station is half-buried beneath ash and collapsed plating."
    )
    narrate(
        "A wounded SEAF relay operator still guards the manual activation codes."
    )

    blank()

    class_response(player, "reactivate_beacon")

    blank()

    computer(">> RELAY POWER RESTORED", delay=0.6)
    computer(">> ORBITAL BEACON ONLINE", delay=0.8)
    computer(">> FLEET LINK ESTABLISHED", delay=0.8)

    blank()

    radio("[FLEET CHANNEL]", delay=0.5)
    npc("Fleet Control", "Beacon received. Support window confirmed.")

    blank()

    narrate(
        "Orbital scans reveal two opportunities before the final assault: "
        "sabotage the geothermal extractors or seize an armored supply convoy."
    )

    decision_three(player, state)


# ============================================================
# Decision Point 3
# Weaken the Furnace before entering the main complex.
# ============================================================

def decision_three(player, state):
    choice = get_choice(
        "The Black Furnace depends on both geothermal power and constant supply shipments.",
        [
            "Sabotage the geothermal extractor network.",
            "Seize the armored supply convoy.",
        ],
    )

    if choice == 1:
        sabotage_geothermal_extractors(player, state)
    else:
        seize_armored_convoy(player, state)


def sabotage_geothermal_extractors(player, state):
    blank()

    title_card(
        "INDUSTRIAL BASIN",
        "GEOTHERMAL EXTRACTORS"
    )

    narrate(
        "The extractor platforms hang above channels of exposed magma."
    )
    narrate(
        "Pipelines feed heat and pressure directly into the Black Furnace."
    )

    blank()

    class_response(player, "sabotage_extractors")

    blank()

    computer(">> PRESSURE GOVERNORS COMPROMISED", delay=0.6)
    computer(">> EXTRACTION NETWORK CASCADE FAILURE", delay=0.8)

    blank()

    narrate(
        "The platforms rupture in sequence."
    )
    narrate(
        "The Furnace loses power across multiple production lines, forcing its defenders "
        "to abandon outer positions."
    )

    decision_four(player, state)


def seize_armored_convoy(player, state):
    blank()

    title_card(
        "INDUSTRIAL BASIN",
        "ARMORED SUPPLY CONVOY"
    )

    narrate(
        "The convoy moves toward the Furnace beneath heavy escort."
    )
    narrate(
        "Its cargo includes ammunition, reactor components, and siege-walker control modules."
    )

    blank()

    class_response(player, "seize_convoy")

    blank()

    computer(">> LEAD TRANSPORT CAPTURED", delay=0.6)
    computer(">> CONVOY COMMAND OVERRIDDEN", delay=0.8)

    blank()

    narrate(
        "The captured vehicles continue toward the Furnace under false Automaton identification."
    )
    narrate(
        "Your squad enters the final perimeter inside the enemy's own supply line."
    )

    decision_four(player, state)


# ============================================================
# Decision Point 4
# Decide whether to destroy the Furnace or capture its walker.
# ============================================================

def decision_four(player, state):
    blank()

    narrate(
        "The Black Furnace rises around a geothermal core suspended beneath the refinery."
    )
    narrate(
        "Assembly lines move through every level, producing armor and weapons without pause."
    )

    blank()

    narrate(
        "At the center of the complex stands a prototype siege walker larger than any field unit."
    )
    narrate(
        "Its reactor is linked directly to the Furnace's containment system."
    )

    choice = get_choice(
        "The operation can end in one of two ways.",
        [
            "Overload the Black Furnace and destroy the entire complex.",
            "Capture the prototype siege walker and disable the Furnace intact.",
        ],
    )

    if choice == 1:
        overload_black_furnace(player, state)
    else:
        capture_prototype_siege_walker(player, state)


def overload_black_furnace(player, state):
    blank()

    title_card(
        "FINAL OBJECTIVE",
        "BURN THE BLACK FURNACE"
    )

    narrate(
        "The squad fights toward the containment controls while the complex enters lockdown."
    )
    narrate(
        "The geothermal core rises in temperature with every disabled safety system."
    )

    blank()

    class_response(player, "overload_furnace")

    blank()

    computer(">> PRIMARY COOLANT OFFLINE", delay=0.5)
    computer(">> SECONDARY CONTAINMENT DISABLED", delay=0.5)
    computer(">> CORE PRESSURE CRITICAL", delay=0.7)
    computer(">> EVACUATE IMMEDIATELY", delay=0.8)

    blank()

    narrate(
        "The Furnace begins collapsing inward as molten metal floods the production levels."
    )
    narrate(
        "The prototype walker disappears beneath the reactor chamber."
    )

    computer("[PRIMARY OBJECTIVE COMPLETE] BLACK FURNACE DESTROYED", delay=0.8)

    mission_extraction(player, state, outcome="destroyed")


def capture_prototype_siege_walker(player, state):
    blank()

    title_card(
        "FINAL OBJECTIVE",
        "TAKE THE TITAN"
    )

    narrate(
        "The prototype siege walker activates as the squad enters the assembly chamber."
    )
    narrate(
        "Its weapons lock onto the production floor while the Furnace continues feeding it power."
    )

    blank()

    class_response(player, "capture_siege_walker")

    blank()

    computer(">> WALKER OPTICS DISABLED", delay=0.5)
    computer(">> MOVEMENT CONTROL OVERRIDDEN", delay=0.5)
    computer(">> COMMAND LINK REWRITTEN", delay=0.7)
    computer(">> PROTOTYPE CONTROL CONFIRMED", delay=0.8)

    blank()

    narrate(
        "The siege walker turns away from your squad and fires into the Furnace's defense grid."
    )
    narrate(
        "Under its own stolen guns, the complex powers down sector by sector."
    )

    computer("[PRIMARY OBJECTIVE COMPLETE] PROTOTYPE WALKER CAPTURED", delay=0.8)
    computer("[STATUS] BLACK FURNACE DISABLED INTACT", delay=0.8)

    mission_extraction(player, state, outcome="captured")


# ============================================================
# Extraction and Mission End
# ============================================================

def mission_extraction(player, outcome):
    blank()

    radio("[EXTRACTION CHANNEL]", delay=0.5)

    if outcome == "destroyed":
        npc("Pelican Pilot", "The whole refinery is going critical.")
        npc("Pelican Pilot", "Move now unless you plan to become part of the geology.")
    else:
        npc("Pelican Pilot", "I see the walker.")
        npc("Pelican Pilot", "I am choosing not to ask how you intend to bring that home.")

    blank()

    narrate(
        "The squad crosses the final platform beneath collapsing gantries and burning machinery."
    )
    narrate(
        "Automaton defenders continue firing even as the industrial complex fails around them."
    )

    blank()

    if outcome == "destroyed":
        narrate(
            "The Pelican lifts away moments before the geothermal core breaches."
        )
        narrate(
            "The Black Furnace erupts beneath the ash storm, turning night into white fire."
        )
    else:
        narrate(
            "The captured siege walker marches toward the extraction perimeter beneath fleet escort."
        )
        narrate(
            "Behind it, the Black Furnace stands silent for the first time since the occupation began."
        )

    blank()

    computer(">> EXTRACTION CONFIRMED", delay=0.8)
    computer(f">> OPERATIVE VERIFIED: {player.callsign.upper()}", delay=0.8)

    blank()

    if outcome == "destroyed":
        npc(
            "Tiberius",
            "The machines have lost one of their greatest forges."
        )
        npc(
            "Tiberius",
            "The front will feel the absence."
        )
    else:
        npc(
            "Tiberius",
            "A captured siege walker is more than a weapon."
        )
        npc(
            "Tiberius",
            "It is proof that even their largest machines can be made to kneel."
        )

    blank()

    title_card(
        "MISSION COMPLETE",
        MISSION_NAME
    )

    computer("[STATUS] BLACK FURNACE NEUTRALIZED", delay=0.6)
    computer("[STATUS] AUTOMATON PRODUCTION CRIPPLED", delay=0.6)
    computer("[STATUS] OPERATIVE RETURNING TO THE SPEAR OF TARTARUS", delay=1)

    blank()

    npc("Atreides", "Efficient.")
    npc("Atreides", "I approve.")

    blank()

    npc("Spooky", "I would have used more explosives.")

    blank()

    npc("Valinor", "I would have used more fire.")

    blank()

    npc("Atreides", "For once, both of your suggestions were already included.")

    blank()

    npc("Brexor", "The Spear of Tartarus personally inspired this victory.")

    blank()

    npc("Unknown Crew Member", "The ship did not enter the atmosphere.")

    blank()

    npc("Brexor", "Leadership can be indirect.")

    blank()

    narrate(
        "Mordren's Wake disappears beneath the ash clouds."
    )
    narrate(
        "The Automaton front still stretches across countless worlds."
    )
    narrate(
        "But one of its great forges has gone dark."
    )

    blank()


# ============================================================
# Local Test Runner
#
# Run from the project root with:
#     py story\mission_04_automatons.py
# ============================================================

if __name__ == "__main__":
    from core.player import Player

    test_player = Player()
    test_player.create_character()

    start_mission_04(test_player)

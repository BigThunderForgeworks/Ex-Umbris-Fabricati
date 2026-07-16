"""
story/mission_03_automatons.py

Mission 03 for Ex Umbris Fabricati.

Operation: IRON ECHO
Front: Automaton
Purpose:
- Begins the Automaton campaign
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


# ============================================================
# Mission Configuration
# ============================================================

MISSION_NAME = "OPERATION IRON ECHO"
MISSION_FRONT = "AUTOMATON FRONT"
MISSION_PLANET = "VARYLIA PRIME"


# ============================================================
# Class-Specific Responses
# ============================================================

CLASS_RESPONSES = {
    # --------------------------------------------------------
    # Decision 1A: Infiltrate the communications trench
    # --------------------------------------------------------
    "communications_trench": {
        "Voidrunner": [
            "You vanish into the trench before the sentry sweep completes.",
            "Every collapsed conduit becomes a route deeper into the machine line."
        ],
        "Grimshield": [
            "You enter first and absorb the opening burst from a hidden turret.",
            "The squad advances behind the certainty of your armor."
        ],
        "Ashreaver": [
            "The trench is narrow, crowded, and full of targets.",
            "You answer the red glow ahead with disciplined destruction."
        ],
        "Nightreaper": [
            "The trench lights flicker as you pass beneath them.",
            "Automaton sentries disappear one by one without raising an alarm."
        ],
        "Umbracaster": [
            "Signal interference rolls through the trench in repeating waves.",
            "You begin turning the machines' own confusion against them."
        ],
        "Ritesmith": [
            "You identify the trench's power spine immediately.",
            "One severed junction could blind half the defensive grid."
        ],
        "Oathkeeper": [
            "You keep the squad close and check every wound before moving on.",
            "The trench offers no room for a fallen Helldiver to be left behind."
        ],
        "Fluxhunter": [
            "Every red optic becomes a measured point in the darkness.",
            "You fire only when the shot matters."
        ],
        "Fumebinder": [
            "Smoke settles low between the trench walls.",
            "The Automatons lose sight of your squad while you retain control of every angle."
        ],
        "Emberbrand": [
            "Sparks rain from ruptured cables around you.",
            "The trench feels less like a battlefield and more like a forge waiting to awaken."
        ],
    },

    # --------------------------------------------------------
    # Decision 1B: Assault the forward gun line
    # --------------------------------------------------------
    "forward_gun_line": {
        "Voidrunner": [
            "You sprint between artillery impacts while the guns traverse too slowly to follow.",
            "Their greatest strength becomes dead weight against your speed."
        ],
        "Grimshield": [
            "You advance beneath direct fire, each impact hammering against your armor.",
            "The gun line breaks because you refuse to."
        ],
        "Ashreaver": [
            "You meet the emplacements with overwhelming force.",
            "Steel fragments scatter across the battlefield like shrapnel from a broken altar."
        ],
        "Nightreaper": [
            "You move through blind sectors between rotating batteries.",
            "The first crew notices you only after the second gun falls silent."
        ],
        "Umbracaster": [
            "You flood their targeting systems with false signatures.",
            "The batteries fire at ghosts while the squad closes the distance."
        ],
        "Ritesmith": [
            "You identify the support braces and ammunition feeds.",
            "The strongest weapon is still only a machine assembled from vulnerable parts."
        ],
        "Oathkeeper": [
            "You move from one wounded diver to the next without breaking stride.",
            "The gun line does not receive the casualties it expected."
        ],
        "Fluxhunter": [
            "You target optics, loaders, and exposed power cells.",
            "The line collapses one precise failure at a time."
        ],
        "Fumebinder": [
            "A wall of smoke rolls across the approach.",
            "The artillery fires blindly into empty ground."
        ],
        "Emberbrand": [
            "You push through the barrage with fire at your back.",
            "By the time the guns realize you have reached them, the line is already burning."
        ],
    },

    # --------------------------------------------------------
    # Decision 2A: Disable the jammer array
    # --------------------------------------------------------
    "disable_jammer": {
        "Voidrunner": [
            "You climb the jammer tower faster than its defenses can reposition.",
            "The array dies before the lower patrols understand the threat came from above."
        ],
        "Grimshield": [
            "You hold the base of the tower while the squad breaches the controls.",
            "Every Automaton assault crashes against you and loses momentum."
        ],
        "Ashreaver": [
            "You tear into the jammer's cooling system.",
            "The machine overheats in a storm of sparks and molten plating."
        ],
        "Nightreaper": [
            "You pass through the service access without tripping a single sensor.",
            "The tower loses power in perfect silence."
        ],
        "Umbracaster": [
            "You feed contradictory commands into the jammer's network.",
            "The machine begins suppressing its own signals."
        ],
        "Ritesmith": [
            "You open the core housing and reroute the power flow by hand.",
            "The jammer becomes a beacon for your own fleet."
        ],
        "Oathkeeper": [
            "You stabilize the wounded technician long enough to finish the shutdown.",
            "The array falls because one more person remained alive to complete the work."
        ],
        "Fluxhunter": [
            "You fire into the exposed signal regulator.",
            "One shot ends the interference across the entire valley."
        ],
        "Fumebinder": [
            "Smoke fills the lower access chambers.",
            "The defenders search room by room while you disable the array above them."
        ],
        "Emberbrand": [
            "The jammer core glows white beneath sustained heat.",
            "Its final transmission ends in fire."
        ],
    },

    # --------------------------------------------------------
    # Decision 2B: Recover the downed intelligence drone
    # --------------------------------------------------------
    "recover_drone": {
        "Voidrunner": [
            "You reach the crash site before the Automaton salvage team.",
            "The drone is in your hands while the enemy is still searching the wrong ridge."
        ],
        "Grimshield": [
            "You shield the drone while data extraction begins.",
            "The enemy can destroy neither the machine nor the people working beside it."
        ],
        "Ashreaver": [
            "You reduce the salvage team to scattered metal.",
            "The drone survives because nothing hostile remains close enough to touch it."
        ],
        "Nightreaper": [
            "You remove the patrol guarding the wreck without alerting the larger force.",
            "The intelligence leaves the battlefield unseen."
        ],
        "Umbracaster": [
            "You isolate the drone from hostile network pings.",
            "For the first time since it fell, the machine is truly silent."
        ],
        "Ritesmith": [
            "You rebuild the damaged memory port from spare components.",
            "The drone gives up its secrets because you refuse to accept broken as final."
        ],
        "Oathkeeper": [
            "You pull the injured scout from beneath the wreckage before touching the data core.",
            "Information matters, but not before life."
        ],
        "Fluxhunter": [
            "You neutralize the patrol leaders before the salvage team can organize.",
            "Their recovery operation ends before it begins."
        ],
        "Fumebinder": [
            "Smoke hides the crash site from aerial scanners.",
            "The drone disappears from the Automaton network as if swallowed by the planet."
        ],
        "Emberbrand": [
            "You cut through the fused hull with controlled flame.",
            "The data core emerges glowing but intact."
        ],
    },

    # --------------------------------------------------------
    # Decision 3A: Sabotage the walker foundry
    # --------------------------------------------------------
    "sabotage_foundry": {
        "Voidrunner": [
            "You race along overhead gantries while unfinished walkers turn beneath you.",
            "Charges appear on the assembly line faster than the machines can track."
        ],
        "Grimshield": [
            "You hold the main corridor while demolition teams work.",
            "The foundry sends everything it has, and still the line remains closed."
        ],
        "Ashreaver": [
            "You turn the production floor into ruin.",
            "Machines built for war die before ever reaching the battlefield."
        ],
        "Nightreaper": [
            "You pass beneath hanging chassis and strike at the control nodes.",
            "The foundry goes dark without understanding it has been infiltrated."
        ],
        "Umbracaster": [
            "You corrupt the assembly instructions.",
            "Half-built walkers begin attacking one another before the charges even detonate."
        ],
        "Ritesmith": [
            "You reverse the foundry's power regulators.",
            "The machines consume themselves in the act of trying to continue production."
        ],
        "Oathkeeper": [
            "You keep the demolition team alive through every counterattack.",
            "The foundry falls because no specialist is lost before the work is done."
        ],
        "Fluxhunter": [
            "You target control relays across the production line.",
            "One precise cascade shuts down an army before it is born."
        ],
        "Fumebinder": [
            "Smoke fills the assembly floor and blinds the automated defenses.",
            "The machines fire into shadows while the foundry is dismantled around them."
        ],
        "Emberbrand": [
            "Flame races along oil lines and ammunition belts.",
            "The foundry becomes a furnace worthy of your name."
        ],
    },

    # --------------------------------------------------------
    # Decision 3B: Free the captured SEAF prisoners
    # --------------------------------------------------------
    "free_prisoners": {
        "Voidrunner": [
            "You slip through the detention grid and open the cells from inside.",
            "The prisoners see freedom before the guards see you."
        ],
        "Grimshield": [
            "You stand in the doorway while the prisoners evacuate.",
            "No Automaton crosses that threshold."
        ],
        "Ashreaver": [
            "You tear through the guard detail with merciless force.",
            "The prisoners leave behind nothing capable of pursuing them."
        ],
        "Nightreaper": [
            "You silence the watch towers before the first cell opens.",
            "The entire rescue unfolds beneath the enemy's notice."
        ],
        "Umbracaster": [
            "You falsify the prison alarms and redirect patrols away.",
            "The compound reports that all captives remain secure while the cells stand empty."
        ],
        "Ritesmith": [
            "You bypass the magnetic locks and disable the restraint field.",
            "The prison was built to resist force, not understanding."
        ],
        "Oathkeeper": [
            "You treat the weakest prisoners before the escape begins.",
            "No one is left behind simply because they cannot run."
        ],
        "Fluxhunter": [
            "You remove each tower gunner before the prisoners cross open ground.",
            "The escape route remains clear because your aim does not fail."
        ],
        "Fumebinder": [
            "A thick smoke screen separates the cells from the outer wall.",
            "The prisoners vanish into cover before the alarm can become useful."
        ],
        "Emberbrand": [
            "You burn through the final barricade and lead the captives into the open.",
            "Freedom arrives with heat, light, and the collapse of steel."
        ],
    },

    # --------------------------------------------------------
    # Decision 4A: Destroy the command bunker
    # --------------------------------------------------------
    "destroy_bunker": {
        "Voidrunner": [
            "You outrun the bunker doors as they begin to seal.",
            "The command core falls before the defenses can lock you out."
        ],
        "Grimshield": [
            "You hold the breach against wave after wave of defenders.",
            "The bunker dies behind you because you refuse to yield the doorway."
        ],
        "Ashreaver": [
            "You carry destruction into the heart of the command center.",
            "The bunker becomes a tomb of scorched steel."
        ],
        "Nightreaper": [
            "You reach the command core through maintenance passages no soldier was meant to use.",
            "The machines never see the strike that ends their coordination."
        ],
        "Umbracaster": [
            "You overload their tactical network with false orders.",
            "The bunker collapses into chaos before the final charge explodes."
        ],
        "Ritesmith": [
            "You set the reactor to consume its own containment field.",
            "The bunker destroys itself according to your design."
        ],
        "Oathkeeper": [
            "You keep every member of the assault team moving.",
            "No one falls in the final corridor while you still have a stim remaining."
        ],
        "Fluxhunter": [
            "You fire through the core's exposed regulator.",
            "The entire command network dies from one perfectly chosen shot."
        ],
        "Fumebinder": [
            "Smoke swallows the command floor.",
            "The officers fire at empty silhouettes while your squad reaches the core."
        ],
        "Emberbrand": [
            "The reactor chamber blooms with flame.",
            "The bunker ends as a furnace beneath the earth."
        ],
    },

    # --------------------------------------------------------
    # Decision 4B: Capture the command core
    # --------------------------------------------------------
    "capture_core": {
        "Voidrunner": [
            "You reach the extraction point with the core while the bunker still believes it is secure.",
            "By the time the alarm spreads, the prize is already gone."
        ],
        "Grimshield": [
            "You carry the core through incoming fire like a shielded relic.",
            "Nothing touches it while you remain standing."
        ],
        "Ashreaver": [
            "You eliminate every defender between the core and the exit.",
            "The machine survives because everything around it does not."
        ],
        "Nightreaper": [
            "You disable the command staff before they can erase the data.",
            "The core leaves the bunker with its secrets intact."
        ],
        "Umbracaster": [
            "You convince the command network it is still operating normally.",
            "The core continues transmitting while being carried away."
        ],
        "Ritesmith": [
            "You detach the core without triggering its failsafe.",
            "A machine designed never to be captured becomes portable in your hands."
        ],
        "Oathkeeper": [
            "You balance the weight of the core with the need to protect the wounded.",
            "The squad returns with both intelligence and every living member."
        ],
        "Fluxhunter": [
            "You remove each defender who approaches the extraction route.",
            "The core crosses open ground under a corridor of perfect shots."
        ],
        "Fumebinder": [
            "Smoke hides the extraction convoy from every targeting optic.",
            "The command core disappears behind a wall of controlled confusion."
        ],
        "Emberbrand": [
            "You burn through the containment clamps without damaging the core.",
            "The machine leaves its bunker glowing from your touch."
        ],
    },
}


# ============================================================
# Shared Helpers
# ============================================================

def class_response(player, response_key):
    """Print the selected class response for the current scene."""
    class_name = player.class_name
    response_group = CLASS_RESPONSES.get(response_key, {})
    lines = response_group.get(
        class_name,
        [
            "You steady yourself and continue with the squad.",
            "The Automaton line will not break itself."
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

def start_mission_03(player, state):
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
    computer("[THREAT] AUTOMATON OCCUPATION FORCE", delay=0.7)
    computer("[PRIMARY] DISRUPT REGIONAL COMMAND NETWORK", delay=0.7)
    computer("[SECONDARY] RECOVER SEAF INTELLIGENCE", delay=0.7)
    computer("[WARNING] ORBITAL SUPPORT JAMMED", delay=1)

    blank()

    radio("[COMMAND CHANNEL]", delay=0.5)

    npc(
        "Tiberius",
        "The Terminid front is quieter, but the war does not wait for reflection."
    )
    npc(
        "Tiberius",
        "Varylia Prime has gone silent beneath an Automaton communications net."
    )

    blank()

    narrate(
        "The machines have fortified the planet around a command bunker "
        "buried beneath an industrial basin."
    )
    narrate(
        "Every artillery battery, patrol, and walker in the region receives "
        "orders from that network."
    )

    blank()

    npc("Tiberius", f"{player.callsign}, break their signal.")
    npc("Tiberius", "Remind the machines that coordination is not the same as unity.")

    blank()

    computer(">> DROP VECTOR LOCKED", delay=0.6)
    computer(">> AUTOMATON AIR DEFENSE DETECTED", delay=0.6)
    computer(">> EVASIVE ENTRY PROFILE ACTIVE", delay=0.8)

    blank()

    narrate(
        "The drop pod tears through red tracer fire and impacts behind a "
        "ridge of shattered fortifications."
    )
    narrate(
        "When the hatch opens, the horizon glows with factories, searchlights, "
        "and the cold red eyes of the Automaton occupation."
    )


# ============================================================
# Decision Point 1
# Choose the opening approach toward the command network.
# ============================================================

def decision_one(player, state):
    choice = get_choice(
        "Two routes lead toward the regional command network.",
        [
            "Infiltrate the communications trench.",
            "Assault the forward gun line.",
        ],
    )

    if choice == 1:
        infiltrate_communications_trench(player, state)
    else:
        assault_forward_gun_line(player, state)


def infiltrate_communications_trench(player, state):
    blank()

    title_card(
        "APPROACH",
        "COMMUNICATIONS TRENCH"
    )

    narrate(
        "The trench cuts through the basin beneath layers of cables and armored plating."
    )
    narrate(
        "Red searchlights sweep overhead while patrols march through the narrow passage."
    )

    blank()

    class_response(player, state, "communications_trench")

    blank()

    narrate(
        "The squad reaches the trench relay and extracts a partial command map."
    )
    narrate(
        "It reveals both a jammer array and the crash site of a missing SEAF intelligence drone."
    )

    decision_two(player, state)


def assault_forward_gun_line(player, state):
    blank()

    title_card(
        "APPROACH",
        "FORWARD GUN LINE"
    )

    narrate(
        "Heavy emplacements overlook the industrial basin."
    )
    narrate(
        "The batteries begin firing the moment your squad crosses the ridge."
    )

    blank()

    class_response(player, state, "forward_gun_line")

    blank()

    narrate(
        "The final emplacement collapses beneath coordinated fire."
    )
    narrate(
        "Its targeting records identify a jammer array and a recently downed "
        "SEAF intelligence drone."
    )

    decision_two(player, state)


# ============================================================
# Decision Point 2
# Choose between restoring support or recovering intelligence.
# ============================================================

def decision_two(player, state):
    choice = get_choice(
        "The regional command bunker remains protected by both signal interference and patrol intelligence.",
        [
            "Disable the Automaton jammer array.",
            "Recover the downed SEAF intelligence drone.",
        ],
    )

    if choice == 1:
        disable_jammer_array(player, state)
    else:
        recover_intelligence_drone(player, state)


def disable_jammer_array(player, state):
    blank()

    title_card(
        "SECONDARY OBJECTIVE",
        "DISABLE JAMMER ARRAY"
    )

    narrate(
        "The jammer tower rises above the basin, surrounded by automated guns "
        "and rotating searchlights."
    )
    narrate(
        "Its signal turns every orbital request into static."
    )

    blank()

    class_response(player, state, "disable_jammer")

    blank()

    computer(">> JAMMER POWER CORE OFFLINE", delay=0.6)
    computer(">> ORBITAL LINK RESTORED", delay=0.8)

    blank()

    radio("[ORBITAL CHANNEL]", delay=0.5)
    npc("Fleet Control", "Signal restored. Support assets are standing by.")

    blank()

    narrate(
        "The tower's archived network traffic identifies an active walker foundry "
        "and a nearby SEAF detention compound."
    )

    decision_three(player, state)


def recover_intelligence_drone(player, state):
    blank()

    title_card(
        "SECONDARY OBJECTIVE",
        "RECOVER INTELLIGENCE DRONE"
    )

    narrate(
        "The drone lies broken in a crater beneath the remains of its escort."
    )
    narrate(
        "An Automaton salvage team is already cutting into the hull."
    )

    blank()

    class_response(player, state, "recover_drone")

    blank()

    computer(">> MEMORY CORE CONNECTED", delay=0.6)
    computer(">> ENCRYPTED DATA RECOVERED", delay=0.8)

    blank()

    narrate(
        "The drone's final reconnaissance pass identified an active walker foundry "
        "and a SEAF detention compound operating beneath the same defensive grid."
    )

    decision_three(player, state)


# ============================================================
# Decision Point 3
# Choose between weakening enemy production or rescuing captives.
# ============================================================

def decision_three(player, state):
    choice = get_choice(
        "The route to the command bunker passes two critical locations.",
        [
            "Sabotage the Automaton walker foundry.",
            "Free the captured SEAF prisoners.",
        ],
    )

    if choice == 1:
        sabotage_walker_foundry(player, state)
    else:
        free_seaf_prisoners(player, state)


def sabotage_walker_foundry(player, state):
    blank()

    title_card(
        "INDUSTRIAL BASIN",
        "WALKER FOUNDRY"
    )

    narrate(
        "The foundry floor is lined with unfinished walkers suspended from cranes."
    )
    narrate(
        "Assembly arms continue working while armed machines converge on your position."
    )

    blank()

    class_response(player, state, "sabotage_foundry")

    blank()

    computer(">> PRODUCTION CONTROL CORRUPTED", delay=0.6)
    computer(">> REACTOR OVERLOAD INITIATED", delay=0.8)

    blank()

    narrate(
        "The foundry tears itself apart in a chain of explosions."
    )
    narrate(
        "The command bunker loses an entire wave of reinforcements before they can deploy."
    )

    decision_four(player, state)


def free_seaf_prisoners(player, state):
    blank()

    title_card(
        "INDUSTRIAL BASIN",
        "SEAF DETENTION COMPOUND"
    )

    narrate(
        "Rows of magnetic cells stand beneath watch towers and automated guns."
    )
    narrate(
        "The prisoners look up as the first alarm begins to sound."
    )

    blank()

    class_response(player, state, "free_prisoners")

    blank()

    computer(">> DETENTION GRID OFFLINE", delay=0.6)
    computer(">> PRISONER EXTRACTION ROUTE OPEN", delay=0.8)

    blank()

    npc("SEAF Captain", "We thought the fleet had abandoned this sector.")
    npc("SEAF Captain", "Show us where to fight.")

    blank()

    narrate(
        "The freed prisoners arm themselves and begin disrupting patrols across the basin."
    )
    narrate(
        "The command bunker is forced to divide its remaining defenders."
    )

    decision_four(player, state)


# ============================================================
# Decision Point 4
# Decide whether to destroy or capture the command core.
# ============================================================

def decision_four(player, state):
    blank()

    narrate(
        "The command bunker lies beneath a fortress of black steel."
    )
    narrate(
        "Inside, the regional command core coordinates every Automaton unit "
        "within hundreds of kilometers."
    )

    choice = get_choice(
        "The Iron Echo ends at the command core.",
        [
            "Destroy the command bunker and sever the network.",
            "Capture the command core for Sanctum intelligence.",
        ],
    )

    if choice == 1:
        destroy_command_bunker(player, state)
    else:
        capture_command_core(player, state)


def destroy_command_bunker(player, state):
    blank()

    title_card(
        "FINAL OBJECTIVE",
        "SILENCE THE IRON ECHO"
    )

    narrate(
        "The squad breaches the bunker as alarms flood every corridor."
    )
    narrate(
        "The command core seals itself behind layers of armored doors."
    )

    blank()

    class_response(player, state, "destroy_bunker")

    blank()

    say("DETONATE", delay=0.8)

    blank()

    narrate(
        "The reactor overload tears through the bunker from the inside."
    )
    narrate(
        "Across the basin, Automaton formations stagger as their orders vanish."
    )

    computer("[PRIMARY OBJECTIVE COMPLETE] COMMAND NETWORK DESTROYED", delay=0.8)

    mission_extraction(player, state, outcome="destroyed")


def capture_command_core(player, state):
    blank()

    title_card(
        "FINAL OBJECTIVE",
        "TAKE THE IRON MIND"
    )

    narrate(
        "The squad enters the command chamber while the core begins purging its data."
    )
    narrate(
        "Automaton defenders pour into the surrounding corridors."
    )

    blank()

    class_response(player, state, "capture_core")

    blank()

    computer(">> FAILSAFE DISABLED", delay=0.6)
    computer(">> COMMAND CORE DETACHED", delay=0.8)
    computer(">> DATA INTEGRITY CONFIRMED", delay=0.8)

    blank()

    narrate(
        "The command core continues issuing orders as it is carried from the bunker."
    )
    narrate(
        "For several minutes, the machines obey a commander that is no longer theirs."
    )

    computer("[PRIMARY OBJECTIVE COMPLETE] COMMAND CORE CAPTURED", delay=0.8)

    mission_extraction(player, state, outcome="captured")


# ============================================================
# Extraction and Mission End
# ============================================================

def mission_extraction(player, state, outcome):
    blank()

    radio("[EXTRACTION CHANNEL]", delay=0.5)
    npc("Pelican Pilot", "Basin airspace is opening.")
    npc("Pelican Pilot", "Get to the beacon before the machines reorganize.")

    blank()

    narrate(
        "The squad crosses the industrial basin beneath burning searchlights."
    )
    narrate(
        "Automaton formations move without coordination, firing at conflicting targets "
        "as the command network fails."
    )

    blank()

    narrate(
        "The Pelican drops behind a shattered artillery position."
    )
    narrate(
        "Its ramp lowers while tracer fire tears across the landing zone."
    )

    blank()

    npc("Pelican Pilot", "Board now. Admire the explosions from orbit.")

    blank()

    computer(">> EXTRACTION CONFIRMED", delay=0.8)
    computer(f">> OPERATIVE VERIFIED: {player.callsign.upper()}", delay=0.8)

    blank()

    if outcome == "destroyed":
        narrate(
            "The command bunker collapses into a crater of molten steel."
        )
        narrate(
            "Across Varylia Prime, isolated Automaton units continue fighting without direction."
        )
        npc(
            "Tiberius",
            "Their network is broken. Now we learn what the machines do without a voice."
        )

    else:
        narrate(
            "The captured command core pulses inside its containment frame."
        )
        narrate(
            "Even disconnected, it continues attempting to contact units across the planet."
        )
        npc(
            "Tiberius",
            "Bring it to the Spear of Tartarus."
        )
        npc(
            "Tiberius",
            "If the machines possess a language of command, we will learn to read it."
        )

    blank()

    title_card(
        "MISSION COMPLETE",
        MISSION_NAME
    )

    computer("[STATUS] REGIONAL COMMAND NETWORK NEUTRALIZED", delay=0.6)
    computer("[STATUS] AUTOMATON DEFENSE GRID DISRUPTED", delay=0.6)
    computer("[STATUS] OPERATIVE RETURNING TO THE SPEAR OF TARTARUS", delay=1)

    blank()

    npc("Atreides", "I reviewed the combat feed.")
    npc("Atreides", "Acceptable shooting.")

    blank()

    npc("Spooky", "The bunker could have used more explosions.")

    blank()

    npc("Valinor", "And more fire.")

    blank()

    npc("Atreides", "Neither of you are writing the after-action report.")

    blank()

    narrate(
        "Varylia Prime burns beneath the Pelican."
    )
    narrate(
        "The machines are still there."
    )
    narrate(
        "But for the first time, they are no longer moving as one."
    )

    blank()


# ============================================================
# Local Test Runner
# ============================================================

if __name__ == "__main__":
    from core.player import Player

    test_player = Player()
    test_player.create_character()

    start_mission_03(test_player)

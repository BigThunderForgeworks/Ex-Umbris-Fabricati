"""
story/mission_05_illuminate.py

Mission 05 for Ex Umbris Fabricati.

Operation: VEIL OF GLASS
Front: Illuminate
Purpose:
- Introduces the Illuminate ("Squid") front
- Contains four major decision points
- Provides unique class-specific responses for all ten classes
- Ends on an open thread for a future continuation
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

MISSION_NAME = "OPERATION VEIL OF GLASS"
MISSION_FRONT = "ILLUMINATE FRONT"
MISSION_PLANET = "NEREID'S FALL"


# ============================================================
# Class-Specific Responses
# ============================================================

CLASS_RESPONSES = {
    # --------------------------------------------------------
    # Decision 1A: Enter the flooded district
    # --------------------------------------------------------
    "flooded_district": {
        "Voidrunner": [
            "You move across submerged rooftops and broken transit rails.",
            "The drowned streets slow everyone except you."
        ],
        "Grimshield": [
            "You wade into the flooded avenue at the head of the squad.",
            "Whatever waits beneath the water will meet your armor first."
        ],
        "Ashreaver": [
            "Blue light flickers beneath the black water.",
            "You answer the alien glow with the promise of violence."
        ],
        "Nightreaper": [
            "Rain, darkness, and ruined buildings hide your movement.",
            "Even the Illuminate struggle to follow a shadow that never stays still."
        ],
        "Umbracaster": [
            "The district bends sound and light in impossible ways.",
            "You let the distortion guide you instead of resisting it."
        ],
        "Ritesmith": [
            "You test the flooded power grid before each crossing.",
            "Alien current still moves beneath the streets, but patterns can be understood."
        ],
        "Oathkeeper": [
            "You keep the squad linked by sight and signal.",
            "In water this deep, one wounded Helldiver can disappear in seconds."
        ],
        "Fluxhunter": [
            "You watch for ripples that do not belong to the rain.",
            "Every disturbance becomes a warning before the enemy surfaces."
        ],
        "Fumebinder": [
            "Mist gathers across the water at your command.",
            "The district becomes a maze whose exits only you can read."
        ],
        "Emberbrand": [
            "Steam rises where your heat meets the floodwater.",
            "You carry a moving furnace through the drowned city."
        ],
    },

    # --------------------------------------------------------
    # Decision 1B: Scale the crystalline causeway
    # --------------------------------------------------------
    "crystal_causeway": {
        "Voidrunner": [
            "You leap between fractured crystal spans above the city.",
            "The causeway was not built for human feet, but speed makes its own path."
        ],
        "Grimshield": [
            "You cross the exposed causeway without hesitation.",
            "Alien fire strikes around you, and the squad advances in your shadow."
        ],
        "Ashreaver": [
            "Every crystal structure refracts the glow of distant explosions.",
            "You decide the causeway would look better shattered."
        ],
        "Nightreaper": [
            "The reflective surface offers little darkness.",
            "You create your own by moving between each pulse of alien light."
        ],
        "Umbracaster": [
            "The causeway hums with layered signals.",
            "You begin separating illusion from structure."
        ],
        "Ritesmith": [
            "You study the crystalline supports as you move.",
            "The material appears delicate, but its geometry carries impossible loads."
        ],
        "Oathkeeper": [
            "You monitor every footing and every heartbeat.",
            "A fall from the causeway would leave no one to recover."
        ],
        "Fluxhunter": [
            "The height exposes distant observers along the skyline.",
            "You remove them before the squad enters their range."
        ],
        "Fumebinder": [
            "Smoke rolls along the crystal like dark water.",
            "The Illuminate lose their clean sight lines."
        ],
        "Emberbrand": [
            "Your flame reflects a hundred times across the causeway.",
            "For a moment, it looks as though an army of Emberbrands advances with you."
        ],
    },

    # --------------------------------------------------------
    # Decision 2A: Destroy the cognitive beacon
    # --------------------------------------------------------
    "destroy_beacon": {
        "Voidrunner": [
            "You reach the beacon between pulses.",
            "The machine cannot influence a mind that never remains where it expects."
        ],
        "Grimshield": [
            "You stand beneath the beacon's pressure and refuse to kneel.",
            "The squad reaches the core because your will holds."
        ],
        "Ashreaver": [
            "You answer the psychic assault with explosives.",
            "The beacon's song ends in a language you understand."
        ],
        "Nightreaper": [
            "You enter through the maintenance aperture and strike the core.",
            "The beacon dies before its guardians realize it has been breached."
        ],
        "Umbracaster": [
            "You turn the beacon's rhythm against itself.",
            "Its final pulse fractures through its own network."
        ],
        "Ritesmith": [
            "You identify the resonant supports holding the core stable.",
            "Three precise failures are enough to collapse the entire device."
        ],
        "Oathkeeper": [
            "You keep the squad conscious through the beacon's mental pressure.",
            "No one is lost inside their own mind."
        ],
        "Fluxhunter": [
            "You wait for the shielding cycle to open.",
            "One shot reaches the exposed core and ends the signal."
        ],
        "Fumebinder": [
            "Aerosol interference distorts the beacon's targeting field.",
            "Its influence scatters while the squad closes in."
        ],
        "Emberbrand": [
            "The core burns with cold blue light until your flame overtakes it.",
            "The beacon dies beneath warmer fire."
        ],
    },

    # --------------------------------------------------------
    # Decision 2B: Rescue enthralled civilians
    # --------------------------------------------------------
    "rescue_enthralled": {
        "Voidrunner": [
            "You move among the civilians before the overseers react.",
            "Restraints fall open faster than the enemy can restore control."
        ],
        "Grimshield": [
            "You shield the civilians from alien fire during the withdrawal.",
            "Their first free steps are taken behind your armor."
        ],
        "Ashreaver": [
            "You destroy the overseers without turning your weapons toward the enthralled.",
            "For once, precision tempers your fury."
        ],
        "Nightreaper": [
            "The overseers vanish from their posts one by one.",
            "The civilians awaken to find their captors already gone."
        ],
        "Umbracaster": [
            "You disrupt the control pattern long enough for individual minds to return.",
            "The silence breaks into frightened human voices."
        ],
        "Ritesmith": [
            "You adapt a signal repeater into a counter-frequency generator.",
            "The alien restraint fails because you learn how it was built."
        ],
        "Oathkeeper": [
            "You move from person to person, grounding them with voice and touch.",
            "Freedom begins with being reminded that they are still human."
        ],
        "Fluxhunter": [
            "You remove every overseer watching the evacuation lanes.",
            "The civilians cross open ground beneath your protection."
        ],
        "Fumebinder": [
            "Mist hides the freed civilians from the remaining sentries.",
            "They disappear from the control grid before the enemy can reclaim them."
        ],
        "Emberbrand": [
            "You burn through the restraint pylons without harming those bound to them.",
            "The civilians step into the glow of their own freedom."
        ],
    },

    # --------------------------------------------------------
    # Decision 3A: Enter the phase archive
    # --------------------------------------------------------
    "phase_archive": {
        "Voidrunner": [
            "You cross shifting platforms before they fully exist.",
            "Momentum carries you through spaces that refuse to remain still."
        ],
        "Grimshield": [
            "You anchor the squad while gravity changes around the chamber.",
            "When the room moves, everyone has something solid to hold."
        ],
        "Ashreaver": [
            "The archive surrounds itself with elegant defenses.",
            "You respond with inelegant force."
        ],
        "Nightreaper": [
            "You move through moments of darkness between phase shifts.",
            "The archive never sees you occupying the same reality twice."
        ],
        "Umbracaster": [
            "You recognize that the archive is not hidden in space alone.",
            "Its pathways open through attention, memory, and expectation."
        ],
        "Ritesmith": [
            "You map the phase sequence and build a stable route from unstable geometry.",
            "The impossible becomes repeatable."
        ],
        "Oathkeeper": [
            "You keep every squadmate oriented as the chamber shifts.",
            "No one is allowed to vanish alone between phases."
        ],
        "Fluxhunter": [
            "You track the archive's synchronization point.",
            "One precise interruption locks the chamber into a single state."
        ],
        "Fumebinder": [
            "Particles in your smoke reveal air moving through invisible doors.",
            "The archive's hidden passages become visible outlines."
        ],
        "Emberbrand": [
            "Your flame flickers across several positions at once.",
            "You follow the version that burns brightest."
        ],
    },

    # --------------------------------------------------------
    # Decision 3B: Assault the levitation spire
    # --------------------------------------------------------
    "levitation_spire": {
        "Voidrunner": [
            "You ascend the spire through maintenance fins and broken platforms.",
            "Gravity becomes another obstacle too slow to catch you."
        ],
        "Grimshield": [
            "You advance upward beneath concentrated energy fire.",
            "The spire's defenders fail to force you back."
        ],
        "Ashreaver": [
            "You blast apart each stabilizer as you climb.",
            "The elegant tower begins dying in ugly pieces."
        ],
        "Nightreaper": [
            "You move along the exterior where the defenders never expect a human shape.",
            "The command level is breached from the sky."
        ],
        "Umbracaster": [
            "You invert the spire's own field around its defenders.",
            "They drift helplessly while the squad continues upward."
        ],
        "Ritesmith": [
            "You reroute the levitation grid into the structure's supports.",
            "The tower begins carrying loads it was never meant to bear."
        ],
        "Oathkeeper": [
            "You keep the squad secured during each gravity shift.",
            "No one is cast into the sky while you can still reach them."
        ],
        "Fluxhunter": [
            "You remove each shield emitter in ascending order.",
            "The path opens one exact failure at a time."
        ],
        "Fumebinder": [
            "A cloud surrounds the upper levels despite the open air.",
            "The defenders lose sight of the climbing squad."
        ],
        "Emberbrand": [
            "Fire coils upward through the spire's exposed conduits.",
            "The tower becomes a burning beacon against the storm."
        ],
    },

    # --------------------------------------------------------
    # Decision 4A: Seal the gateway
    # --------------------------------------------------------
    "seal_gateway": {
        "Voidrunner": [
            "You carry the final stabilizer into position as reality tears around you.",
            "The gateway closes a heartbeat behind your retreat."
        ],
        "Grimshield": [
            "You hold the approach while the sealing sequence completes.",
            "The things beyond the gateway never cross your line."
        ],
        "Ashreaver": [
            "You overload the gateway anchors and let the rupture consume itself.",
            "Whatever waits beyond receives only fire."
        ],
        "Nightreaper": [
            "You reach the hidden anchor beneath the portal frame.",
            "The gateway dies without revealing what noticed you."
        ],
        "Umbracaster": [
            "You reverse the gateway's phase logic.",
            "The doorway forgets how to remain open."
        ],
        "Ritesmith": [
            "You align the stabilizers according to the archive's geometry.",
            "A machine built to connect worlds becomes a lock."
        ],
        "Oathkeeper": [
            "You refuse to begin the seal until every squadmate is clear.",
            "The gateway closes with no one abandoned on the wrong side."
        ],
        "Fluxhunter": [
            "You strike the final anchor at the exact moment of synchronization.",
            "One shot collapses the corridor between worlds."
        ],
        "Fumebinder": [
            "Smoke pours into the unstable threshold and reveals its collapsing edges.",
            "The squad withdraws through the only safe path."
        ],
        "Emberbrand": [
            "Your flame bends toward the gateway before it closes.",
            "For an instant, something on the other side seems to answer."
        ],
    },

    # --------------------------------------------------------
    # Decision 4B: Send a probe through the gateway
    # --------------------------------------------------------
    "send_probe": {
        "Voidrunner": [
            "You deliver the probe to the threshold and withdraw before the pull intensifies.",
            "The first signal returns while you are still moving."
        ],
        "Grimshield": [
            "You brace the probe assembly against the gateway's force.",
            "Nothing drags it—or the squad—through before the launch completes."
        ],
        "Ashreaver": [
            "You arm the probe with enough explosives to end the conversation if necessary.",
            "Exploration and deterrence travel together."
        ],
        "Nightreaper": [
            "You place the probe beyond the visible edge without exposing the squad.",
            "The other side receives an observer it never sees arrive."
        ],
        "Umbracaster": [
            "You tune the probe to the gateway's shifting resonance.",
            "Its signal survives where ordinary transmission would dissolve."
        ],
        "Ritesmith": [
            "You rebuild the probe's shielding around the archive's phase data.",
            "Human machinery crosses because alien principles now protect it."
        ],
        "Oathkeeper": [
            "You keep every member tethered while the gateway pulls at armor and memory.",
            "The probe leaves. The squad does not."
        ],
        "Fluxhunter": [
            "You launch the probe through the most stable point in the threshold.",
            "Its trajectory vanishes with perfect precision."
        ],
        "Fumebinder": [
            "Particles in your smoke map the gateway's current.",
            "The probe enters through the safest channel."
        ],
        "Emberbrand": [
            "The probe disappears into blue light carrying a small human flame.",
            "Seconds later, the flame appears again—far away."
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
            "You steady yourself and move with the squad.",
            "The unknown waits ahead."
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

def start_mission_05(player, state):
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
    computer("[THREAT] ILLUMINATE INCURSION", delay=0.7)
    computer("[PRIMARY] LOCATE AND DISABLE PHASE GATEWAY", delay=0.7)
    computer("[SECONDARY] RECOVER ALIEN NAVIGATION DATA", delay=0.7)
    computer("[WARNING] COGNITIVE INTERFERENCE DETECTED", delay=1)

    blank()

    radio("[COMMAND CHANNEL]", delay=0.5)

    npc(
        "Tiberius",
        "The Automatons built fortresses. The Illuminate build questions."
    )
    npc(
        "Tiberius",
        "Nereid's Fall stopped transmitting twelve hours ago."
    )

    blank()

    narrate(
        "Orbital observation shows flooded districts, crystalline structures, "
        "and a gateway emitting signals that do not remain in normal space."
    )
    narrate(
        "Civilians still move through the city, but many no longer respond "
        "to human communications."
    )

    blank()

    npc("Tiberius", f"{player.callsign}, enter the city.")
    npc("Tiberius", "Close the door if you can.")
    npc("Tiberius", "Learn what stands beyond it if you must.")

    blank()

    computer(">> DROP VECTOR LOCKED", delay=0.6)
    computer(">> NAVIGATION ERROR: POSITION SHIFT DETECTED", delay=0.6)
    computer(">> MANUAL CORRECTION ACTIVE", delay=0.8)

    blank()

    narrate(
        "The drop pod falls through a storm lit by silent blue lightning."
    )
    narrate(
        "For several seconds, the city appears above, below, and beside you at once."
    )
    narrate(
        "Impact restores gravity with brutal certainty."
    )


# ============================================================
# Decision Point 1
# Choose the route into the occupied city.
# ============================================================

def decision_one(player, state):
    choice = get_choice(
        "The phase gateway lies beyond two unstable approaches.",
        [
            "Enter through the flooded district.",
            "Scale the crystalline causeway.",
        ],
    )

    if choice == 1:
        enter_flooded_district(player, state)
    else:
        scale_crystalline_causeway(player, state)


def enter_flooded_district(player, state):
    blank()

    title_card(
        "APPROACH",
        "FLOODED DISTRICT"
    )

    narrate(
        "Black water fills the lower streets between drowned towers."
    )
    narrate(
        "Human voices echo from buildings where no lights remain."
    )

    blank()

    class_response(player, "flooded_district")

    blank()

    narrate(
        "The district opens toward a plaza dominated by a cognitive beacon."
    )
    narrate(
        "Nearby, enthralled civilians move in silent formation beneath Illuminate overseers."
    )

    decision_two(player, state)


def scale_crystalline_causeway(player, state):
    blank()

    title_card(
        "APPROACH",
        "CRYSTALLINE CAUSEWAY"
    )

    narrate(
        "A translucent bridge rises above the flooded city."
    )
    narrate(
        "Its surface shifts beneath each step, reflecting places that are not present."
    )

    blank()

    class_response(player, "crystal_causeway")

    blank()

    narrate(
        "From the causeway, you identify a cognitive beacon controlling the district."
    )
    narrate(
        "Below it, enthralled civilians gather beneath Illuminate guard."
    )

    decision_two(player, state)


# ============================================================
# Decision Point 2
# Choose between destroying control infrastructure or rescuing civilians.
# ============================================================

def decision_two(player, state):
    choice = get_choice(
        "The Illuminate control the district through both machinery and captured minds.",
        [
            "Destroy the cognitive beacon.",
            "Rescue the enthralled civilians.",
        ],
    )

    if choice == 1:
        destroy_cognitive_beacon(player, state)
    else:
        rescue_enthralled_civilians(player, state)


def destroy_cognitive_beacon(player, state):
    blank()

    title_card(
        "SECONDARY OBJECTIVE",
        "DESTROY COGNITIVE BEACON"
    )

    narrate(
        "The beacon emits no sound, yet pressure builds behind your eyes."
    )
    narrate(
        "Images not belonging to you flash across the edge of thought."
    )

    blank()

    class_response(player, "destroy_beacon")

    blank()

    computer(">> BEACON CORE DESTABILIZED", delay=0.6)
    computer(">> COGNITIVE FIELD COLLAPSING", delay=0.8)

    blank()

    narrate(
        "Across the district, enthralled civilians collapse as the control signal ends."
    )
    narrate(
        "The beacon's final transmission reveals two routes toward the gateway: "
        "a phase archive and a levitation spire."
    )

    decision_three(player, state)


def rescue_enthralled_civilians(player, state):
    blank()

    title_card(
        "SECONDARY OBJECTIVE",
        "BREAK THE THRALL"
    )

    narrate(
        "The civilians walk beneath crystalline restraints attached to the base of their skulls."
    )
    narrate(
        "Illuminate overseers watch from elevated platforms."
    )

    blank()

    class_response(player, "rescue_enthralled")

    blank()

    computer(">> CONTROL FREQUENCY DISRUPTED", delay=0.6)
    computer(">> HUMAN VITAL SIGNS STABILIZING", delay=0.8)

    blank()

    npc("Civilian", "There was a voice behind the light.")
    npc("Civilian", "It knew we were coming before we arrived.")

    blank()

    narrate(
        "Recovered memories point toward a phase archive and a levitation spire "
        "guarding the approach to the gateway."
    )

    decision_three(player, state)


# ============================================================
# Decision Point 3
# Choose how to reach the phase gateway.
# ============================================================

def decision_three(player, state):
    choice = get_choice(
        "Two structures control access to the gateway complex.",
        [
            "Enter the Illuminate phase archive.",
            "Assault the levitation spire.",
        ],
    )

    if choice == 1:
        enter_phase_archive(player, state)
    else:
        assault_levitation_spire(player, state)


def enter_phase_archive(player, state):
    blank()

    title_card(
        "GATEWAY COMPLEX",
        "PHASE ARCHIVE"
    )

    narrate(
        "The archive occupies several overlapping versions of the same chamber."
    )
    narrate(
        "Doors open into places that vanish when observed directly."
    )

    blank()

    class_response(player, "phase_archive")

    blank()

    computer(">> PHASE INDEX ACQUIRED", delay=0.6)
    computer(">> GATEWAY ANCHOR MAP RECOVERED", delay=0.8)

    blank()

    narrate(
        "The archive contains navigation records pointing far beyond mapped space."
    )
    narrate(
        "One route appears repeatedly, marked by a symbol the system refuses to translate."
    )

    decision_four(player, state)


def assault_levitation_spire(player, state):
    blank()

    title_card(
        "GATEWAY COMPLEX",
        "LEVITATION SPIRE"
    )

    narrate(
        "The spire hangs above the city without visible support."
    )
    narrate(
        "Gravity shifts around it in violent, repeating waves."
    )

    blank()

    class_response(player, "levitation_spire")

    blank()

    computer(">> GRAVITY CONTROL OFFLINE", delay=0.6)
    computer(">> GATEWAY SHIELD DISABLED", delay=0.8)

    blank()

    narrate(
        "The spire descends until its foundation touches the city for the first time."
    )
    narrate(
        "Behind it, the phase gateway opens wider."
    )

    decision_four(player, state)


# ============================================================
# Decision Point 4
# Decide whether to close the gateway or investigate it.
# ============================================================

def decision_four(player, state):
    blank()

    narrate(
        "The gateway stands within a circular plaza of black crystal."
    )
    narrate(
        "Beyond it is not another room, but a sky filled with unfamiliar stars."
    )

    blank()

    narrate(
        "Something enormous moves across the distant horizon."
    )
    narrate(
        "The gateway begins widening without any command from the structures around it."
    )

    choice = get_choice(
        "The Veil of Glass cannot remain open.",
        [
            "Seal the gateway immediately.",
            "Send a reconnaissance probe through before sealing it.",
        ],
    )

    if choice == 1:
        seal_phase_gateway(player, state)
    else:
        send_probe_through_gateway(player, state)


def seal_phase_gateway(player, state):
    blank()

    title_card(
        "FINAL OBJECTIVE",
        "CLOSE THE VEIL"
    )

    narrate(
        "The squad moves between gateway anchors while alien forms gather beyond the threshold."
    )
    narrate(
        "Reality fractures around the plaza with every widening pulse."
    )

    blank()

    class_response(player, "seal_gateway")

    blank()

    computer(">> ANCHOR 01 INVERTED", delay=0.5)
    computer(">> ANCHOR 02 INVERTED", delay=0.5)
    computer(">> ANCHOR 03 INVERTED", delay=0.5)
    computer(">> PHASE COLLAPSE INITIATED", delay=0.8)

    blank()

    narrate(
        "The unfamiliar sky folds inward."
    )
    narrate(
        "For one instant, a vast silhouette turns toward the closing doorway."
    )
    narrate(
        "Then the gateway becomes a line of blue light and disappears."
    )

    computer("[PRIMARY OBJECTIVE COMPLETE] GATEWAY SEALED", delay=0.8)

    mission_extraction(player, state, outcome="sealed")


def send_probe_through_gateway(player, state):
    blank()

    title_card(
        "FINAL OBJECTIVE",
        "LOOK BEYOND THE VEIL"
    )

    narrate(
        "A compact reconnaissance probe is prepared while the gateway continues to widen."
    )
    narrate(
        "Its systems were not designed for the physics waiting beyond."
    )

    blank()

    class_response(player, "send_probe")

    blank()

    computer(">> PROBE SHIELDING ACTIVE", delay=0.5)
    computer(">> SIGNAL TETHER ESTABLISHED", delay=0.5)
    computer(">> LAUNCHING", delay=0.8)

    blank()

    narrate(
        "The probe crosses the threshold and vanishes."
    )
    narrate(
        "For twelve seconds, nothing returns."
    )

    blank()

    computer(">> SIGNAL RECEIVED", delay=0.8)
    computer(">> LOCATION UNKNOWN", delay=0.6)
    computer(">> HUMAN STRUCTURES DETECTED", delay=0.8)
    computer(">> MESSAGE FRAGMENT RECOVERED", delay=0.8)

    blank()

    radio("[UNIDENTIFIED TRANSMISSION]", delay=0.5)
    npc("Unknown Voice", "Do not close it.")
    npc("Unknown Voice", "We have been waiting.")

    blank()

    narrate(
        "The voice is human."
    )
    narrate(
        "The gateway surges before the signal can continue."
    )

    blank()

    computer(">> EMERGENCY PHASE COLLAPSE", delay=0.7)
    computer(">> GATEWAY SEALED", delay=0.8)

    mission_extraction(player, state, outcome="probe")


# ============================================================
# Extraction and Open-Ended Mission Conclusion
# ============================================================

def mission_extraction(player, outcome):
    blank()

    radio("[EXTRACTION CHANNEL]", delay=0.5)
    npc("Pelican Pilot", "The entire city is shifting.")
    npc("Pelican Pilot", "Reach the beacon before the landing zone becomes somewhere else.")

    blank()

    narrate(
        "The squad retreats through streets that no longer match the route inward."
    )
    narrate(
        "Illuminate forces flicker between positions while the city folds around the sealed plaza."
    )

    blank()

    narrate(
        "The Pelican appears through rain and blue static."
    )
    narrate(
        "Its ramp lowers for only seconds before the ground beneath it begins to phase."
    )

    blank()

    npc("Pelican Pilot", "Board now. Questions can survive the trip home.")

    blank()

    computer(">> EXTRACTION CONFIRMED", delay=0.8)
    computer(f">> OPERATIVE VERIFIED: {player.callsign.upper()}", delay=0.8)

    blank()

    if outcome == "sealed":
        npc(
            "Tiberius",
            "The gateway is closed."
        )
        npc(
            "Tiberius",
            "That does not mean the path behind it has ceased to exist."
        )

        blank()

        narrate(
            "No transmission escaped the far side."
        )
        narrate(
            "Still, sensors aboard the Spear of Tartarus detect a faint signal following the fleet."
        )

    else:
        npc(
            "Tiberius",
            "A human voice beyond an Illuminate gateway changes the nature of this war."
        )
        npc(
            "Tiberius",
            "We do not yet know whether it was a survivor, a warning, or a lure."
        )

        blank()

        narrate(
            "The probe's final data packet contains a star map with no matching region."
        )
        narrate(
            "One coordinate continues transmitting after the gateway is gone."
        )

    blank()

    title_card(
        "MISSION COMPLETE",
        MISSION_NAME
    )

    computer("[STATUS] PHASE GATEWAY SEALED", delay=0.6)
    computer("[STATUS] ILLUMINATE INCURSION INTERRUPTED", delay=0.6)
    computer("[STATUS] UNKNOWN SIGNAL PERSISTING", delay=0.8)
    computer("[STATUS] OPERATIVE RETURNING TO THE SPEAR OF TARTARUS", delay=1)

    blank()

    npc("Caz", "Your vitals are normal.")
    npc("Caz", "Your neural scan is not.")

    blank()

    npc("Tiberius", "Rest while you can.")

    blank()

    npc("Tiberius", "The signal is still moving.")

    blank()

    narrate(
        "Nereid's Fall disappears behind the carrier."
    )
    narrate(
        "Far beyond visible space, something answers the stolen coordinates."
    )

    blank()

    say("TO BE CONTINUED", delay=2)

    blank()


# ============================================================
# Local Test Runner
#
# Run from the project root with:
#     py story\mission_05_illuminate.py
#
# When this mission is connected to the normal game flow, this
# test runner can be removed entirely.
# ============================================================

if __name__ == "__main__":
    from core.player import Player

    test_player = Player()
    test_player.create_character()

    start_mission_05(test_player)

from core.text import say, narrate, title_card, blank, press_enter


def final_words():
    blank()

    narrate("When the operation ends, the world is still hostile.")
    narrate("The war is not over.")

    blank()

    narrate("But another ember has been carried through the dark.")
    narrate("Another story has been bound into the walls of the Sanctum.")

    blank()

    narrate("Forged in Shadow.")
    narrate("Sealed in Flame.")


def show_service_record(player, state):
    blank()

    title_card(
        "SERVICE RECORD",
        player.callsign.upper()
    )

    say(f"Class: {player.class_name}", delay=0.5)
    say(f"Missions completed: {len(state.completed_missions)}", delay=0.5)
    say(f"Deaths recorded: {state.deaths}", delay=0.5)

    blank()

    say("Carrier visits:", delay=0.5)
    say(
        f"  Hall of Embers: "
        f"{state.visit_count('hall_of_embers')}",
        delay=0.25
    )
    say(
        f"  Mission Planning: "
        f"{state.visit_count('mission_planning')}",
        delay=0.25
    )
    say(
        f"  Armory: "
        f"{state.visit_count('armory')}",
        delay=0.25
    )
    say(
        f"  Med Bay: "
        f"{state.visit_count('med_bay')}",
        delay=0.25
    )
    say(
        f"  Hangar Bay: "
        f"{state.visit_count('hangar_bay')}",
        delay=0.25
    )
    say(
        f"  Mission Deck: "
        f"{state.visit_count('mission_deck')}",
        delay=0.25
    )

    blank()

    if state.has_flag("attempted_undersuit"):
        say("Armor protocol violations: 1", delay=0.5)
    else:
        say("Armor protocol violations: 0", delay=0.5)

    blank()


def thank_you(player, state):
    state.set_flag("currently_deployed", False)
    state.set_flag("campaign_complete")

    final_words()
    show_service_record(player, state)

    title_card(
        "THANK YOU",
        "THE FLAME ENDURES"
    )

    say(
        "Thank you for taking the time to play Ex Umbris Fabricati.",
        delay=1
    )
    say(
        "What began as a fun idea has grown into something much larger.",
        delay=1
    )

    blank()

    say("Look forward to the next adventure.", delay=1)

    blank()

    say("With love,", delay=0.5)
    say("Caz, Artifex of Shadows", delay=1)

    press_enter()
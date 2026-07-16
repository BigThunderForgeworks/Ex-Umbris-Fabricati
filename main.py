from core.player import Player
from core.game_state import GameState

from story.intro import opening, sanctum_registration
from story.prologue import awakening, choose_destination
from story.chapter1 import first_choice
from story.chapter2 import start_mission_02
from story.chapter3 import start_mission_03
from story.chapter4 import start_mission_04
from story.chapter5 import start_mission_05
from story.endings import thank_you


def finish_mission(state, mission_number):
    state.complete_mission(mission_number)
    state.set_flag("currently_deployed", False)


def return_to_carrier(player, state):
    choose_destination(player, state)


def main():
    opening()
    sanctum_registration()

    player = Player()
    state = GameState()

    player.create_character()

    # --------------------------------------------------------
    # Initial carrier exploration and Mission 1 deployment
    # --------------------------------------------------------

    awakening(player, state)

    # --------------------------------------------------------
    # Mission 1
    # --------------------------------------------------------

    mission_01_result = first_choice(player, state)

    if mission_01_result == "sacrifice":
        state.complete_mission(1)
        state.set_flag("currently_deployed", False)
        thank_you(player, state)
        return

    finish_mission(state, 1)

    # --------------------------------------------------------
    # Return to carrier before Mission 2
    # --------------------------------------------------------

    return_to_carrier(player, state)

    # --------------------------------------------------------
    # Mission 2
    # --------------------------------------------------------

    start_mission_02(player, state)
    finish_mission(state, 2)

    # --------------------------------------------------------
    # Return to carrier before Mission 3
    # --------------------------------------------------------

    return_to_carrier(player, state)

    # --------------------------------------------------------
    # Mission 3
    # --------------------------------------------------------

    start_mission_03(player, state)
    finish_mission(state, 3)

    # --------------------------------------------------------
    # Return to carrier before Mission 4
    # --------------------------------------------------------

    return_to_carrier(player, state)

    # --------------------------------------------------------
    # Mission 4
    # --------------------------------------------------------

    start_mission_04(player, state)
    finish_mission(state, 4)

    # --------------------------------------------------------
    # Return to carrier before Mission 5
    # --------------------------------------------------------

    return_to_carrier(player, state)

    # --------------------------------------------------------
    # Mission 5
    # --------------------------------------------------------

    start_mission_05(player, state)
    finish_mission(state, 5)

    # --------------------------------------------------------
    # Campaign ending
    # --------------------------------------------------------

    thank_you(player, state)


if __name__ == "__main__":
    main()
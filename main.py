from core.player import Player
from story.intro import opening, sanctum_registration, mission_intro
from story.chapter1 import first_choice
from story.endings import thank_you


def main():
    opening()
    sanctum_registration()

    player = Player()
    player.create_character()

    mission_intro(player)
    first_choice(player)

    thank_you()


if __name__ == "__main__":
    main()

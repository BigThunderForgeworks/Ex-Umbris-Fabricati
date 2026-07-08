from core.text import say


CLASSES = {
    "voidrunner": {
        "title": "Voidrunner",
        "flavor": "You move where maps fail, crossing the silence between stars with instinct as your compass."
    },
    "grimshield": {
        "title": "Grimshield",
        "flavor": "You are the wall before the storm, the last shadow standing when the line begins to break."
    },
    "ashreaver": {
        "title": "Ashreaver",
        "flavor": "You carry ruin like a sacred tool, reducing enemy strongholds to memory and ash."
    },
    "nightreaper": {
        "title": "Nightreaper",
        "flavor": "You strike from the unseen places, swift as silence and final as the dark."
    },
    "umbracaster": {
        "title": "Umbracaster",
        "flavor": "You wield the hidden arts, shaping shadow, will, and forbidden knowledge into purpose."
    },
    "ritesmith": {
        "title": "Ritesmith",
        "flavor": "You bind craft to ritual, forging order from wreckage and purpose from flame."
    },
    "oathkeeper": {
        "title": "Oathkeeper",
        "flavor": "You stand between ruin and survival, bound by vow to mend the broken and steady the fallen."
    },
    "fluxhunter": {
        "title": "Fluxhunter",
        "flavor": "You track instability through chaos, finding the fracture before the enemy can exploit it."
    },
    "fumebinder": {
        "title": "Fumebinder",
        "flavor": "You command smoke, pressure, and storm, turning confusion into cover and breath into weapon."
    },
    "emberbrand": {
        "title": "Emberbrand",
        "flavor": "You carry the living flame, a spark of defiance that refuses to die in the dark."
    }
}


def choose_class():
    say("Choose your class within Ex Umbris Fabricati:")
    print()

    class_names = list(CLASSES.keys())

    for index, key in enumerate(class_names, start=1):
        print(f"{index}. {CLASSES[key]['title']}")

    print()

    while True:
        choice = input("Enter class number: ").strip()

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(class_names):
                selected_key = class_names[number - 1]
                return CLASSES[selected_key]

        print("Invalid selection. Choose a number from the list.")
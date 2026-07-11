"""
story/prologue.py

Interactive opening sequence before Mission 01.
"""

from core.text import (
    say,
    narrate,
    computer,
    radio,
    title_card,
    blank,
    npc
)
from story.intro import mission_intro


CARRIER_NAME = "The Spear of Tartarus"


def awakening(player):
    title_card(
        "PROLOGUE",
        "AWAKENING"
    )

    narrate("You wake from cold slumber.")
    narrate("For several long seconds, you cannot remember where you are.")

    blank()

    narrate("Frost clings to the edges of your cryogenic chamber.")
    narrate("Pale emergency lights flash across the steel walls around you.")

    blank()

    narrate("You look to your left...")
    narrate("Then to your right...")

    blank()

    narrate("Your armor rests nearby, carefully arranged beside its helmet and cape.")
    narrate("The sight of it stirs something buried beneath the haze.")

    blank()

    narrate("Memories of training return in fragments.")
    narrate("The roar of gunfire.")
    narrate("The smell of sulfur.")
    narrate("The heaviness of a rifle in your hands.")

    blank()

    narrate("Then you remember.")

    blank()

    narrate("You are a Helldiver.")
    narrate("But not merely another soldier cast into an endless war.")

    blank()

    narrate("You left the certainty of Super Earth's command behind.")
    narrate("You chose instead to stand beside those who uphold brotherhood, unity, and purpose.")

    blank()

    narrate("Ex Umbris Fabricati.")
    narrate("Forged from the Shadows.")

    blank()

    equipment_choice(player)


def equipment_choice(player):
    while True:
        print("What do you do?")
        print()
        print("[1] Don your equipment.")
        print("[2] Walk around in your undersuit.")
        print()

        choice = input("Select an option: ").strip()

        if choice == "1":
            don_equipment(player)
            return

        if choice == "2":
            blank()
            say("WRONG.")
            narrate("A Helldiver always wears their armor.")
            narrate("Especially the cape.")
            narrate("All heroes wear capes.")
            blank()
            continue

        say("Invalid selection. Choose option 1 or 2.")


def don_equipment(player):
    blank()

    narrate("You begin donning each piece of armor into place.")
    narrate("It feels tighter than you remember.")

    blank()

    narrate("Yet the familiar pressure brings an unexpected sense of comfort.")
    narrate("The armor does not merely protect you.")
    narrate("It reminds you who you are.")

    blank()

    narrate("You secure your cape across your shoulders.")
    narrate("The fabric settles behind you...an air of grace surrounds you.")

    blank()

    narrate("The helmet comes last.")

    blank()

    # Add sound here for clicks or something to signify helmet is clicking into place

    computer(">> HELMET SEAL CONFIRMED", delay=0.6)
    computer(">> HUD INITIALIZING...", delay=0.8)
    computer(">> HUD ONLINE", delay=0.6)
    computer(">> CONNECTING TO GALNET...", delay=0.8)
    computer(">> GALNET ONLINE", delay=0.6)
    computer(">> OPERATIVE PROFILE DETECTED", delay=0.8)
    computer(
        f">> IDENTITY: {player.callsign.upper()} // {player.class_name.upper()}",
        delay=1.2
    )

    blank()

    narrate("Targeting markers and navigation data flicker across your visor.")
    narrate("The world sharpens into focus.")

    blank()

    narrate(
        f"You stand within the inner Sanctum of the carrier {CARRIER_NAME}."
    )

    narrate("Beyond the chamber, the ship hums with restrained power.")
    narrate("Somewhere beneath your feet, launch crews prepare the drop pods.")

    blank()

    choose_destination(player)


def choose_destination(player):
    title_card(
        CARRIER_NAME.upper(),
        "INNER SANCTUM"
    )

    while True:
        print("Where do you want to go?")
        print()
        print("[1] Visit the Hall of Embers.")
        print("[2] Mission Planning.")
        print("[3] Enter the Armory.")
        print("[4] Visit the Hangar Bay.")
        print("[5] Go to the Med bay.")
        print("[6] Report to the Mission Deck.")
        print()

        choice = input("Select a destination: ").strip()

        if choice == "1":
            visit_hall_of_embers(player)

        elif choice == "2":
            visit_mission_planning(player)

        elif choice == "3":
            visit_armory(player)
        
        elif choice == "4":
            visit_hangar_bay(player)

        elif choice == "5":
            visit_med_bay(player)

        elif choice == "6":
            deployment_confirmed = report_to_mission_deck(player)

            if deployment_confirmed:
                return
            
        else:
            say("Invalid selection. Choose an available destination.")


def visit_hall_of_embers(player):
    blank()

    title_card(
            CARRIER_NAME.upper(),
            "HALL OF EMBERS"
        )

    narrate("You enter the Hall of Embers.")
    narrate("A low flame burns at its center, reflected across walls of darkened steel.")

    blank()

    narrate("Names have been etched into those walls.")
    narrate("Specters. Veterans. The Eclipsed.")
    narrate("Each one is remembered.")

    blank()

    narrate("You stand before the flame for a moment.")
    narrate("Then you return to the inner Sanctum.")

    blank()


# ------------------------------------------------------------
# Mission Planning
# ------------------------------------------------------------

def visit_mission_planning(player):
    blank()

    title_card(
        "MISSION PLANNING",
        "The Spear of Tartarus"
    )

    narrate(
        "The Mission Planning Chamber hums quietly beneath the weight of countless campaigns."
    )

    narrate(
        "Massive holographic displays drift above a circular command table, "
        "showing occupied sectors, supply routes, and active operations."
    )

    blank()

    narrate(
        "Officers move through the chamber exchanging reports in hushed voices."
    )

    narrate(
        "No one raises their voice."
    )

    narrate(
        "They don't need to."
    )

    blank()

    narrate(
        "Standing alone at the center of the room is the Marshal of Shadows."
    )

    blank()

    say("TIBERIUS", delay=1)
    say("Marshal of Shadows", delay=2)

    blank()

    narrate(
        "His attention never leaves the tactical display."
    )

    narrate(
        "Entire worlds shift beneath his fingertips as deployment routes adjust across the map."
    )

    blank()

    narrate(
        "Eventually..."
    )

    narrate(
        "without ever turning around..."
    )

    blank()

    npc("Tiberius", "You have questions.")

    blank()

    npc(
        "Tiberius",
        "Most recruits ask where they are going."
    )

    npc(
        "Tiberius",
        "Veterans ask who will return."
    )

    blank()

    narrate(
        "Only now does he finally look toward you."
    )

    blank()

    class_name = player.class_name

    if class_name == "Voidrunner":

        npc(
            "Tiberius",
            "A Voidrunner never waits for opportunity."
        )

        npc(
            "Tiberius",
            "Create it."
        )

    elif class_name == "Grimshield":

        npc(
            "Tiberius",
            "Every squad needs someone willing to stand when others cannot."
        )

        npc(
            "Tiberius",
            "Do not mistake stubbornness for courage."
        )

    elif class_name == "Ashreaver":

        npc(
            "Tiberius",
            "Fire is an effective servant."
        )

        npc(
            "Tiberius",
            "Never allow it to become your commander."
        )

    elif class_name == "Nightreaper":

        npc(
            "Tiberius",
            "Victory often belongs to the soldier never seen."
        )

        npc(
            "Tiberius",
            "Let the enemy fear shadows."
        )

    elif class_name == "Umbracaster":

        npc(
            "Tiberius",
            "Confusion is a weapon."
        )

        npc(
            "Tiberius",
            "Use it wisely."
        )

    elif class_name == "Ritesmith":

        npc(
            "Tiberius",
            "Wars are not won solely by rifles."
        )

        npc(
            "Tiberius",
            "Someone must keep the forge burning."
        )

    elif class_name == "Oathkeeper":

        npc(
            "Tiberius",
            "Life is our rarest resource."
        )

        npc(
            "Tiberius",
            "Guard it well."
        )

    elif class_name == "Fluxhunter":

        npc(
            "Tiberius",
            "One precise shot may achieve what a thousand rounds cannot."
        )

        npc(
            "Tiberius",
            "Patience is often deadlier than aggression."
        )

    elif class_name == "Fumebinder":

        npc(
            "Tiberius",
            "Control the battlefield..."
        )

        npc(
            "Tiberius",
            "...and the battle often controls itself."
        )

    elif class_name == "Emberbrand":

        npc(
            "Tiberius",
            "The flame inspires."
        )

        npc(
            "Tiberius",
            "Ensure it inspires your allies more than your enemies."
        )

    else:

        npc(
            "Tiberius",
            "Every Helldiver writes a story."
        )

        npc(
            "Tiberius",
            "Few remember they are also writing everyone else's."
        )

    blank()

    npc(
        "Tiberius",
        "Remember why Ex Umbris Fabricati exists."
    )

    npc(
        "Tiberius",
        "Not for glory."
    )

    npc(
        "Tiberius",
        "Not for recognition."
    )

    npc(
        "Tiberius",
        "For the Helldiver standing beside you."
    )

    blank()

    narrate(
        "The Marshal turns back toward the tactical display."
    )

    narrate(
        "The conversation is over."
    )

    narrate(
        "Somehow..."
    )

    narrate(
        "you feel you have learned far more than was actually said."
    )

    blank()

# ------------------------------------------------------------
# Armory
# ------------------------------------------------------------

def visit_armory(player):
    blank()

    title_card(
        "ARMORY",
        "The Spear of Tartarus"
    )

    narrate("The Armory is anything but quiet.")
    narrate("Tools strike steel.")
    narrate("Magazines lock into place.")
    narrate("Weapons are field-stripped, inspected, and rebuilt with practiced precision.")

    blank()

    narrate("Three Helldivers occupy the center workbench.")
    narrate("From the sound of things...")
    narrate("they have been arguing for quite some time.")

    blank()

    npc("Valinor", "I am telling you...")
    npc("Valinor", "Everything is better with fire.")

    blank()

    npc("Atreides", "Everything is not better with fire.")
    npc("Atreides", "Sometimes precision is the correct answer.")

    blank()

    npc("Spooky", "Precision is nice.")
    npc("Spooky", "Fire is fun.")
    npc("Spooky", "I see no conflict here.")

    blank()

    npc("Valinor", "Exactly.")

    blank()

    npc("Atreides", "You are both impossible.")

    blank()

    narrate("The conversation pauses as all three notice your arrival.")

    blank()

    say("ATREIDES", delay=1)
    say("Fluxhunter", delay=1.5)

    blank()

    say("SPOOKY", delay=1)
    say("Ashreaver", delay=1.5)

    blank()

    say("VALINOR_07", delay=1)
    say("Emberbrand", delay=2)

    blank()

    narrate("Atreides rests one hand beside a carefully calibrated rifle.")
    narrate("Spooky continues cleaning a weapon marked by old scorch damage.")
    narrate("Valinor stands beside enough incendiary equipment to concern any reasonable person.")

    blank()

    class_name = player.class_name

    # --------------------------------------------------------
    # Voidrunner
    # --------------------------------------------------------

    if class_name == "Voidrunner":
        npc("Atreides", "A Voidrunner.")
        npc("Atreides", "You move faster than most people can aim.")
        npc("Atreides", "Try not to cross my line of fire.")

        blank()

        npc("Spooky", "If you do cross it...")
        npc("Spooky", "Move faster.")

        blank()

        npc("Valinor", "Or trail fire behind you.")
        npc("Valinor", "That would make you easier to track.")

    # --------------------------------------------------------
    # Grimshield
    # --------------------------------------------------------

    elif class_name == "Grimshield":
        npc("Atreides", "A Grimshield.")
        npc("Atreides", "Stand between me and the enemy.")
        npc("Atreides", "I will handle the rest.")

        blank()

        npc("Spooky", "That is his polite way of asking you to absorb incoming fire.")

        blank()

        npc("Valinor", "Do not worry.")
        npc("Valinor", "I will provide covering flames.")

        blank()

        npc("Atreides", "That phrase does not reassure anyone.")

    # --------------------------------------------------------
    # Ashreaver
    # --------------------------------------------------------

    elif class_name == "Ashreaver":
        npc("Spooky", "Another Ashreaver.")
        npc("Spooky", "Good.")
        npc("Spooky", "Someone else understands that restraint is optional.")

        blank()

        npc("Atreides", "Restraint is not optional.")

        blank()

        npc("Valinor", "It is when fire is involved.")

        blank()

        npc("Spooky", "See?")
        npc("Spooky", "You are going to fit in just fine.")

    # --------------------------------------------------------
    # Nightreaper
    # --------------------------------------------------------

    elif class_name == "Nightreaper":
        npc("Atreides", "A Nightreaper.")
        npc("Atreides", "Quiet movement. Clean kills.")
        npc("Atreides", "Respectable.")

        blank()

        npc("Spooky", "Too quiet.")
        npc("Spooky", "I prefer the enemy to know exactly why they are dying.")

        blank()

        npc("Valinor", "They usually notice the flames.")

        blank()

        npc("Atreides", "Everyone notices the flames, Valinor.")

    # --------------------------------------------------------
    # Umbracaster
    # --------------------------------------------------------

    elif class_name == "Umbracaster":
        npc("Spooky", "An Umbracaster.")
        npc("Spooky", "Good.")
        npc("Spooky", "Someone else who appreciates battlefield confusion.")

        blank()

        npc("Atreides", "Confusion is useful when it belongs to the enemy.")

        blank()

        npc("Valinor", "Fire creates confusion.")

        blank()

        npc("Atreides", "Fire also creates maintenance reports.")

        blank()

        npc("Spooky", "Also useful.")
        npc("Spooky", "They keep command occupied.")

    # --------------------------------------------------------
    # Ritesmith
    # --------------------------------------------------------

    elif class_name == "Ritesmith":
        npc("Atreides", "A Ritesmith.")
        npc("Atreides", "Good.")
        npc("Atreides", "You may be the only person here capable of keeping their equipment functional.")

        blank()

        npc("Spooky", "My equipment functions.")

        blank()

        narrate("Spooky lifts a scorched weapon from the bench.")
        narrate("A loose component falls onto the floor.")

        blank()

        npc("Spooky", "Mostly.")

        blank()

        npc("Valinor", "Can you increase the fuel pressure on this flamethrower?")

        blank()

        npc("Atreides", "Do not answer that.")

    # --------------------------------------------------------
    # Oathkeeper
    # --------------------------------------------------------

    elif class_name == "Oathkeeper":
        npc("Spooky", "An Oathkeeper?")
        npc("Spooky", "Excellent.")

        blank()

        npc("Valinor", "Now someone can keep us alive when my ideas succeed.")

        blank()

        npc("Atreides", "You mean when your ideas fail.")

        blank()

        npc("Valinor", "The distinction is mostly philosophical.")

        blank()

        npc("Atreides", "Stay close to them.")
        npc("Atreides", "You will be busy.")

    # --------------------------------------------------------
    # Fluxhunter
    # --------------------------------------------------------

    elif class_name == "Fluxhunter":
        npc("Atreides", "Another Fluxhunter.")
        npc("Atreides", "Good.")
        npc(
            "Atreides",
            "Someone around here still understands that one accurate shot "
            "beats a hundred wasted ones."
        )

        blank()

        npc("Spooky", "Or...")
        npc("Spooky", "One hundred accurate shots.")

        blank()

        npc("Valinor", "While on fire.")

        blank()

        npc("Atreides", "I regret beginning this conversation.")

    # --------------------------------------------------------
    # Fumebinder
    # --------------------------------------------------------

    elif class_name == "Fumebinder":
        npc("Atreides", "A Fumebinder.")
        npc("Atreides", "Keep the enemy blinded.")
        npc("Atreides", "Just leave me a clear firing lane.")

        blank()

        npc("Spooky", "Or fill the entire field with smoke.")
        npc("Spooky", "Then we all become surprises.")

        blank()

        npc("Valinor", "Smoke usually means fire is nearby.")

        blank()

        npc("Atreides", "Not everything leads back to fire.")

        blank()

        npc("Valinor", "Eventually it does.")

    # --------------------------------------------------------
    # Emberbrand
    # --------------------------------------------------------

    elif class_name == "Emberbrand":
        npc("Valinor", "Now there is someone with taste.")
        npc("Valinor", "Ignore them.")
        npc("Valinor", "Fire solves everything eventually.")

        blank()

        npc("Atreides", "Including our paint jobs.")

        blank()

        npc("Spooky", "Paint can be replaced.")

        blank()

        npc("Valinor", "Exactly.")

        blank()

        npc("Atreides", "You are encouraging each other again.")
        npc("Atreides", "That is never a good sign.")

    # --------------------------------------------------------
    # Fallback
    # --------------------------------------------------------

    else:
        npc("Atreides", "Know your weapon.")
        npc("Atreides", "Know your target.")
        npc("Atreides", "Do not confuse the order.")

        blank()

        npc("Spooky", "And bring enough ammunition.")

        blank()

        npc("Valinor", "And fuel.")

    blank()

    narrate("Atreides returns his attention to the rifle before him.")
    narrate("The calibration display shifts by a fraction.")

    blank()

    narrate("Spooky checks the action on his weapon.")
    narrate("It produces a noise that does not inspire confidence.")

    blank()

    narrate("Valinor quietly lifts another flamethrower from beneath the workbench.")

    blank()

    npc("Atreides", "Why do you need three?")

    blank()

    npc("Valinor", "One might run out.")

    blank()

    npc("Spooky", "That is actually reasonable.")

    blank()

    narrate("Atreides slowly lowers his tools.")

    blank()

    npc("Atreides", "I hate that you are both making sense.")

    blank()

    narrate("The argument resumes before you have even reached the door.")

    blank()

# ------------------------------------------------------------
# Med Bay
# ------------------------------------------------------------

def visit_med_bay(player):
    blank()

    title_card(
        "MED BAY",
        "The Spear of Tartarus"
    )

    narrate("The Med Bay is unusually quiet.")
    narrate(
        "The sterile scent of antiseptic mingles with machine oil, "
        "freshly cleaned armor, and the faint chemical bite of stimulants."
    )

    blank()

    narrate("Rows of medical supplies line polished steel cabinets.")
    narrate("Every instrument sits exactly where it belongs.")

    blank()

    narrate(
        "At the center of the room, a lone Helldiver methodically loads "
        "fresh cartridges into a rack of Stim Pistols."
    )
    narrate("Each movement is measured, deliberate, and practiced.")

    blank()

    narrate("Without looking up, the operative speaks.")

    blank()

    npc("Caz", "Mission already?")
    npc("Caz", "They never seem to stop these days.")

    blank()

    narrate("Another stim cartridge clicks into place.")

    blank()

    narrate("The operative finally turns toward you.")
    narrate("The insignia upon his armor identifies him immediately.")

    blank()

    say("CAZ", delay=1)
    say("Artifex of Shadows", delay=2)

    blank()

    narrate("There is no rush in Caz's movements.")
    narrate("Everything is measured.")
    narrate("Everything has purpose.")
    narrate("It is the confidence of someone accustomed to bringing people home.")

    blank()

    class_name = player.class_name

    if class_name == "Voidrunner":
        npc("Caz", "A Voidrunner.")
        npc("Caz", "You people always disappear over the horizon before anyone can stop you.")
        npc("Caz", "Try to leave enough of a trail that I can find you when things go wrong.")

    elif class_name == "Grimshield":
        npc("Caz", "A Grimshield.")
        npc("Caz", "Standing between danger and everyone else is admirable.")
        npc("Caz", "It is also an excellent way to become my most frequent patient.")

    elif class_name == "Ashreaver":
        npc("Caz", "An Ashreaver.")
        npc("Caz", "I assume the scorch marks are intentional.")
        npc("Caz", "Just remember that friendly armor burns too.")

    elif class_name == "Nightreaper":
        npc("Caz", "A Nightreaper.")
        npc("Caz", "You are difficult enough to find when you are healthy.")
        npc("Caz", "Do not make me search the whole battlefield while you quietly bleed somewhere.")

    elif class_name == "Umbracaster":
        npc("Caz", "An Umbracaster.")
        npc("Caz", "You keep their attention elsewhere.")
        npc("Caz", "I will make sure our people remain alive long enough to benefit from it.")

    elif class_name == "Ritesmith":
        npc("Caz", "A Ritesmith.")
        npc("Caz", "You repair machines. I repair Helldivers.")
        npc("Caz", "Between the two of us, perhaps this operation will return in one piece.")

    elif class_name == "Oathkeeper":
        npc("Caz", "An Oathkeeper.")
        npc("Caz", "Good.")
        npc("Caz", "We will both have plenty of work today.")

        blank()

        narrate("A faint smile crosses Caz's face.")

        blank()

        npc("Caz", "Try not to steal all my patients.")

    elif class_name == "Fluxhunter":
        npc("Caz", "A Fluxhunter.")
        npc("Caz", "I have seen your kind turn impossible odds into impressive casualty reports.")
        npc("Caz", "Aim carefully. I would rather treat the enemy's mistakes than yours.")

    elif class_name == "Fumebinder":
        npc("Caz", "A Fumebinder.")
        npc("Caz", "Smoke is useful until nobody can see the wounded.")
        npc("Caz", "Leave me a clear path, and I will handle the rest.")

    elif class_name == "Emberbrand":
        npc("Caz", "An Emberbrand.")
        npc("Caz", "I know the flame is part of the appeal.")
        npc("Caz", "Try not to arrive back here still actively on fire.")

    else:
        npc("Caz", "Everyone wants to be remembered as the hero.")
        npc("Caz", "Few volunteer to make sure the hero gets home.")

    blank()

    narrate(
        "Caz removes one final stim cartridge from the rack "
        "and checks its pressure seal."
    )
    narrate("Satisfied, he locks it into place.")

    blank()

    npc("Caz", "Hopefully, you will not need one of these.")

    blank()

    npc("Caz", "But hope has never been a reliable strategy.")

    blank()

    narrate(
        "Without another word, Caz returns to preparing medical equipment "
        "for the next deployment."
    )

    blank()

    narrate("As you reach the doorway, his voice follows you.")

    blank()

    npc("Caz", "Come back.")

    blank()

    npc("Caz", "Preferably standing.")

    blank()

# ------------------------------------------------------------
# Hangar Bay
# ------------------------------------------------------------

def visit_hangar_bay(player):
    blank()

    title_card(
        "HANGAR BAY",
        "The Spear of Tartarus"
    )

    narrate(
        "The Hangar Bay is alive with controlled chaos."
    )

    narrate(
        "Deck crews weave between Pelicans and drop pods while engineers race against the clock."
    )

    narrate(
        "Fuel lines hiss."
    )

    narrate(
        "Hydraulic lifts whine."
    )

    narrate(
        "Somewhere overhead, a launch alarm briefly sounds before falling silent once more."
    )

    blank()

    narrate(
        "Every Helldiver you pass is preparing for deployment."
    )

    narrate(
        "Except one."
    )

    blank()

    narrate(
        "Leaning comfortably against a stack of supply crates is a Helldiver who appears to have absolutely nowhere important to be."
    )

    blank()

    say("BREXOR", delay=1)
    say("Sanctum Operative", delay=2)

    blank()

    narrate(
        "He notices you almost immediately."
    )

    narrate(
        "A grin slowly spreads across his face."
    )

    blank()

    npc(
        "Brexor",
        "Hey..."
    )

    npc(
        "Brexor",
        "Come here for a second."
    )

    blank()

    narrate(
        "He glances around the Hangar as though checking to make sure nobody is listening."
    )

    blank()

    npc(
        "Brexor",
        "You know what this carrier is called..."
    )

    blank()

    npc(
        "Brexor",
        "The Spear of Tartarus."
    )

    blank()

    npc(
        "Brexor",
        "...my idea."
    )

    blank()

    narrate(
        "He folds his arms proudly."
    )

    blank()

    npc(
        "Brexor",
        "Named it myself."
    )

    blank()

    narrate(
        "Before you can respond..."
    )

    blank()

    npc(
        "Deck Chief",
        "That's what you said about the last three ships."
    )

    blank()

    narrate(
        "Brexor lets out a dramatic sigh."
    )

    blank()

    npc(
        "Brexor",
        "Nobody ever believes me."
    )

    blank()

    npc(
        "Brexor",
        "History is written by people with better paperwork."
    )

    blank()

    narrate(
        "He leans in slightly."
    )

    blank()

    npc(
        "Brexor",
        "Between you and me..."
    )

    blank()

    npc(
        "Brexor",
        "I definitely named this one."
    )

    blank()

    narrate(
        "A mechanic walks past, shaking their head."
    )

    blank()

    npc(
        "Mechanic",
        "You absolutely did not."
    )

    blank()

    npc(
        "Brexor",
        "See?"
    )

    npc(
        "Brexor",
        "The conspiracy goes deeper than I thought."
    )

    blank()

    narrate(
        "He laughs to himself before pointing toward the rows of waiting drop pods."
    )

    blank()

    npc(
        "Brexor",
        "Seriously though..."
    )

    npc(
        "Brexor",
        "Whatever happens down there..."
    )

    blank()

    npc(
        "Brexor",
        "Come back."
    )

    blank()

    npc(
        "Brexor",
        "Someone has to keep confirming my story."
    )

    blank()

    npc(
        "Brexor",
        "One day they'll finally admit I named this ship."
    )

    blank()

    narrate(
        "Somehow..."
    )

    narrate(
        "you suspect they never will."
    )

    blank()

    narrate(
        "Behind him, another Pelican settles onto the deck as crews rush to prepare the next wave of deployments."
    )

    blank()

    npc("Brexor", "Oh!")

    blank()

    npc("Brexor", "If anyone asks...")

    blank()

    npc("Brexor", "You heard it from me first.")


# ------------------------------------------------------------
# Mission Deck
# ------------------------------------------------------------

def report_to_mission_deck(player):
    blank()

    title_card(
        "MISSION DECK",
        "The Spear of Tartarus"
    )

    narrate("The Mission Deck is alive with disciplined activity.")
    narrate("Operations officers relay tactical updates between rows of illuminated terminals.")
    narrate("Flight crews finalize launch windows.")
    narrate("Technicians perform final diagnostics on the waiting drop pods.")

    blank()

    computer("[SYS] OPERATIVE DETECTED", delay=0.6)
    computer(
        f"[SYS] CALLSIGN: {player.callsign.upper()}",
        delay=0.6
    )
    computer(
        f"[SYS] CLASSIFICATION: {player.class_name.upper()}",
        delay=0.8
    )
    computer("[SYS] DROP WINDOW AVAILABLE", delay=1)

    blank()

    radio("[SHIPWIDE COMMUNICATION]", delay=0.5)
    npc("Tiberius", "Attention, Sanctum.")
    npc("Tiberius", "Your destination has already been chosen.")
    npc("Tiberius", "What remains...")
    npc("Tiberius", "...is what you choose to become once you arrive.")

    blank()

    npc("Operations Officer", "Drop pods are green.")
    npc("Operations Officer", "All Helldivers report to launch stations.")

    blank()

    # Show the mission briefing the first time the player enters.
    mission_intro(player)

    while True:
        blank()

        title_card(
            "FINAL CHECK",
            "DEPLOYMENT CONTROL"
        )

        print("[1] Review the mission briefing.")
        print("[2] Return to the carrier.")
        print("[3] Deploy.")
        print()

        choice = input("Select an option: ").strip()

        if choice == "1":
            blank()
            mission_intro(player)

        elif choice == "2":
            blank()
            npc("Operations Officer", "Deployment placed on standby.")
            narrate("You step away from the launch station and return to the inner Sanctum.")
            blank()

            return False

        elif choice == "3":
            deploy_sequence(player)
            return True

        else:
            say("Invalid selection. Choose option 1, 2, or 3.")

# ------------------------------------------------------------
# Deployment Sequence
# ------------------------------------------------------------

def deploy_sequence(player):
    blank()

    npc("Operations Officer", "Deployment confirmed.")

    blank()

    narrate("You approach the waiting drop pod.")
    narrate("Its armored hatch stands open beneath the harsh lights of the Mission Deck.")

    blank()

    narrate("You step inside.")
    narrate("The restraints lock across your armor.")
    narrate("The hatch closes.")

    blank()

    computer(">> MAGNETIC LOCKS ENGAGED", delay=0.6)
    computer(">> POD SYSTEMS INITIALIZING...", delay=0.8)
    computer(">> POD SYSTEMS ONLINE", delay=0.6)
    computer(">> LIFE SUPPORT ONLINE", delay=0.6)
    computer(">> NAVIGATION LINK ESTABLISHED", delay=0.6)
    computer(">> HELLDIVER VERIFIED", delay=0.6)
    computer(
        f">> CALLSIGN VERIFIED: {player.callsign.upper()}",
        delay=0.8
    )
    computer(">> DROP SEQUENCE AUTHORIZED", delay=1)

    blank()

    radio("[PRIVATE COMMUNICATION]", delay=0.5)

    npc("Caz", "Try not to make me work too hard today.")

    blank()

    npc("Brexor", "And remember...")

    blank()

    npc("Brexor", "I named this ship.")

    blank()

    npc("Unknown Crew Member", "Negative.")

    blank()

    npc("Brexor", "Still worth a shot.")

    blank()

    narrate("The communication channel closes.")

    blank()

    radio("[COMMAND CHANNEL]", delay=0.5)

    npc("Tiberius", "Helldiver.")

    blank()

    npc("Tiberius", "Bring them home.")

    blank()

    computer(">> DROP SEQUENCE INITIATED", delay=1)

    blank()

    say("3...", delay=1)
    say("2...", delay=1)
    say("1...", delay=1.5)

    blank()

    say("THUNK", delay=1)

    blank()

    computer(">> DROP POD LAUNCHED", delay=1)

    blank()

    narrate("The pod tears free from The Spear of Tartarus.")
    narrate("Your body presses into the restraints as the carrier vanishes above you.")
    narrate("Fire spreads across the viewport.")
    narrate("The surface rushes closer.")

    blank()

    narrate("There is no turning back now.")

    blank()
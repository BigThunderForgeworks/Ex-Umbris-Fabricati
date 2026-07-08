import sys
import time


# ------------------------------------------------------------
# Text / Display Settings
# ------------------------------------------------------------

DEFAULT_PAUSE = 2
NARRATION_SPEED = 0.03
COMPUTER_SPEED = 0.015
RADIO_SPEED = 0.02
MARSHAL_SPEED = 0.045


# ------------------------------------------------------------
# Basic Timing
# ------------------------------------------------------------

def pause(seconds=DEFAULT_PAUSE):
    time.sleep(seconds)


def blank(lines=1):
    for _ in range(lines):
        print()


# ------------------------------------------------------------
# Instant Text
# ------------------------------------------------------------

def say(text="", delay=DEFAULT_PAUSE):
    print(text)
    pause(delay)


def system(text="", delay=DEFAULT_PAUSE):
    print(text)
    pause(delay)


# ------------------------------------------------------------
# Typewriter Core
# ------------------------------------------------------------

def typewriter(text="", speed=NARRATION_SPEED, delay=1.5):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

    print()
    pause(delay)


# ------------------------------------------------------------
# Voice / Style Functions
# ------------------------------------------------------------

def narrate(text="", delay=1.5):
    typewriter(text, speed=NARRATION_SPEED, delay=delay)


def computer(text="", delay=1.0):
    typewriter(text, speed=COMPUTER_SPEED, delay=delay)


def radio(text="", delay=1.0):
    typewriter(text, speed=RADIO_SPEED, delay=delay)


def marshal(text="", delay=2.0):
    typewriter(text, speed=MARSHAL_SPEED, delay=delay)


# ------------------------------------------------------------
# Formatting Helpers
# ------------------------------------------------------------

def divider(delay=1):
    say("══════════════════════════════════════════════", delay)


def title_card(title, subtitle=None):
    divider(1)
    say(f"        {title}", 2)

    if subtitle:
        say(f"        {subtitle}", 2)

    divider(2)


def section_header(text):
    blank()
    say("──────────────────────────────────────────────", 0.5)
    say(text, 1)
    say("──────────────────────────────────────────────", 0.5)
    blank()


# ------------------------------------------------------------
# Input Helpers
# ------------------------------------------------------------

def ask(prompt_text):
    return input(prompt_text).strip()


def press_enter():
    blank()
    input("Press Enter to continue...")
    blank()
# imports microbit library
from microbit import *

# imports music library
import music

# MODELS
# config values
# starting octave
OCTAVE = 4
# starting duration
DURATION = 1

# VIEW METHODS
def show_note(note, octave):
    constructed_note = note + octave
    display.scroll(constructed_note)


# CONTROLLER METHODS
def play_note(note, octave, duration):
    constructed_note = str(note) + str(octave) + ":" + str(duration)

    show_note(note, octave)
    music.play(constructed_note)

def up_octave(value):
    OCTAVE += value

def down_octave(value):
    OCTAVE -= value

def up_duration(value):
    DURATION += value

def down_duration(value):
    DURATION -= value

music.set_tempo(ticks=15, bpm=240)

while True:
    # sets up note pins
    C = pin1.is_touched()
    D = pin8.is_touched()
    E = pin12.is_touched()
    F = pin2.is_touched()
    G = pin13.is_touched()
    A = pin15.is_touched()
    B = pin16.is_touched()

    # sets up logic for note touches
    if C:
        play_note("C", OCTAVE, DURATION)
    elif D:
        play_note("D", OCTAVE, DURATION)
    elif E:
        play_note("E", OCTAVE, DURATION)
    elif F:
        play_note("F", OCTAVE, DURATION)
    elif G:
        play_note("G", OCTAVE, DURATION)
    elif A:
        play_note("A", OCTAVE, DURATION)
    elif B:
        play_note("B", OCTAVE, DURATION)

    # octave control
    elif button_a.is_pressed():
        down_octave(1)
    elif button_b.is_pressed():
        up_octave(1)
    elif button_a.is_pressed() and button_b.is_pressed():
        display.show(OCTAVE)
    else:
        display.show(Image.ASLEEP)

    play_note("C", OCTAVE, DURATION)
# imports microbit library
from microbit import *

# imports music library
import music

# MODELS
# config values
# starting octave
OCTAVE = 4
# starting duration
DURATION = 4
BPM = 240

# VIEW METHODS
def show_note(note, octave):
    constructed_note = note + octave
    display.scroll(constructed_note)


# CONTROLLER METHODS
def play_note(note, octave, duration):
    constructed_note = str(note) + str(octave) + ":" + str(duration)

    show_note(note, octave)
    music.play(constructed_note)

def increase_octave(value):
    if OCTAVE < 8:
        OCTAVE += value
    else:
        OCTAVE = 8

def decrease_octave(value):
    if OCTAVE > 1:
        OCTAVE -= value
    else:
        OCTAVE = 1

def up_duration(value):
    DURATION += value

def down_duration(value):
    DURATION -= value

def up_bpm(value):
    BPM += value

def down_bpm(value):
    BPM -= value

music.set_tempo(ticks=15, bpm=BPM)

while True:
    # sets up note pins
    C = pin1.is_touched()
    D = pin8.is_touched()
    E = pin12.is_touched()
    F = pin2.is_touched()
    G = pin13.is_touched()
    A = pin15.is_touched()
    B = pin16.is_touched()

    up_tempo = button_a.is_pressed()
    down_tempo = button_b.is_pressed()

    up_octave = pin19.is_touched()
    down_octave = pin20.is_touched()

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

    # tempo control
    elif up_tempo:
        up_bpm(10)
        display.scroll(BPM)
        music.set_tempo(ticks=15, bpm=BPM)

    elif down_tempo:
        down_bpm(10)
        display.scroll(BPM)
        music.set_tempo(ticks=15, bpm=BPM)


    # octave control
    elif down_octave:
        decrease_octave(1)
    elif button_b.is_pressed():
        increase_octave(1)
    elif button_a.is_pressed() and button_b.is_pressed():
        display.show(OCTAVE)
    else:
        display.show(Image.ASLEEP)

    play_note("C", OCTAVE, DURATION)
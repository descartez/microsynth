# imports microbit library
from microbit import *

# imports music library
import music

# MODELS
# config values
# starting octave
OCTAVE = 4
DURATION = 1

# VIEW METHODS
def show_note(note, octave):
    constructed_note = note + ":" + octave
    display.scroll(constructed_note)



# CONTROLLER METHODS
def play_note(note, octave, duration):
    constructed_note = str(note) + str(octave) + ":" + str(duration)
    music.play(constructed_note)

def up_octave(value):
    OCTAVE += 1

def down_octave(value):
    OCTAVE -= 1


while True:
    if button_a.is_pressed():
        down_octave(1)
    elif button_b.is_pressed():
        up_octave(1)
    elif button_a.is_pressed() and button_b.is_pressed():
        display.show(OCTAVE)
    else:
        display.show(Image.ASLEEP)

    play_note("C", OCTAVE, DURATION)
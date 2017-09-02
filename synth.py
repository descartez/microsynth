# imports microbit library
from microbit import *

# imports music library
import music

class Synth():
    def __init__(self):
        self.octave = 4
        self.tempo = 240


    def up_octave(self, value):
        self.octave += value

    def down_octave(self, value):
        self.octave -= value

    def play_note(note, octave, duration):
        contructed_note = str(note) + str(octave) + ":" + str(duration)
        music.play(constructed_note)

synth = Synth()

music.set_tempo(ticks=15, bpm=synth.tempo)

while True:
    # octave control
    if button_a.is_pressed():
        synth.down_octave(1)
        display.show(str(synth.octave))
        synth.play_note("C", 8, 150)
    elif button_b.is_pressed():
        synth.up_octave(1)
        display.show(str(synth.octave))
        synth.play_note("C", 4, 150)
    elif button_a.is_pressed() and button_b.is_pressed():
        display.show(synth.octave)
    else:
        display.show(Image.ASLEEP)
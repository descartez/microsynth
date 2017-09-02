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

    def play_note(self, note):
        music.play((str(note) + str(self.octave) + ":4"))

synth = Synth()

music.set_tempo(ticks=15, bpm=synth.tempo)

while True:
    # octave control
    if button_a.is_pressed():
        synth.down_octave(1)
        display.show(str(synth.octave))
        synth.play_note("C")
    elif button_b.is_pressed():
        synth.up_octave(1)
        display.show(str(synth.octave))
        synth.play_note("C")
    elif button_a.is_pressed() and button_b.is_pressed():
        display.show(synth.octave)
    else:
        display.show(Image.ASLEEP)
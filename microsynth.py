# imports microbit library
from microbit import *

# imports music library
import music

class Synth():
    def __init__(self):
        self.octave = 4
        self.tempo = 240


    def up_octave(self, value):
        if self.octave < 8:
            self.octave += value
        else:
            self.octave = 9

    def down_octave(self, value):
        if self.octave > 1:
            self.octave -= value
        else:
            self.octave = 0

    def play_note(self, note):
        music.play((str(note) + str(self.octave) + ":4"))

synth = Synth()

jingle = ["C4:4","D4:4","E5:4","C6:4"]

music.set_tempo(ticks=15, bpm=synth.tempo)

# starting jingle
music.play(jingle)

while True:
    # octave control
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(str(synth.octave))
    elif pin1.read_digital():
        display.show("A")
        synth.play_note("A")
    elif pin2.read_digital():
        display.show("B")
        synth.play_note("B")
    elif pin3.read_digital():
        display.show("C")
        synth.play_note("C")
    elif pin8.read_digital():
        display.show("D")
        synth.play_note("D")
    elif pin12.read_digital():
        display.show("E")
        synth.play_note("E")
    elif pin13.read_digital():
        display.show("E")
        synth.play_note("E")
    elif pin15.read_digital():
        display.show("F")
        synth.play_note("F")
    elif pin16.read_digital():
        display.show("G")
        synth.play_note("G")
    elif pin19.read_digital():
        #ups tempo
        display.show(Image.NORTH)
    elif pin20.read_digital():
        #downs tempo
        display.show(Image.SOUTH)
    elif button_a.is_pressed():
        synth.down_octave(1)
        display.show(str(synth.octave))
        synth.play_note("C")
        sleep(100)
    elif button_b.is_pressed():
        synth.up_octave(1)
        display.show(str(synth.octave))
        synth.play_note("C")
        sleep(100)
    else:
        display.show(Image.ASLEEP)
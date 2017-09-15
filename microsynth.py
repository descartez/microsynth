# imports microbit library
from microbit import *

# imports music library
import music

class Synth():
    def __init__(self):
        self.sustain = 4
        self.tempo = 100


    def set_octave(self, value):
        self.octave = value

    def set_sustain(self, value):
        self.sustain = value

    def play_note(self, note):
        music.play((str(note) ":" + str(self.sustain)))

    def play_pitch(self, freq, sustain):
        music.pitch(freq, sustain)


synth = Synth()

jingle = ["C4:4","D4:4","E5:4","C6:4"]
notes = [
         "C3",
         "D3",
         "E3",
         "F3",
         "G3",
         "A3",
         "B3",
         "C4",
         "D4",
         "E4",
         "F4",
         "G4",
         "A4",
         "B4",
         ]

music.set_tempo(ticks=16, bpm=synth.tempo)

# starting jingle
music.play(jingle)

while True:
    note_index = int((pin1.read_analog() / 1023) * 13)
    if pin2.read_digital():
        synth.play_note(notes[note_index])
    elif pin3.read_digital():
        synth.play_pitch(pin1.read_analog(), synth.sustain)
    elif button_a.is_pressed():
        sustain = int((pin1.read_analog() / 1023) * 8)
        synth.set_sustain(int((pin1.read_analog() / 1023) * 8))
    else:
        display.show(Image.HEART_SMALL)
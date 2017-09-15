# imports microbit library
from microbit import *

# imports music library
import music

class Synth():
    def __init__(self):
        self.octave = 4
        self.sustain = 4
        self.tempo = 100


    def set_octave(self, value):
        self.octave = value

    def set_sustain(self, value):
        self.sustain = value

    def play_note(self, note):
        music.play((str(note) + str(self.octave) + ":" + str(self.sustain)))

synth = Synth()

jingle = ["C4:4","D4:4","E5:4","C6:4"]
notes = ["C","D","E","F","G","A","B"]

music.set_tempo(ticks=16, bpm=synth.tempo)

# starting jingle
music.play(jingle)

while True:
    # octave control
    note_index = int((pin1.read_analog() / 1023) * 6)
    display.show(str(note_index))
    if button_a.is_pressed():
        synth.play_note(notes[note_index])
    if button_b.is_pressed():
        sustain = int((pin1.read_analog() / 1023) * 8)
        synth.set_sustain(int((pin1.read_analog() / 1023) * 8))
# imports microbit library
from microbit import *

# imports music library
import music

class Synth():
    def __init__(self):
        self.octave = 3
        self.sustain = 4
        self.tempo = 100
        self.musical = True
        self.notes = [
         "C" + str(self.octave),
         "D" + str(self.octave),
         "E" + str(self.octave),
         "F" + str(self.octave),
         "G" + str(self.octave),
         "A" + str(self.octave),
         "B" + str(self.octave),
         ]

    def construct_notes(self):
        self.notes = [
         "C" + str(self.octave),
         "D" + str(self.octave),
         "E" + str(self.octave),
         "F" + str(self.octave),
         "G" + str(self.octave),
         "A" + str(self.octave),
         "B" + str(self.octave),
         ]

    def set_octave(self, value):
        self.octave = value
        self.construct_notes()

    def set_sustain(self, value):
        self.sustain = value

    def play_note(self, note, pitch=""):
        music.play((str(note) + ":" + str(self.sustain)))

    def play_pitch(self, freq, sustain):
        music.pitch(freq, sustain)

    def switch_mode(self):
        if self.musical == False:
            self.musical = True
        else:
            self.musical = False



synth = Synth()

jingle = ["C4:4","D4:4","E5:4","C6:4"]

music.set_tempo(ticks=16, bpm=synth.tempo)

# starting jingle
music.play(jingle)

while True:
    note_index = int((pin1.read_analog() / 1023) * 6)
    octave = int((pin4.read_analog() / 1023) * 7)
    tempo = int((pin10.read_analog() / 1023) * 360)
    pitch = pin1.read_analog()


    if button_a.was_pressed():
        synth.switch_mode()

    if synth.musical == True:
        if (pin1.read_analog() > 8):
            display.show(Image.HEART)
            music.set_tempo(ticks=16, bpm=tempo)
            synth.set_octave(octave)
            synth.play_note(synth.notes[note_index])
        elif pin3.read_digital():
            synth.play_pitch(pitch, synth.sustain)
        else:
            display.show(Image.HEART_SMALL)
    else:
        if (pin1.read_analog() > 8):
            display.show(Image.HAPPY)
            synth.play_pitch(pitch, synth.sustain)
        else:
            display.show(Image.MEH)

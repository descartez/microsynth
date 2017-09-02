# imports microbit library
from microbit import *

# imports music library
import music

class Sequencer():
    def __init__(self):
        self.sequence = []
        self.current_note_index = 0
        self.notes = ["A","B","C","D","E","F"]

    def play_sequence(self):
        music.play(self.sequence, loop=False)

    def add_note(self):
        self.sequence.append(self.notes[self.current_note_index])

    def progress_note(self):
        display.show(str(self.notes[self.current_note_index]))
        music.play((str(self.notes[self.current_note_index])))
        if self.current_note_index < 5:
            self.current_note_index +=1
        else:
            self.current_note_index = 0

sequencer = Sequencer()

music.reset()

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        sequencer.play_sequence()
    elif button_a.is_pressed():
        sequencer.add_note()
    elif button_b.is_pressed():
        sequencer.progress_note()
    else:
        display.show(str(sequencer.notes[sequencer.current_note_index]))

# sequencer runs out of memory, can't hold more than a few notes
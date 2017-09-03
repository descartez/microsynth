from microbit import *

# imports music library
import music

tune = ["E3:1", "E3:1", "E3:1", "D3:2", "G3:2", "E3:1", "F3:2", "E3:1", "D3:1", "C3:2", "C3:2"]

music.set_tempo(ticks=4, bpm=60)
while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        music.play(tune)
    else:
        display.show(Image.ASLEEP)
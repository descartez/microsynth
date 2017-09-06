# imports microbit library
from microbit import *

# imports music library
import music

class Drums():
    def __init__(self):
        self.frequency_interval = 50

    def freq_up(self):
        if self.frequency_interval < 400:
            self.frequency_interval += 25
        else:
            self.frequency_interval = 450

    def freq_down(self):
        if self.frequency_interval > 100:
            self.frequency_interval -= 25
        else:
            self.frequency_interval = 50


    def play_drums(self):
        while True:
            if button_a.is_pressed() or button_b.is_pressed():
                break
            else:
                music.play("G0:1")
                display.show(Image.HEART)
                sleep(100)
                display.show(Image.HEART_SMALL)



drums = Drums()

jingle = ["C4:4","D4:4","E5:4","C6:4"]
music.play(jingle)

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        # plays drums
        drums.play_drums()
    if button_a.is_pressed():
        display.show(Image.ARROW_S)
        # freq down
        drums.freq_down()
        music.set_tempo(ticks=16, bpm=drums.frequency_interval)
    elif button_b.is_pressed():
        display.show(Image.ARROW_N)
        # freq up
        drums.freq_up()
        music.set_tempo(ticks=16, bpm=drums.frequency_interval)
    else:
        display.show(Image.HEART_SMALL)
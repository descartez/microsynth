# imports microbit library
from microbit import *

# imports music library
import music

class Drums():
    def __init__(self):
        self.frequency_interval = 50

    def freq_up(self):
        if self.frequency_interval < 400:
            self.frequency_interval += 50
        else:
            self.frequency_interval = 450

    def freq_down(self):
        if self.frequency_interval > 100:
            self.frequency_interval -= 50
        else:
            self.frequency_interval = 50


    def play_drums(self):
        while True:
            if button_a.is_pressed():
                break
            else:
                music.play("G0:1")
                sleep(self.frequency_interval)
                display.show(Image.HEART)
                sleep(self.frequency_interval)
                display.show(Image.HEART_SMALL)



drums = Drums()

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        # plays drums
        drums.play_drums()
    if button_a.is_pressed():
        # freq down
        drums.freq_down()
    elif button_b.is_pressed():
        # freq up
        drums.freq_up()
    else:
        display.show(Image.HEART_SMALL)
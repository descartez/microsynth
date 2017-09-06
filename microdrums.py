# imports microbit library
from microbit import *

# imports music library
import music

while True:
    if button_a.is_pressed():
        music.play("G0:1")
        sleep(100)
        display.show(Image.HEART)
    elif button_b.is_pressed():
        music.play("G0:1")
        sleep(300)
        display.show(Image.HEART)
    else:
        display.show(Image.HEART_SMALL)
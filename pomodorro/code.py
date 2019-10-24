import time
import board
from digitalio import DigitalInOut, Direction, Pull
import neopixel

pixels = neopixel.NeoPixel(board.A0, 5, brightness=.02, auto_write=True)

button_c = DigitalInOut(board.A2) #pin0 on the board
button_c.direction = Direction.INPUT
button_c.pull = Pull.UP

def blinkRest():
    count = 0
    while (count < 5):
        for i in range(0,5):
            pixels[i] = (0, 100, 0)
            time.sleep(.5)
        for i in range(0,5):
            pixels[i] = (0, 0, 0)
            time.sleep(.5)
        count+=1

while True:
    buttonClicked = not button_c.value
    if buttonClicked:
        for i in range(0,5):
            pixels[i] = (100, 0, 0)
            time.sleep(5)
        
        blinkRest()
        
        for i in range(0,5):
            pixels[i] = (0,0,0)
    time.sleep(.2)

#!/usr/bin/python3
""" Example of the Wargames' WOPR 8x8 LED matrix dispplay class """

from threading import Lock

from Adafruit_Python_LED_Backpack.Adafruit_LED_Backpack import BicolorMatrix8x8

from led8x8wopr.led8x8wopr import Led8x8Wopr

if __name__ == '__main__':
    LOCK = Lock()
    DISPLAY = BicolorMatrix8x8.BicolorMatrix8x8()
    WOPR = Led8x8Wopr(DISPLAY, LOCK)
    while True:
        WOPR.display()
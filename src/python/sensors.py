#!/usr/bin/env python
import sys, time

def run():
    # Moisture sensor
    INPUT_MOISTURE = 4
    GPIO.setup(INPUT_MOISTURE, GPIO.IN)  # Set our input pin to be an input
    while True:
        print GPIO.input(INPUT_MOISTURE)
        time.sleep(1)

try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM) # Set's GPIO pins to BCM GPIO numbering

    run()
except RuntimeError:
    print("Error importing RPi.GPIO!  sudo required")
    sys.exit(1)

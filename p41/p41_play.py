# T.Knoll, 02-2024, GPLv3.0  

import RPi.GPIO as GPIO
import time

# ---------------------------------
# RaspberryPi IO pins
# ---------------------------------
# Read the RasPi docs to find the pins on the board
# Output pins
playclockpin = 21
# Inpute pins

# ---------------------------------
# Init of the IO pins
# ---------------------------------
GPIO.setmode(GPIO.BCM)
GPIO.setup(playclockpin, GPIO.OUT)

# ---------------------------------
# Some variables 
# ---------------------------------
# Wait time t0 between every pin toggle operation
t0 = 0.5

# ---------------------------------
# Loop to play the 8x8 Mem
# ---------------------------------
while True:
        GPIO.output(playclockpin, GPIO.HIGH)
        time.sleep(t0)
        GPIO.output(playclockpin, GPIO.LOW)
        time.sleep(t0)

# T.Knoll, 02-2024, GPLv3.0  

import RPi.GPIO as GPIO
import time

# ---------------------------------
# RaspberryPi IO pins
# ---------------------------------
# Read the RasPi docs to find the pins on the board
# Output pins
datapin = 18
clockpin = 23
# Input pins

# ---------------------------------
# Init of the IO pins
# ---------------------------------
GPIO.setmode(GPIO.BCM)
GPIO.setup(datapin, GPIO.OUT)
GPIO.setup(clockpin, GPIO.OUT)

# ---------------------------------
# Some variables 
# ---------------------------------
# 64 Bits as an array to shift into the 8x8 Mem.
# This should play "THORSTEN" on a 8-seg display.
bitarray = [0,1,0,1,0,1,0,0,\
            0,1,1,1,1,0,1,1,\
            0,1,1,1,1,0,0,0,\
            0,1,1,0,1,1,0,1,\
            0,1,0,1,0,0,0,0,\
            0,1,0,1,1,1,0,0,\
            0,1,1,1,0,1,0,0,
            0,1,1,1,1,0,0,0]
# Wait time t0 between every pin toggle operation
t0 = 0.01

# ---------------------------------
# Loop to shift the bitarray into the 8x8 Mem
# ---------------------------------
for b in bitarray:
    if b == 0:
        GPIO.output(clockpin, GPIO.LOW)
        time.sleep(t0)
        GPIO.output(datapin, GPIO.LOW)
        time.sleep(t0)
        GPIO.output(clockpin, GPIO.HIGH)
        time.sleep(t0)
        GPIO.output(clockpin, GPIO.LOW)
    else:
        GPIO.output(clockpin, GPIO.LOW)
        time.sleep(t0)
        GPIO.output(datapin, GPIO.HIGH)
        time.sleep(t0)
        GPIO.output(clockpin, GPIO.HIGH)
        time.sleep(t0)
        GPIO.output(clockpin, GPIO.LOW)

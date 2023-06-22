#-------------------------------------------------------------------------------
# Name:        gpio.py
# Purpose:
#
# Author:      Quad
#
# Created:     09/04/2023
# Copyright:   (c) Quad 2023
# Licence:     CLOSED
#-------------------------------------------------------------------------------

#IMPORTS
import RPi.GPIO as GPIO
import time 

GPIO.setwarnings(False)

class Gpio:
    def __init__(self):
        #PIN MAPPING FOR THE RASPBERRY
        #playsound('music/background.mp3', block=False)
        self.contact = 4
        self.red_led = 18
        self.green_led = 23
        self.config()
    def config(self):
        #SETMODE & DIRECTION FOR THE GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.contact, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.red_led, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.green_led, GPIO.OUT, initial=GPIO.HIGH)
    

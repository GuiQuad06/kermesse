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
from playsound import playsound 

GPIO.setwarnings(False)
playsound('music/background.mp3', block=False)

# Event : Eteindre LED verte / Mettre la LED rouge pendant 2 sec, son "tu as perdu"
def contact_callback(channel):
    GPIO.remove_event_detect(channel)
    #print("Event s'est produit sur" + str(channel) )
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)
    playsound('music/gameover.wav')
    #time.sleep(2)
    Gpio()

class Gpio:
    def __init__(self):
        #PIN MAPPING FOR THE RASPBERRY
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
        GPIO.add_event_detect(self.contact, GPIO.FALLING, callback=contact_callback)
    

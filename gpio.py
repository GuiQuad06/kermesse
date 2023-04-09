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

#PIN MAPPING FOR THE RASPBERRY
#Besoin : un gpio pour le conact (gpio 4), un gpio pour le led verte (gpio 23) et un pour la led rouge (gpio 18)
#PIN_CONTACT = 4
#PIN_RED_LED = 18
#PIN_GREEN_LED = 23

# Event : Eteindre LED verte / Mettre la LED rouge pendant 2 sec, son "tu as perdu"
def contact_callback(channel):
    print("Event s'est produit sur" + channel )
    Gpio.game_over()

#SETMODE & DIRECTION FOR THE GPIO
#GPIO.setmode(GPIO.BCM)

#GPIO.setup(PIN_CONTACT, GPIO.IN)
#GPIO.setup(PIN_RED_LED, GPIO.OUT)
#GPIO.setup(PIN_GREEN_LED, GPIO.OUT)

#GPIO.add_event_detect(PIN_CONTACT, GPIO.RISING, callback=contact_callback)

class Gpio:
    def __init__(self):
        self.contact = 4
        self.red_led = 18
        self.green_led = 23
        self.config()
    def config(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.contact, GPIO.IN)
        GPIO.setup(self.red_led, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.green_led, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.add_event_detect(self.contact, GPIO.RISING, callback=contact_callback)
    def game_over(self):
        GPIO.output(self.red_led, GPIO.HIGH)
        GPIO.output(self.green_led, GPIO.LOW)
        time.sleep(2)
        self.config()
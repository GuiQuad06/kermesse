#-------------------------------------------------------------------------------
# Name:        kermesse.py
# Purpose:
#
# Author:      Quad
#
# Created:     09/04/2023
# Copyright:   (c) Quad 2023
# Licence:     CLOSED
#-------------------------------------------------------------------------------

#IMPORTS
from gpio import *
import time
import tkinter as tk
from tkinter import *
from threading import Thread

Gpio()

class check_contact(Thread):

    def __init__(self, labelText):
        Thread.__init__(self)
        self.labelText = labelText
        self.tries = 5

    def checkloop(self):
        while True:
            if GPIO.input(4) == 1:
                playsound('music/gameover.wav')
                GPIO.output(18, GPIO.HIGH)
                GPIO.output(23, GPIO.LOW)
                if self.tries > 0:
                    self.labelText.set(self.tries)
                    print("aouch !")
                    self.tries = self.tries - 1
                else:
                    self.labelText.set("GAME OVER")
                    print("game over")
                    self.tries = 5
                time.sleep(0.5)
                while GPIO.input(4) == 1: pass

#Création de l'objet Tkinter
window = Tk()

label_text = StringVar()
display = Label(window, textvariable=label_text) 
display.config(font=('Helvetica', 100, 'bold'))
display.pack(fill = BOTH, expand = True)
window.title("LABYRINTHE 3000") 

#Définition du thread qui poll l'action du contact
contact_handler = check_contact(label_text)
contact = Thread(target=contact_handler.checkloop)
contact.start()

#Ouverture de la fenêtre avant la boucle du jeu
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d" % (w, h))
open
window.mainloop()


def main():
    pass

if __name__ == '__main__':
    main()

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

def main():
    pass
    # Init : configure les gpios, met la musique de fond, allume la LED
    Gpio()

    while True:
        # Boucle infinie : Attends un event + sleep
        time.sleep(0.5)

if __name__ == '__main__':
    main()

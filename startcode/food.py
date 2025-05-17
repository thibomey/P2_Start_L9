import pygame
from snake import veld_grootte
#import snake
import random

kleur_voedsel = (255, 0 ,0)

class Food:
    def __init__(self, breedte, hoogte):
        self.breedte = breedte
        self.hoogte = hoogte
        self.plaats = kleur_voedsel
    def plaats_voedsel(self):
        self.x = round(random.randrange(0, self.breedte - veld_grootte)/veld_grootte * veld_grootte
        self.y = round(random.randrange(0, self.breedte - veld_grootte)/veld_grootte * veld_grootte

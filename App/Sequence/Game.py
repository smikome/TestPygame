import pygame
from pygame.locals import *
from Fwk.SequenceBase import *
from Fwk.Screen import *

class Game(SequenceBase):
    def __init__(self):
        pass

    def Enter(self):
        print("Game.py Enter")
        Screen.Instance().set_bg_color((0, 0, 0))
        pass

    def Exit(self):
        print("Game.py Exit")
        pass

    def Update(self):
        pass
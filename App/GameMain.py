import pygame
from pygame.locals import *
from Fwk.SequenceManager import *
from App.Sequence.Title import *

class GameMain:
    def __init__(self):
        title = Title()
        SequenceManager.Instance().Change(title)

    def Update(self):
        SequenceManager.Instance().Update()

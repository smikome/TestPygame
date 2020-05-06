import pygame
from pygame.locals import *


class Transform:
    def __init__(self):
        self.position = (0, 0)
        self.angleY = 0
        self.scale = (1, 1)

import pygame
from pygame.locals import *


class Screen:
    @classmethod
    def Instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.__color = (0, 0, 0)
        self.__screen = pygame.display.set_mode((640, 480))
        self.__screen.fill(self.__color)

    def get_screen(self):
        return self.__screen

    def set_bg_color(self, color):
        self.__color = color

    def Update(self):
        pygame.display.update()
        pygame.display.flip()
        self.__screen.fill(self.__color)



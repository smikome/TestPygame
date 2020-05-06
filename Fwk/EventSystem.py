import pygame
from pygame.locals import *

class EventSystem:

    @classmethod
    def Instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.__event = pygame.event.get()
        pass

    def Update(self):
        self.__event = pygame.event.get()

    def get_event(self):
        return self.__event

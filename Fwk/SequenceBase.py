import pygame
from pygame.locals import *
from abc import ABCMeta, abstractmethod


class SequenceBase:
    def __init__(self):
        pass

    @abstractmethod
    def Enter(self):
        pass

    @abstractmethod
    def Exit(self):
        pass

    @abstractmethod
    def Update(self):
        pass
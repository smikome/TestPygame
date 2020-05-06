import pygame
from pygame.locals import *


class SequenceManager:
    @classmethod
    def Instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.currentSequence = None
        pass

    def Change(self, sequence):
        if self.currentSequence is not None:
            self.currentSequence.Exit()
            del self.currentSequence
        self.currentSequence = sequence
        self.currentSequence.Enter()

    def Update(self):
        if self.currentSequence is None:
            return
        self.currentSequence.Update()


import pygame
from pygame.locals import *
from Fwk.SequenceManager import *
from Fwk.SequenceBase import *
from Fwk.UI.Button import *
from App.Sequence.Game import *

class Title(SequenceBase):
    def __init__(self):
        pass

    def Enter(self):
        print("Title.py Enter")
        Screen.Instance().set_bg_color((255, 255, 255))
        self.__button_test = Button().set_rect(pygame.Rect(80, 100, 200, 80)).set_color((127, 192, 222))
        self.__button_test.set_on_click_button(self.test)
        self.__button_go_game = Button().set_rect(pygame.Rect(360, 100, 200, 80)).set_color((0, 127, 255))
        self.__button_go_game.set_on_click_button(self.go_game)
        pass

    def Exit(self):
        print("Title.py Exit")
        pass

    def Update(self):
        self.__button_test.Update()
        self.__button_go_game.Update()
        pass

    def test(self):
        print("testだよ")

    def go_game(self):
        next = Game()
        SequenceManager.Instance().Change(next)


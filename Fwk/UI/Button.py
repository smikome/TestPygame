import pygame
from pygame.locals import *
import sys
from Fwk.UI.UIParts import *
from Fwk.Screen import *
from Fwk.EventSystem import *


class Button(UIParts):
    def __init__(self):
        self.__rect = pygame.Rect(0, 0, 0, 0)
        self.__color = (255, 255, 255)
        self.__onClickButton = None

    def set_rect(self, rect):
        self.__rect = rect
        return self

    def set_color(self, color):
        self.__color = color
        return self

    def set_on_click_button(self, callback):
        self.__onClickButton = callback
        return self

    def Update(self):
        super(Button, self).Update()
        pygame.draw.rect(Screen.Instance().get_screen(), self.__color, self.__rect)
        for event in EventSystem.Instance().get_event():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.__rect.collidepoint(event.pos):
                    if self.__onClickButton is not None:
                        self.__onClickButton()

import sys
import pygame
from pygame.locals import *
from Fwk.Screen import *
from Fwk.EventSystem import *
from App.GameMain import *

BLACK = (0, 0, 0)
pygame.init()
myclock = pygame.time.Clock()

finish = 0
gameMain = GameMain()

while finish == 0:
    EventSystem.Instance().Update()
    for event in EventSystem.Instance().get_event():
        if event.type == pygame.QUIT:
            finish = 1
    gameMain.Update()
    Screen.Instance().Update()
    myclock.tick(60)
pygame.quit()
sys.exit()

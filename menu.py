# comment
from pygame import *
import pygame

import shooter_game
pygame.init()
windows = pygame.display.set_mode((700,500))
FPS = pygame.time.Clock()
fon = pygame.image.load('galaxy.jpg')
fon = pygame.transform.scale(fon,(700,500))
btn = pygame.Rect(250,200,200,50)
text_btn = pygame.font.Font(None,35).render('Start',True,(255,255,255))
run = True
while run:
    windows.blit(fon,(0,0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            shooter_game.game()
            pygame.QUIT()

    pygame.draw.rect(windows,(22,66,168),btn)
    windows.blit(text_btn,(320,210))
    pygame.display.update()
    FPS.tick(60)

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import sys
font = pygame.font.Font(None,30)
import time

def draw_gameover(bg):
            
    pygame.mixer.music.load("image/game_over.mp3")
    pygame.mixer.music.play(0)
    clock = pygame.time.Clock()

    from Dateclass import para

    bg.fill((0,0,0))
    sur = font.render("Game Over!",True,(96,96,96))
    bg.blit(sur,[300,320])
    pygame.display.update()

    while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            key = pygame.key.get_pressed()
            if key[pygame.K_w] == 1:
                  pygame.mixer.music.stop()
                  break
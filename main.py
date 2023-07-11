from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import sys
import random
from back_scroll import draw,move_player,draw_boss
from startbg import start_bg
from stair import put_stair,first_point,stair_check
import time

font = pygame.font.Font(None,30)
white = (96,96,96)
black = (0,0,0)


def main():
    pygame.init()
    pygame.display.set_caption("pygame")
    screen = pygame.display.set_mode((720,720))
    clock = pygame.time.Clock()
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                para.savefile()
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    para.savefile()
                    pygame.quit()
                    sys.exit()
        
        start_bg(screen)
        from Dateclass import para
        if para.stair == "stairoff":
            put_stair()
            first_point()
            para.stair = "stairon"
        pygame.mixer.music.load("image/20230528-Shion.mp3")
        pygame.mixer.music.play(0)

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    para.savefile()
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        para.savefile()
                        pygame.quit()
                        sys.exit()
                
            stair_check(screen)
            if para.stair_now == 5:
                para.pl_x,para.pl_y = 15,15
                para.savefile()
                break
            else:
                draw(screen)
                move_player(para.pl_y,para.pl_x)
                pygame.display.update()
                clock.tick(30)
        
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    para.savefile()
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        para.savefile()
                        pygame.quit()
                        sys.exit()

            draw_boss(screen)
            move_player(para.pl_y,para.pl_x)
            pygame.display.update()
            clock.tick(30)
            break


if __name__ == '__main__':
    main()
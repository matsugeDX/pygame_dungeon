import pygame
import sys
import time
from map_maker import make_map

black = (0,0,0)
white = (96,96,96)
pygame.init()
font = pygame.font.Font(None,30)

def start_bg(bg):

        from Dateclass import para

        se_select = pygame.mixer.Sound("image/deci1.mp3")
        se_deci = pygame.mixer.Sound("image/deci2.mp3")
        point = 0
        bg.fill(black)
        sur = font.render("Magic Game",True,white)
        bg.blit(sur,[300,240])
        sur = font.render("New Game",True,white)
        bg.blit(sur,[300,360])
        sur = font.render("Continue",True,white)
        bg.blit(sur,[300,480])
        clock = pygame.time.Clock()
        pygame.mixer.music.load("image/PerituneMaterial_ice_Cave.mp3")
        pygame.mixer.music.play(0)
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                para.savefile()
                                pygame.quit()
                                sys.exit()
                
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                        para.avefile()
                                        pygame.quit()
                                        sys.exit()
                key = pygame.key.get_pressed()
                if key[pygame.K_s] == 1:
                        se_select.play()
                        point = 1
                if key[pygame.K_w] == 1:
                        se_select.play()
                        point = 0
                if point == 0:
                        bg.fill(black)
                        sur = font.render("Magic Game",True,white)
                        bg.blit(sur,[300,240])
                        sur = font.render("New Game",True,white)
                        bg.blit(sur,[300,360])
                        sur = font.render("Continue",True,white)
                        bg.blit(sur,[300,480])
                        sur = font.render("->",True,white)
                        bg.blit(sur,[200,360])
                else:
                        bg.fill(black)
                        sur = font.render("Magic Game",True,white)
                        bg.blit(sur,[300,240])
                        sur = font.render("New Game",True,white)
                        bg.blit(sur,[300,360])
                        sur = font.render("Continue",True,white)
                        bg.blit(sur,[300,480])
                        sur = font.render("->",True,white)
                        bg.blit(sur,[200,480])
                if key[pygame.K_SPACE] == 1:
                        pygame.mixer.music.stop()
                        se_deci.play()
                        if point == 0:
                                para.get_exp = 0
                                para.lv_up = 150
                                para.lv = 1
                                para.pl_x = 9
                                para.pl_y = 9
                                para.room = make_map()
                                para.stair = "stairoff"
                                para.stair_now = 1
                                break
                        else:
                                file = open("save.txt","r")
                                rl = file.readlines()
                                file.close()
                                para.get_exp = int(rl[0].strip("\n"))
                                para.lv_up = int(rl[1].strip("\n"))
                                para.lv = int(rl[2].strip("\n"))
                                para.pl_x = int(rl[3].strip("\n"))
                                para.pl_y = int(rl[4].strip("\n"))
                                para.room = eval(rl[5].strip("\n"))
                                para.stair = (rl[6].strip("\n"))
                                break
                pygame.display.update()
                clock.tick(30)
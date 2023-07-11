from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import sys
import random
from map_maker import room_w,room_h,room,cyan,gray,make_map
from battle_scene import battle_count,battle_boss
import time

screen = pygame.display.set_mode((720,720))
font = pygame.font.Font(None,30)

floor1 = pygame.image.load("image/sougen30.png")
wall1= pygame.image.load("image/wall30.png")
char1 = pygame.image.load("image/char30.png")
stair = pygame.image.load("image/stair.png")

black = (0,0,0)

def draw(bg):
    bg.fill(black)

    from Dateclass import para

    for y in range(-6,6):
        for x in range(-6,6):
            X,Y = (x+6)*60,(y+6)*60
            dx,dy = para.pl_x+x,para.pl_y+y
            if 0 <= dx < room_w and 0 <= dy < room_h:
                if para.room[dy][dx] == 0:
                    bg.blit(floor1,[X,Y])
                if para.room[dy][dx] == 9:
                    bg.blit(wall1,[X,Y])
                if para.room[dy][dx] == 3:
                    bg.blit(stair,[X,Y])
            if x == 0 and y == 0:
                if para.room[dy][dx] != 9:
                    bg.blit(char1,[X,Y])
                '''else:
                    para.pl_x += 1
                    para.pl_y += 1'''
    sur = font.render("Lv "+str(para.lv),True,black)
    bg.blit(sur,[0,0])
    sur = font.render("{},{}".format(para.pl_y,para.pl_x),True,black)
    bg.blit(sur,[600,600])

    '''for y in range(-12,12):
        for x in range(-12,12):
            X,Y = (x+12)*30,(y+12)*30
            dx,dy = para.pl_x+x,para.pl_y+y
            if 0 <= dx < room_w and 0 <= dy < room_h:
                if para.room[dy][dx] == 0:
                    bg.blit(floor1,[X,Y])
                if para.room[dy][dx] == 9:
                    bg.blit(wall1,[X,Y])
                if para.room[dy][dx] == 3:
                    bg.blit(stair,[X,Y])
            if x == 0 and y == 0:
                if para.room[dy][dx] != 9:
                    bg.blit(char1,[X,Y])
                else:
                    para.pl_x += 1
                    para.pl_y += 1
    sur = font.render("Lv "+str(para.lv),True,black)
    bg.blit(sur,[0,0])'''

def draw_boss(bg):
    bg.fill(black)

    from Dateclass import para

    for y in range(-6,6):
        for x in range(-6,6):
            X,Y = (x+6)*60,(y+6)*60
            dx,dy = para.pl_x+x,para.pl_y+y
            if 0 <= dx < 29 and 0 <= dy < 29:
                if para.room[dy][dx] == 0:
                    bg.blit(floor1,[X,Y])
                if para.room[dy][dx] == 9:
                    bg.blit(wall1,[X,Y])
            if x == 0 and y == 0:
                if para.room[dy][dx] != 9:
                    bg.blit(char1,[X,Y])
                '''else:
                    para.pl_x += 1
                    para.pl_y += 1'''
    sur = font.render("Lv "+str(para.lv),True,black)
    bg.blit(sur,[0,0])
    pygame.display.update()
    time.sleep(2)
    battle_boss(bg)


def move_player(y,x): # 主人公の移動
    
    from Dateclass import para
    
    key = pygame.key.get_pressed()
    if key[pygame.K_w] == 1:
        if para.room[y-1][x] != 9: para.pl_y  -= 1
        d = random.randint(0,999)
        if d < -1:
            battle_count(screen)
    if key[pygame.K_s] == 1:
        if para.room[y+1][x] != 9: para.pl_y += 1
        d = random.randint(0,999)
        if d < -1:
            battle_count(screen)
    if key[pygame.K_a] == 1:
        if para.room[y][x-1] != 9: para.pl_x -= 1
        d = random.randint(0,999)
        if d < -1:
            battle_count(screen)
    if key[pygame.K_d] == 1:
        if para.room[y][x+1] != 9: para.pl_x += 1
        d = random.randint(0,999)
        if d < -1:
            battle_count(screen)
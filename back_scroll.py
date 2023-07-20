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
healfloor = pygame.image.load("image/healfloor.png")
meatfloor = pygame.image.load("image/meatfloor.png")

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
                if para.room[dy][dx] == 1:
                    bg.blit(healfloor,[X,Y])
                if para.room[dy][dx] == 2:
                    bg.blit(meatfloor,[X,Y]) 
                if para.room[dy][dx] == 9:
                    bg.blit(wall1,[X,Y])
                if para.room[dy][dx] == 3:
                    bg.blit(stair,[X,Y])
            if x == 0 and y == 0:
                if para.room[dy][dx] != 9:
                    bg.blit(char1,[X,Y])
                    if para.room[dy][dx] == 1:
                        if para.now_hp+5 <= 100:
                            para.now_hp += 5
                        else:
                            para.now_hp = 100
                        para.room[dy][dx] = 0
                    elif para.room[dy][dx] == 2:
                        if para.now_hungry+5 <= 100:
                            para.now_hungry += 5
                        else:
                            para.now_hungry = 100
                        para.room[dy][dx] = 0
                '''else:
                    para.pl_x += 1
                    para.pl_y += 1'''
    sur = font.render("Lv "+str(para.lv),True,black)

    bg.blit(sur,[0,0])
    pygame.draw.rect(bg,(255,138,197),(610,10,100,10))
    nowhp_rate = (para.now_hp/para.max_hp)*100
    pygame.draw.rect(bg,(0,208,0),(610,10,nowhp_rate,10))

    pygame.draw.rect(bg,(128,128,0),(610,30,100,10))
    nowhungry_rate = (para.now_hungry/para.max_hungry)*100
    pygame.draw.rect(bg,(255,255,128),(610,30,nowhungry_rate,10))


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


    '''if key[pygame.K_w] == 1 and key[pygame.K_a] == 1:
        if para.room[y-1][x-1] != 9:
            para.pl_y -= 1
            para.pl_x -= 1 
            para.hungry_cnt += 1
            d = random.randint(0,999)
            if d < -5:
                battle_count(screen)
            if para.hungry_cnt == 50:
                para.hungry_cnt = 0
                if para.now_hungry > 0:
                    para.now_hungry -= 1
            if para.now_hungry == 0:
                para.now_hp -= 1

    if key[pygame.K_w] == 1 and key[pygame.K_d] == 1:
        if para.room[y-1][x+1] != 9:
            para.pl_y -= 1
            para.pl_x += 1 
            para.hungry_cnt += 1
            d = random.randint(0,999)
            if d < -5:
                battle_count(screen)
            if para.hungry_cnt == 50:
                para.hungry_cnt = 0
                if para.now_hungry > 0:
                    para.now_hungry -= 1
            if para.now_hungry == 0:
                para.now_hp -= 1

    if key[pygame.K_s] == 1 and key[pygame.K_a] == 1:
        if para.room[y+1][x-1] != 9:
            para.pl_y += 1
            para.pl_x -= 1 
            para.hungry_cnt += 1
            d = random.randint(0,999)
            if d < -5:
                battle_count(screen)
            if para.hungry_cnt == 50:
                para.hungry_cnt = 0
                if para.now_hungry > 0:
                    para.now_hungry -= 1
            if para.now_hungry == 0:
                para.now_hp -= 1

    if key[pygame.K_s] == 1 and key[pygame.K_d] == 1:
        if para.room[y+1][x+1] != 9:
            para.pl_y += 1
            para.pl_x += 1 
            para.hungry_cnt += 1
            d = random.randint(0,999)
            if d < -5:
                battle_count(screen)
            if para.hungry_cnt == 50:
                para.hungry_cnt = 0
                if para.now_hungry > 0:
                    para.now_hungry -= 1
            if para.now_hungry == 0:
                para.now_hp -= 1

    if (key[pygame.K_w] == 1 and key[pygame.K_a] == 0) or (key[pygame.K_w] == 1 and key[pygame.K_d] == 0):
        if para.room[y-1][x] != 9:
            para.pl_y  -= 1
            para.hungry_cnt += 1
            d = random.randint(0,999)
            if d < -5:
                battle_count(screen)
            if para.hungry_cnt == 50:
                para.hungry_cnt = 0
                if para.now_hungry > 0:
                    para.now_hungry -= 1
            if para.now_hungry == 0:
                para.now_hp -= 1

    if (key[pygame.K_s] == 1 and key[pygame.K_a] == 0) or (key[pygame.K_s] == 1 and key[pygame.K_d] == 0):
        if para.room[y+1][x] != 9:
            para.pl_y += 1
            para.hungry_cnt += 1
            d = random.randint(0,999)
            if d < -5:
                battle_count(screen)
            if para.hungry_cnt == 50:
                para.hungry_cnt = 0
                if para.now_hungry > 0:
                    para.now_hungry -= 1
            if para.now_hungry == 0:
                para.now_hp -= 1

    if (key[pygame.K_a] == 1 and key[pygame.K_w] == 0) or (key[pygame.K_a] == 1 and key[pygame.K_s] == 0):
        if para.room[y][x-1] != 9:
            para.pl_x -= 1
            para.hungry_cnt += 1
            d = random.randint(0,999)
            if d < -5:
                battle_count(screen)
            if para.hungry_cnt == 50:
                para.hungry_cnt = 0
                if para.now_hungry > 0:
                    para.now_hungry -= 1
            if para.now_hungry == 0:
                para.now_hp -= 1

    if (key[pygame.K_d] == 1 and key[pygame.K_w] == 0) or (key[pygame.K_d] == 1 and key[pygame.K_s] == 0):
        if para.room[y][x+1] != 9:
            para.pl_x += 1
            para.hungry_cnt += 1
            d = random.randint(0,999)
            if d < -5:
                battle_count(screen)
            if para.hungry_cnt == 50:
                para.hungry_cnt = 0
                if para.now_hungry > 0:
                    para.now_hungry -= 1
            if para.now_hungry == 0:
                para.now_hp -= 1'''

    if  key[pygame.K_w] == 1:
        if para.room[y-1][x] != 9:
            if not para.move:
                para.pl_y  -= 1

                para.move = True
                para.move_delay = pygame.time.get_ticks() + para.move_delay_time

                para.hungry_cnt += 1
                d = random.randint(0,999)
                if d < -5:
                    battle_count(screen)
                if para.hungry_cnt == 50:
                    para.hungry_cnt = 0
                    if para.now_hungry > 0:
                        para.now_hungry -= 1
                if para.now_hungry == 0:
                    para.now_hp -= 1

    if  key[pygame.K_s] == 1:
        if para.room[y+1][x] != 9:
            if not para.move:
                para.pl_y += 1

                para.move = True
                para.move_delay = pygame.time.get_ticks() + para.move_delay_time

                para.hungry_cnt += 1
                d = random.randint(0,999)
                if d < -5:
                    battle_count(screen)
                if para.hungry_cnt == 50:
                    para.hungry_cnt = 0
                    if para.now_hungry > 0:
                        para.now_hungry -= 1
                if para.now_hungry == 0:
                    para.now_hp -= 1

    if  key[pygame.K_a] == 1:
        if para.room[y][x-1] != 9:
            if not para.move:
                para.pl_x -= 1

                para.move = True
                para.move_delay = pygame.time.get_ticks() + para.move_delay_time

                para.hungry_cnt += 1
                d = random.randint(0,999)
                if d < -5:
                    battle_count(screen)
                if para.hungry_cnt == 50:
                    para.hungry_cnt = 0
                    if para.now_hungry > 0:
                        para.now_hungry -= 1
                if para.now_hungry == 0:
                    para.now_hp -= 1

    if key[pygame.K_d] == 1:
        if para.room[y][x+1] != 9:
            if not para.move:
                para.pl_x += 1

                para.move = True
                para.move_delay = pygame.time.get_ticks() + para.move_delay_time

                para.hungry_cnt += 1
                d = random.randint(0,999)
                if d < -5:
                    battle_count(screen)
                if para.hungry_cnt == 50:
                    para.hungry_cnt = 0
                    if para.now_hungry > 0:
                        para.now_hungry -= 1
                if para.now_hungry == 0:
                    para.now_hp -= 1
    
    if para.move and pygame.time.get_ticks() > para.move_delay:
        para.move = False
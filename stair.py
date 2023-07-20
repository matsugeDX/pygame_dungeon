from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import sys
import random
from Dateclass import para
from map_maker import room_w,room_h,make_map,boss_map
import time

font = pygame.font.Font(None,30)
white = (96,96,96)
black = (0,0,0)

def put_stair(): #階段座標決めおよび階段周りを床
    while True:
        x = random.randint(3,room_w-4)
        y = random.randint(3,room_h-4)
        if para.room[y][x] == 0:
            for ry in range(-1,2):
                for rx in range(-1,2):
                    para.room[ry+y][rx+x] = 0
            para.stair_x = x
            para.stair_y = y
            para.savefile()
            para.room[y][x] = 3 #階段座標
            break

def first_point(): #最初の座標決め
    while True:
        x = random.randint(3,87)
        y = random.randint(3,87)
        if para.room[y][x] == 0:
            para.pl_x = x
            para.pl_y = y
            para.savefile()
            break

def stair_check(bg):
        if para.stair_y == para.pl_y and para.stair_x == para.pl_x:
            para.stair_now += 1
            if para.stair_now == 5:
                para.room = boss_map()
            else:
                bg.fill(black)
                sur = font.render("B {}F".format(para.stair_now),True,white)
                bg.blit(sur,[360,360])
                pygame.display.update()
                time.sleep(2)
                para.room = make_map()
                put_stair()
                first_point()
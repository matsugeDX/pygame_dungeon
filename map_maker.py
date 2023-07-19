from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import sys
import random

cyan = (0,255,255)
gray = (96,96,96)
white = (255,255,255)

map_w = 30
map_h = 30
map = []
for i in range(map_h):
    map.append([0]*map_w)

room_w = map_w*3
room_h = map_h*3
room = []
for i in range(room_h):
    room.append([0]*room_w)

def make_map():
        xp = [0,1,0,-1]
        yp = [-1,0,1,0]

        #mapリセット
        for h in range(map_h):
            for w in range(map_w):
                map[h][w] = 0
        
        #外周を壁にする
        for w in range(map_w):
            map[0][w] = 1
            map[map_h-1][w] = 1
        for h in range(map_h):
            map[h][0] = 1
            map[h][-1] = 1
        
        #棒倒し、柱生成
        for h in range(2,map_h-2,2):
            for w in range(2,map_w-2,2):
                map[h][w] = 1
        
        for h in range(2,map_h-2,2):
            for w in range(2,map_w-2,2):
                d = random.randint(0,3)
                if w > 2:d = random.randint(0,2)
                map[h+yp[d]][w+xp[d]] = 1
        
        for i in range(room_h):
            for j in range(room_w):
                room[i][j] = 9

        for i in range(1,map_h-1):
            for j in range(1,map_w-1):
                dj = j*3+1
                di = i*3+1
                if map[i][j] == 0:
                    if random.randint(0,99) < 30:
                        for s in range(-1,2):
                            for t in range(-1,2):
                                item = random.randint(0,100)
                                if item == 1:
                                    room[di+s][dj+t] = 1
                                elif item == 2:
                                    room[di+s][dj+t] = 2
                                else:
                                    room[di+s][dj+t] = 0
                    else:
                        room[di][dj] = 0
                        if map[i-1][j] == 0:
                            room[di-1][dj] = 0
                        if map[i+1][j] == 0:
                            room[di+1][dj] = 0
                        if map[i][j-1] == 0:
                            room[di][dj-1] = 0
                        if map[i][j+1] == 0:
                            room[di][dj+1] = 0
        
        return room

def boss_map():
    room = []
    for i in range(30):
        room.append([9]*30)
    for i in range(30):
        for j in range(30):
            if 10 <= i <= 20 and 10 <= j <= 20:
                room[i][j] = 0
    return room
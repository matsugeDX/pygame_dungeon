from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import sys
import random
import time
from Dateclass import Date



monstar = pygame.image.load("image/monstar.png")
black = (0,0,0)
point = 0
ene_x,ene_y = 360-monstar.get_width()/2,400-monstar.get_height()
backimg = pygame.image.load("back/pipo-battlebg017b.jpg")
char1 = pygame.image.load("image/char30.png")
imgBT = pygame.image.load("image/cut.png")
bossback = pygame.image.load("back/pipo-battlebg010b.jpg")
boss = pygame.image.load("image/boss.png")
effe_x,effe_y = 360-imgBT.get_width()/2,400-imgBT.get_height()
pygame.init()
font = pygame.font.Font(None,30)

message = [""]*10

pygame.mixer.music.load("image/20230623-Final-Battle.mp3")

def init_message():
    for i in range(10):
        message[i] = ""

def set_message(msg):
    for i in range(10):
        if message[i] == "":
            message[i] = msg
            return
    for i in range(9):
        message[i] = message[i+1]
    message[9] = msg

def draw_msg(bg,txt,x,y,fnt,col):
    sur = fnt.render(txt,True,black)
    bg.blit(sur,[x+1,y+2])
    sur = fnt.render(txt,True,col)
    bg.blit(sur,[x,y])


def battle_scene(bg):
    global point

    key = pygame.key.get_pressed()
    if key[pygame.K_s] == 1:
            if point == 0:
                point = 1
            elif point == 2:
                point = 3
    if key[pygame.K_w] == 1:
            if point == 1:
                point = 0
            elif point == 3:
                point = 2
    if key[pygame.K_d] == 1:
            if point == 0:
                point = 2
            elif point == 1:
                point = 3
    if key[pygame.K_a] == 1:
            if point == 2:
                point = 0
            elif point == 3:
                point = 1

    bg.blit(backimg,[0,0])
    bg.blit(monstar,[ene_x,ene_y])

    sur = font.render("Cut",True,black)
    bg.blit(sur,[200,600])
    sur = font.render("Flame",True,black)
    bg.blit(sur,[200,660])
    sur = font.render("Ice",True,black)
    bg.blit(sur,[400,600])
    sur = font.render("Thunder",True,black)
    bg.blit(sur,[400,660])
    if point == 0:
            sur = font.render("->",True,black)
            bg.blit(sur,[160,600])
    if point == 1:
            sur = font.render("->",True,black)
            bg.blit(sur,[160,660])
    if point == 2:
            sur = font.render("->",True,black)
            bg.blit(sur,[360,600])
    if point == 3:
            sur = font.render("->",True,black)
            bg.blit(sur,[360,660])

    for i in range(10):
        draw_msg(bg,message[i],0,24*i,font,black)

def battle_scene_fin(bg):
    bg.blit(backimg,[0,0])
    for i in range(10):
        draw_msg(bg,message[i],0,24*i,font,black)

def cut(bg):
    se_cut = pygame.mixer.Sound("image/cut.mp3")
    imgBT = pygame.image.load("image/cut.png")
    bg.blit(imgBT,[effe_x,effe_y])
    se_cut.play()
    pygame.display.update()
    time.sleep(0.5)
    bg.blit(backimg,[0,0])
    bg.blit(monstar,[ene_x,ene_y])

def flame(bg):
    se_cut = pygame.mixer.Sound("image/火炎魔法1.mp3")
    imgBT = pygame.image.load("image/flame.png")
    bg.blit(imgBT,[effe_x,effe_y])
    se_cut.play()
    pygame.display.update()
    time.sleep(0.5)
    bg.blit(backimg,[0,0])
    bg.blit(monstar,[ene_x,ene_y])    

def ice(bg):
    se_cut = pygame.mixer.Sound("image/氷魔法で凍結.mp3")
    imgBT = pygame.image.load("image/ice.png")
    bg.blit(imgBT,[effe_x,effe_y])
    se_cut.play()
    pygame.display.update()
    time.sleep(0.5)
    bg.blit(backimg,[0,0])
    bg.blit(monstar,[ene_x,ene_y]) 

def thunder(bg):
    se_cut = pygame.mixer.Sound("image/雷魔法2.mp3")
    imgBT = pygame.image.load("image/thunder.png")
    bg.blit(imgBT,[effe_x,effe_y])
    se_cut.play()
    pygame.display.update()
    time.sleep(0.5)
    bg.blit(backimg,[0,0])
    bg.blit(monstar,[ene_x,ene_y]) 

def battle_count(bg):

    from Dateclass import para

    idx = 10
    timer = 0
    ene_hp = random.randint(100,150)
    exp = ene_hp*10
    my_at = para.lv*10+random.randint(30,50)

    clock = pygame.time.Clock()

    pygame.mixer.music.load("image/20230623-Final-Battle.mp3")
    pygame.mixer.music.play(0)
    
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
        
        timer += 1
        
        if idx == 10:
            if timer == 1:
                set_message("Encount!")
            if timer == 6:
                idx += 1
                timer = 0
        elif idx == 11:
            if timer == 1:
                set_message("Your Turn!")
            if timer == 6:
                idx += 1
                timer = 0
        elif idx == 12:
            if timer == 1:
                set_message("You  Attack!")
                if point == 0:
                    cut(bg)
                    set_message("{} dameges!".format(my_at))
                    ene_hp -= my_at
                    idx += 1
                    timer = 0
                    if ene_hp <= 0:
                        set_message("Enemy Defeated!")
                        set_message("Get {} exp!".format(exp))
                        para.get_exp += exp
                        while para.get_exp >= para.lv_up:
                            para.lv += 1
                            para.get_exp -= para.lv_up
                            para.lv_up *= 3
                        pygame.mixer.music.stop()
                        battle_scene_fin(bg)
                        pygame.display.update()
                        time.sleep(2)
                        init_message()
                        pygame.mixer.music.load("image/20230528-Shion.mp3")
                        pygame.mixer.music.play(0)
                        para.savefile()
                        break
                if point == 1:
                    flame(bg)
                    set_message("{} dameges!".format(my_at))
                    ene_hp -= my_at
                    idx += 1
                    timer = 0
                    if ene_hp <= 0:
                        set_message("Enemy Defeated!")
                        set_message("Get {} exp!".format(exp))
                        para.get_exp += exp
                        while para.get_exp >= para.lv_up:
                            para.lv += 1
                            para.get_exp -= para.lv_up
                            para.lv_up *= 3
                        pygame.mixer.music.stop()
                        battle_scene_fin(bg)
                        pygame.display.update()
                        time.sleep(2)
                        init_message()
                        pygame.mixer.music.load("image/20230528-Shion.mp3")
                        pygame.mixer.music.play(0)
                        para.savefile()
                        break
                if point == 2:
                    ice(bg)
                    set_message("{} dameges!".format(my_at))
                    ene_hp -= my_at
                    idx += 1
                    timer = 0
                    if ene_hp <= 0:
                        set_message("Enemy Defeated!")
                        set_message("Get {} exp!".format(exp))
                        para.get_exp += exp
                        while para.get_exp >= para.lv_up:
                            para.lv += 1
                            para.get_exp -= para.lv_up
                            para.lv_up *= 3
                        pygame.mixer.music.stop()
                        battle_scene_fin(bg)
                        pygame.display.update()
                        time.sleep(2)
                        init_message()
                        pygame.mixer.music.load("image/20230528-Shion.mp3")
                        pygame.mixer.music.play(0)
                        para.savefile()
                        break
                if point == 3:
                    thunder(bg)
                    set_message("{} dameges!".format(my_at))
                    ene_hp -= my_at
                    idx += 1
                    timer = 0
                    if ene_hp <= 0:
                        set_message("Enemy Defeated!")
                        set_message("Get {} exp!".format(exp))
                        para.get_exp += exp
                        while para.get_exp >= para.lv_up:
                            para.lv += 1
                            para.get_exp -= para.lv_up
                            para.lv_up *= 3
                        pygame.mixer.music.stop()
                        battle_scene_fin(bg)
                        pygame.display.update()
                        time.sleep(2)
                        init_message()
                        pygame.mixer.music.load("image/20230528-Shion.mp3")
                        pygame.mixer.music.play(0)
                        para.savefile()
                        break
            if timer == 6:
                timer = 1
        elif idx == 13:
            if timer == 1:
                set_message("Enemy Turn!")
            if timer == 6:
                idx += 1
                timer = 0
        elif idx == 14:
            if timer == 1:
                set_message("Enemy Attack!")
            if timer == 6:
                idx += 1
                timer = 0
        else:
            idx = 11
            timer = 0
        battle_scene(bg)
        pygame.display.update()
        clock.tick(10)

def boss_scene_fin(bg):
    bg.blit(bossback,[0,0])
    for i in range(10):
        draw_msg(bg,message[i],0,24*i,font,black)

def boss_scene(bg):
    global point

    key = pygame.key.get_pressed()
    if key[pygame.K_s] == 1:
            if point == 0:
                point = 1
            elif point == 2:
                point = 3
    if key[pygame.K_w] == 1:
            if point == 1:
                point = 0
            elif point == 3:
                point = 2
    if key[pygame.K_d] == 1:
            if point == 0:
                point = 2
            elif point == 1:
                point = 3
    if key[pygame.K_a] == 1:
            if point == 2:
                point = 0
            elif point == 3:
                point = 1

    bg.blit(bossback,[0,0])
    bg.blit(boss,[ene_x,ene_y])

    sur = font.render("Cut",True,black)
    bg.blit(sur,[200,600])
    sur = font.render("Flame",True,black)
    bg.blit(sur,[200,660])
    sur = font.render("Ice",True,black)
    bg.blit(sur,[400,600])
    sur = font.render("Thunder",True,black)
    bg.blit(sur,[400,660])
    if point == 0:
            sur = font.render("->",True,black)
            bg.blit(sur,[160,600])
    if point == 1:
            sur = font.render("->",True,black)
            bg.blit(sur,[160,660])
    if point == 2:
            sur = font.render("->",True,black)
            bg.blit(sur,[360,600])
    if point == 3:
            sur = font.render("->",True,black)
            bg.blit(sur,[360,660])

    for i in range(10):
        draw_msg(bg,message[i],0,24*i,font,black)

def battle_boss(bg):

    from Dateclass import para

    idx = 10
    timer = 0
    ene_hp = 3000
    exp = ene_hp*10
    my_at = para.lv*100+random.randint(30,50)

    clock = pygame.time.Clock()

    pygame.mixer.music.load("image/メランコリックシンドローム.mp3")
    pygame.mixer.music.play(0)
    
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
        
        timer += 1
        
        if idx == 10:
            if timer == 1:
                set_message("Boss Battle!")
            if timer == 6:
                idx += 1
                timer = 0
        elif idx == 11:
            if timer == 1:
                set_message("Your Turn!")
            if timer == 6:
                idx += 1
                timer = 0
        elif idx == 12:
            if timer == 1:
                set_message("You  Attack!")
                if point == 0:
                    cut(bg)
                    set_message("{} dameges!".format(my_at))
                    ene_hp -= my_at
                    idx += 1
                    timer = 0
                    if ene_hp <= 0:
                        set_message("Boss Defeated!")
                        set_message("Get {} exp!".format(exp))
                        para.get_exp += exp
                        while para.get_exp >= para.lv_up:
                            para.lv += 1
                            para.get_exp -= para.lv_up
                            para.lv_up *= 3
                        pygame.mixer.music.stop()
                        boss_scene_fin(bg)
                        pygame.display.update()
                        time.sleep(2)
                        init_message()
                        para.savefile()
                        break
                if point == 1:
                    flame(bg)
                    set_message("{} dameges!".format(my_at))
                    ene_hp -= my_at
                    idx += 1
                    timer = 0
                    if ene_hp <= 0:
                        set_message("Boss Defeated!")
                        set_message("Get {} exp!".format(exp))
                        para.get_exp += exp
                        while para.get_exp >= para.lv_up:
                            para.lv += 1
                            para.get_exp -= para.lv_up
                            para.lv_up *= 3
                        pygame.mixer.music.stop()
                        boss_scene_fin(bg)
                        pygame.display.update()
                        time.sleep(2)
                        init_message()
                        para.savefile()
                        break
                if point == 2:
                    ice(bg)
                    set_message("{} dameges!".format(my_at))
                    ene_hp -= my_at
                    idx += 1
                    timer = 0
                    if ene_hp <= 0:
                        set_message("Boss Defeated!")
                        set_message("Get {} exp!".format(exp))
                        para.get_exp += exp
                        while para.get_exp >= para.lv_up:
                            para.lv += 1
                            para.get_exp -= para.lv_up
                            para.lv_up *= 3
                        pygame.mixer.music.stop()
                        boss_scene_fin(bg)
                        pygame.display.update()
                        time.sleep(2)
                        init_message()
                        para.savefile()
                        break
                if point == 3:
                    thunder(bg)
                    set_message("{} dameges!".format(my_at))
                    ene_hp -= my_at
                    idx += 1
                    timer = 0
                    if ene_hp <= 0:
                        set_message("Boss Defeated!")
                        set_message("Get {} exp!".format(exp))
                        para.get_exp += exp
                        while para.get_exp >= para.lv_up:
                            para.lv += 1
                            para.get_exp -= para.lv_up
                            para.lv_up *= 3
                        pygame.mixer.music.stop()
                        boss_scene_fin(bg)
                        pygame.display.update()
                        time.sleep(2)
                        init_message()
                        para.savefile()
                        break
            if timer == 6:
                timer = 1
        elif idx == 13:
            if timer == 1:
                set_message("Enemy Turn!")
            if timer == 6:
                idx += 1
                timer = 0
        elif idx == 14:
            if timer == 1:
                set_message("Enemy Attack!")
            if timer == 6:
                idx += 1
                timer = 0
        else:
            idx = 11
            timer = 0
        boss_scene(bg)
        pygame.display.update()
        clock.tick(10)
#!/usr/bin/env python
#coding:utf-8
"""
created on 24.08.2017
author:Leon Lee
User-Agent:{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0'}
"""
import pygame
from pygame import *
from tank_screen import screen
from tank_color import *
import random
class Tank:
    def __init__(self):
        self.width=20
        self.color=None
        self.flag=False
    def draw(self):
        for coor in self.coors:
            pygame.draw.rect(screen,self.color,(coor[0],coor[1],self.width,self.width))
    def move(self):
        pass
    def shoot(self):
        pass
    def death(self):
        pass
    def gen(self):
        pass
    def start(self):
        self.shoot()
        self.move()
        self.draw()
        self.death()
        clean()
        print(len(enemypools))
class TankMy(Tank):
    def __init__(self):
        Tank.__init__(self)
        coor1=290
        coor2=420
        self.width=20
        self.color=red
        self.shoot_coors=[]
        self.coors=[[coor1,coor2],[coor1-self.width,coor2+self.width],[coor1-self.width,coor2+2*self.width],[coor1,coor2+self.width]
            ,[coor1+self.width,coor2+self.width],[coor1+self.width,coor2+2*self.width]]
    def draw(self):
        Tank.draw(self)
        for coor in self.shoot_coors:
            pygame.draw.rect(screen, self.color, (coor[0], coor[1], self.width, self.width))
    def move(self):
        for event in pygame.event.get():
            if event.type==QUIT:
                exit()
            elif event.type==KEYDOWN:
                if event.key==K_LEFT or event.key==K_a:
                    for coor in self.coors:
                        coor[0]-=20
                elif event.key==K_RIGHT or event.key==K_d:
                    for coor in self.coors:
                        coor[0]+=20
                elif event.key==K_j:
                    self.shoot_coors.append(list(self.coors[0]))
    def shoot(self):
        for coor in self.shoot_coors:
            coor[1]-=20
class TankEnemy(Tank):
    count=1
    def __init__(self):
        Tank.__init__(self)
        self.coor1=80*random.randint(1,7)+10
        self.coor2=0
        self.width=20
        self.color=green
        self.coors=[[self.coor1,self.coor2],[self.coor1-self.width,self.coor2-self.width],[self.coor1-self.width,self.coor2-2*self.width],[self.coor1,self.coor2-self.width],
                    [self.coor1+self.width,self.coor2-self.width],[self.coor1+self.width,self.coor2-2*self.width]]
    def move(self):
        for coor in self.coors:
            coor[1]+=10
    def death(self):
        for coor in tank_my.shoot_coors:
            for coor1 in self.coors:
                if coor[0]==coor1[0] and coor[1]==coor1[1]:
                    self.flag=True
                elif self.coors[5][1]==480:
                    self.flag=True
                    # clean_enemy(enemypools)
                    # judge_enemy(enemypools)
    def gen(self):
        enemy_new=TankEnemy()
        enemypools.append(enemy_new)
def enemy_initia():
    tank_enemy1 = TankEnemy()
    tank_enemy2 = TankEnemy()
    tank_enemy3 = TankEnemy()
    enemypools = [tank_enemy1, tank_enemy2, tank_enemy3]
    return enemypools
def clean():
    for enemy in enemypools:
        if enemy.flag==True:
            enemypools.remove(enemy)
            enemy.gen()
if __name__ == '__main__':
    tank_my=TankMy()
    pygame.init()
    fpsClock = pygame.time.Clock()
    enemypools=enemy_initia()
    while True:
        screen.fill(black)
        tank_my.start()
        for enemy in enemypools:
            enemy.start()
        fpsClock.tick(8)
        pygame.display.flip()



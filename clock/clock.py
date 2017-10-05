#!/usr/bin/env python
#coding:utf-8
"""
created on 24.08.2017
author:Leon Lee
"""
import sys,pygame,math,datetime,time
from pygame.locals import *
import os
black=[0,0,0]
red=[255,0,0]
white=[255,255,255]
blue=[0,0,255]
green=[0,255,0]
clock_name='clock.jpg'
clock=pygame.time.Clock()
screen=pygame.display.set_mode((640,480))
dial_plate=pygame.image.load(clock_name).convert()
pygame.display.set_caption('Leon Clock')
class Clock:
    def __init__(self):
        self.x=0
        self.y=0
        self.color=None
    def draw(self):
        pygame.draw.line(screen, self.color, (318, 240), (self.x, self.y))     #  (318, 240) is the position of the center of the clock
    def start(self):
        self.draw()
class SecondHand(Clock):
    def __init__(self,now):                                 #the initial position and color of second hand
        self.x=318 + 167 *  math.sin(math.pi * now.second / 30)
        self.y = 240 - 167 * math.cos(math.pi * now.second / 30)
        self.color=red
class MinuteHand(Clock):
    def __init__(self,now):     #the initial position and color of minute hand
        self.x=318 + 137 * math.sin(math.pi * (now.minute / 30+now.second/1800))
        self.y=240 - 137 * math.cos(math.pi *( now.minute / 30+now.second/1800))
        self.color=blue
class HourHand(Clock):
    def __init__(self,now):
        if now.hour > 12:     #conditions are different 
            self.y = 240 - 107 * math.cos(math.pi * ((now.hour - 12) / 6 + now.minute / 360))
            self.x = 318 + 107 * math.sin(math.pi * ((now.hour - 12) / 6 + now.minute / 360))
        else:
            self.y = 240 - 107 * math.cos(math.pi * (now.hour / 6 + now.minute / 360))
            self.x = 318 + 107 * math.sin(math.pi * (now.hour / 6 + now.minute / 360))
        self.color=green


if __name__ == '__main__':
    pygame.init()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        now = datetime.datetime.now()
        second = SecondHand(now)
        minute = MinuteHand(now)
        hour = HourHand(now)
        screen.fill(white)
        screen.blit(dial_plate, (75, 0))
        second.start()
        minute.start()
        hour.start()
        pygame.display.flip()
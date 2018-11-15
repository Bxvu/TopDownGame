#made by Benthan Vu, sprite classes for game
#sources: goo.gl/2KMivS
import pygame as pg
import random
from pygame.sprite import Sprite
from settings import *
import pygame.math

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((30,40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.vx = 0
        self.vy = 0
        self.rect.x, self.rect.y = (WIDTH / 2, HEIGHT / 2)
        self.ang = 0

    def update(self):
        self.vx = 0
        self.vy = 0
        # self.ang += 1
        #checks if a button is pressed
        # self.image = pg.Surface((30,40))
        # self.rect = self.image.get_rect()
        # self.rect.center = (WIDTH / 2, HEIGHT / 2)
        # self.image = pg.transform.rotate(self.image,self.ang)
        # keys = pg.key.get_pressed()
        # if keys[pg.K_LEFT]:
        #     self.vx = -5
        # if keys[pg.K_RIGHT]:
        #     self.vx = 5        
        # if keys[pg.K_UP]:
        #     self.vy = -5
        # if keys[pg.K_DOWN]:
        #     self.vy = 5

        self.rect.x += self.vx
        self.rect.y += self.vy 

class Platform(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((100,40))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.vx = 0
        self.vy = 0
        self.acceleration = 0.5
        self.falling = False
        self.max_velocity = -25
        self.rect.x = 0
        self.rect.y = 100

    def update(self):
        self.vx = 0
        self.vy = 0
        self.falling = False
        #checks if a button is pressed

        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.vx = 5
        if keys[pg.K_d]:
            self.vx = -5        
        if keys[pg.K_w]:
            self.vy = 5
        if keys[pg.K_s]:
            self.vy = -5

        self.rect.x += self.vx
        self.rect.y += self.vy

class Enemy(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((30,40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.vx = 0
        self.vy = 0
    def update(self):
        self.vx = 0
        self.vy = 0 

        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.vx = 5
        if keys[pg.K_d]:
            self.vx = -5        
        if keys[pg.K_w]:
            self.vy = 5
        if keys[pg.K_s]:
            self.vy = -5
        
        self.rect.x += self.vx
        self.rect.y += self.vy
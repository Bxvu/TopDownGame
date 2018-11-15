#made by Benthan Vu
#sources: goo.gl/2KMivS
import pygame as pg
import random
from settings import *
from sprites import *
import math
import pygame.math

class Game:
    def __init__(self):
        #init game window
        #init pygame and create a window
        pg.init()
        #init sound mixer
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption((TITLE))
        self.clock = pg.time.Clock()
        self.running = True
    def new(self):
        self.all_sprites = pg.sprite.Group()
        #add a player to the group
        self.player = Player()
        self.all_sprites.add(self.player)
        #adds an enemy to the group
        self.enemy = Enemy()
        self.all_sprites.add(self.enemy)
        #call the run method
        self.platform = Platform()
        self.all_sprites.add(self.platform)
        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def update(self):
        # self.enemy_follow()
        self.all_sprites.update()
        # print(pg.sprite.groupcollide(self.all_sprites, self.all_sprites, False, False))

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
    def draw(self):
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass

    def enemy_follow(self):
        if self.enemy.rect.x == self.player.rect.x:
            self.enemy.rect.x += 0
        elif self.enemy.rect.x > self.player.rect.x:
            self.enemy.rect.x += -6 
        elif self.enemy.rect.x < self.player.rect.x:
            self.enemy.rect.x += 6 
        if self.enemy.rect.y == self.player.rect.y:
            self.enemy.rect.y += 0  
        elif self.enemy.rect.y > self.player.rect.y:
            self.enemy.rect.y += -6 
        elif self.enemy.rect.y < self.player.rect.y:
            self.enemy.rect.y += 6
        self.enemy.update()

g = Game()
g.show_go_screen()

while g.running:
    g.new()
    g.show_go_screen()
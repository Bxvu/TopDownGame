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
        self.movement = pg.sprite.Group()
        #add a player to the group
        self.player = Player()
        self.all_sprites.add(self.player)
        #adds an enemy to the group
        self.enemy = Enemy()
        self.all_sprites.add(self.enemy)
        self.movement.add(self.enemy)
        #call the run method
        self.wall = Wall()
        self.all_sprites.add(self.wall)
        self.movement.add(self.wall)
        #call the run method
        self.wall2 = Wall()
        self.wall2.rect.x = 150
        self.wall2.image = pg.transform.rotate(self.wall2.image,90)
        self.all_sprites.add(self.wall2)
        self.movement.add(self.wall2)
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
        if pg.Rect.colliderect(self.wall.rect,self.player.rect) or pg.Rect.colliderect(self.wall2.rect,self.player.rect) == True:  
            if self.enemy.moving and self.wall.moving and self.wall2.moving == "up":
                self.wall.rect.y += -5
                self.wall2.rect.y += -5
                self.enemy.rect.y += -5
            if self.enemy.moving and self.wall.moving and self.wall2.moving == "down":
                self.wall.rect.y += 5
                self.wall2.rect.y += 5
                self.enemy.rect.y += 5
            if self.enemy.moving and self.wall.moving and self.wall2.moving == "left":
                self.wall.rect.x += -5
                self.wall2.rect.x += -5
                self.enemy.rect.x += -5
            if self.enemy.moving and self.wall.moving and self.wall2.moving == "right":
                self.wall.rect.x += 5
                self.wall2.rect.x += 5
                self.enemy.rect.x += 5
            self.all_sprites.update()
        else:
            self.all_sprites.update()
        # print(pg.sprite.spritecollide(self.player, self.all_sprites, False, False))

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
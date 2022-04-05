# -*- coding: utf-8 -*-
"""
the class for all the objects in the game
@author: ZHANG Chenyu
"""

import pygame
from pygame.locals import *

# the class bullet
class Award(pygame.sprite.Sprite):
    def __init__(self, resource_img, pos_x, speed):
        pygame.sprite.Sprite.__init__(self)
        self.img = resource_img
        self.rect = self.img.get_rect()
        self.rect.center = (pos_x, 0)
        self.speed = speed

    def fall(self):
        self.rect.top += self.speed

class Fire_ball(pygame.sprite.Sprite):
    def __init__(self, fire_img, pos_y, WIDTH):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.transform.flip(fire_img, True, False)
        self.rect = self.img.get_rect()
        self.rect.center = (WIDTH, pos_y)
        self.speed = 10

    def move_left(self):
        self.rect.left -= self.speed

class Fire_wall(pygame.sprite.Sprite):
    def __init__(self, fire_img, WIDTH):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.transform.rotate(fire_img, 90)
        self.rect = self.img.get_rect()
        self.rect[3] = 1000
        self.rect.center = (WIDTH - 100, 200)
        self.rect_list = []
        self.WIDTH = WIDTH
        for i in range(20):
            self.rect_list.append(self.img.get_rect())

        for i in range(20):
            self.rect_list[i].center = (WIDTH - 100, i*50 + 10)

    def move_left(self):
        for i in range(20):
            if self.rect_list[i].left <= 0:
                self.rect_list[i].left = 0
            else:
                self.rect_list[i].left -= 0.5
        self.rect.left -= 0.5

    def move_right(self):
        for i in range(20):
            if self.rect_list[i].left >= self.WIDTH - self.rect.width:
                self.rect_list[i].left = self.WIDTH - self.rect.width
            else:
                self.rect_list[i].left += 100
        self.rect.left += 100


class Player(pygame.sprite.Sprite):
    def __init__(self, player_img, player_move_img, player_fire_img, init_pos, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.player_img = player_img
        self.player_move_img = player_move_img
        self.player_fire_img = player_fire_img
        self.rect = self.player_img[0].get_rect()
        self.rect.center = init_pos
        self.speed = 3
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.flag_move = False
        self.orientation = 1
        self.flag_fire = False
        self.fire_index = 0
        self.fire_count = 0
        self.fire_count_max = 29

        self.move_index = 0
        self.move_count = 0
        self.move_count_max = 19

    def fire_change(self):
        self.fire_count += 1
        if self.fire_count > self.fire_count_max:
            self.fire_count = 15
        self.fire_index = self.fire_count//5
        self.move_right()

    def on_fire(self):
        self.flag_fire = True
        current_center = self.rect.center
        self.rect = self.player_fire_img[0].get_rect()
        self.rect.center = current_center

    def flip(self):
        self.player_img[0] = pygame.transform.flip(self.player_img[0], True, False)
        self.player_move_img[0] = pygame.transform.flip(self.player_move_img[0], True, False)
        self.player_move_img[1] = pygame.transform.flip(self.player_move_img[1], True, False)
        self.player_move_img[2] = pygame.transform.flip(self.player_move_img[2], True, False)
        self.player_move_img[3] = pygame.transform.flip(self.player_move_img[3], True, False)

    def change_move_index(self):
        self.move_count += 1
        if self.move_count > self.move_count_max:
            self.move_count = 0
        self.move_index = self.move_count//5

    def move_up(self):  #移动的时候如果要超出屏幕就不能动了
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed
        self.change_move_index()

    def move_down(self):
        if self.rect.top >= self.HEIGHT - self.rect.height:
            self.rect.top = self.HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed
        self.change_move_index()

    def move_left(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed
        self.change_move_index()

    def move_right(self):
        if self.rect.left >= self.WIDTH - self.rect.width:
            self.rect.left = self.WIDTH - self.rect.width
        else:
            self.rect.left += self.speed
        self.change_move_index()
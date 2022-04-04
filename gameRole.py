# -*- coding: utf-8 -*-
"""
the class for all the objects in the game
@author: ZHANG Chenyu
"""

import pygame
from pygame.locals import *

# the class bullet
class Resource(pygame.sprite.Sprite):
    def __init__(self, resource_img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.resource_img = resource_img
        self.rect = self.resource_img.get_rect()
        self.rect.center = pos

class Fire_wall(pygame.sprite.Sprite):
    def __init__(self, fire_img, WIDTH):
        pygame.sprite.Sprite.__init__(self)
        self.fire = pygame.transform.rotate(fire_img, 90)
        self.rect = self.fire.get_rect()
        self.rect[3] = 1000
        self.rect.center = (WIDTH - 100, 200)
        self.rect_list = []
        self.WIDTH = WIDTH
        for i in range(20):
            self.rect_list.append(self.fire.get_rect())

        for i in range(20):
            self.rect_list[i].center = (WIDTH - 100, i*50 + 10)

    def move_left(self):
        for i in range(20):
            if self.rect_list[i].left <= 0:
                self.rect_list[i].left = 0
            else:
                self.rect_list[i].left -= 1
        self.rect.left -= 1

    def move_right(self):
        for i in range(20):
            if self.rect_list[i].left >= self.WIDTH - self.rect.width:
                self.rect_list[i].left = self.WIDTH - self.rect.width
            else:
                self.rect_list[i].left += 60
        self.rect.left += 60

# class FriendCross(Friend):
#     def __init__(self, number, init_pos, font, WIDTH):
#         Friend.__init__(self, number, init_pos, font)
#         self.WIDTH = WIDTH
#         if init_pos[0] < 400:
#             self.move_mode = 0  # 向右移动
#         else:
#             self.move_mode = 1  # 向左
#
#     def move(self):
#         if self.move_mode == 0:
#             self.rect.right += self.speed
#         if self.move_mode == 1:
#             self.rect.left -= self.speed
#         if self.rect.left <= 0:
#             self.move_mode = 0
#         if self.rect.right >= self.WIDTH:
#             self.move_mode = 1
#         self.rect.top += self.speed/2
#
# class FriendVari(Friend):
#     def __init__(self, number, init_pos, font):
#         Friend.__init__(self, number, init_pos, font)
#         self.static = False
#         self.threshold = 50
#         self.count = 0
#
#     def increment(self):
#         self.count += 1
#         if self.count >= self.threshold:
#             self.number += 1
#             self.text = self.font.render(str(self.number), True, (255, 255, 255))
#             self.count = 0
#
# class FriendDisappear(Friend):
#     def __init__(self, number, init_pos, font):
#         Friend.__init__(self, number, init_pos, font)
#         self.disappear = True
#         self.count = 0
#         self.speed = 1
#         self.threshold = 50
#         self.show = True
#
#     def show_count(self):
#         self.count += 1
#         if self.count >= self.threshold:
#             self.count = 0
#             if self.show:
#                 self.show = False
#             else:
#                 self.show = True

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
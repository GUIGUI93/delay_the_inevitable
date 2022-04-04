# -*- coding: utf-8 -*-
"""
LD theme: start with nothing
@author: ZHANG Chenyu
"""

import pygame
from sys import exit
from pygame.locals import *
import random
import os
import math
from gameRole import *

# 注意存放文件的文件夹命名不要有中文，不然会找不到同一个文件夹下的文件，比如gameRole

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
# initialize the game
pygame.init()
if os.name == 'posix':   # mac环境中运行必须要这么设置，不然刷新频率太低
    flags = FULLSCREEN | DOUBLEBUF
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags)
    screen.set_alpha(None)
else:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.set_alpha(None)
pygame.display.set_caption('Delay the inevitable')

# pygame.mixer.init()
# gain_sound = pygame.mixer.Sound('resources/sound/gain.mp3')
# lose_sound = pygame.mixer.Sound('resources/sound/lose.mp3')
# victory_sound = pygame.mixer.Sound('resources/sound/victory.wav')

resources0 = pygame.image.load('resources/character/fire/firen_0.bmp')
resources2 = pygame.image.load('resources/character/fire/firen_2.bmp')
resources_ball = pygame.image.load('resources/character/fire/firen_ball.bmp')
resources_item = pygame.image.load('resources/item/resource.bmp')

player_rect = []   # 注意这个rect取的方法，第一二个点是图片的左上角坐标，然后两个数值是宽和高
player_rect.append(pygame.Rect(15, 10, 45, 70))
player_rect.append(pygame.Rect(335, 10, 45, 70))
player_rect.append(pygame.Rect(415, 10, 45, 70))
player_rect.append(pygame.Rect(495, 10, 45, 70))
player_rect.append(pygame.Rect(575, 10, 45, 70))
# 玩家精灵图片区域
player_img = []
player_img.append(resources0.subsurface(player_rect[0]))
# 玩家爆炸精灵图片区域
player_move_img = []
player_move_img.append(resources0.subsurface(player_rect[1]))
player_move_img.append(resources0.subsurface(player_rect[2]))
player_move_img.append(resources0.subsurface(player_rect[3]))
player_move_img.append(resources0.subsurface(player_rect[4]))

player_fire_rect = []
player_fire_rect.append(pygame.Rect(245, 170, 60, 70))
player_fire_rect.append(pygame.Rect(335, 170, 60, 70))
player_fire_rect.append(pygame.Rect(410, 170, 60, 70))
player_fire_rect.append(pygame.Rect(5, 170, 60, 70))
player_fire_rect.append(pygame.Rect(90, 170, 60, 70))
player_fire_rect.append(pygame.Rect(170, 170, 60, 70))

player_fire_img = []
player_fire_img.append(resources2.subsurface(player_fire_rect[0]))
player_fire_img.append(resources2.subsurface(player_fire_rect[1]))
player_fire_img.append(resources2.subsurface(player_fire_rect[2]))
player_fire_img.append(resources2.subsurface(player_fire_rect[3]))
player_fire_img.append(resources2.subsurface(player_fire_rect[4]))
player_fire_img.append(resources2.subsurface(player_fire_rect[5]))

fire_ball_img = resources_ball.subsurface(pygame.Rect(25, 180, 60, 60))
resource_img = resources_item.subsurface(pygame.Rect(295, 5, 57, 53))

# 开始画面
def open():
    font = pygame.font.Font(None, 32)  # 字体大小的
    clock = pygame.time.Clock()
    while 1:
        clock.tick(60)
        screen.fill(0)
        text1 = font.render(str("You have only one single mission"), True, (255, 255, 255))
        text_rect1 = text1.get_rect()
        text_rect1.center = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 200]

        text2 = font.render(str("Collect the boxes of resource"), True, (255, 255, 255))
        text_rect2 = text2.get_rect()
        text_rect2.center = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150]

        text3 = font.render(str("And delay the inevitable fatal fire wall"), True, (255, 255, 255))
        text_rect3 = text3.get_rect()
        text_rect3.center = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100]

        text4 = font.render(str("Try to collect 10 boxes"), True, (255, 255, 255))
        text_rect4 = text4.get_rect()
        text_rect4.center = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50]

        text5 = font.render(str("And you shall know something"), True, (255, 255, 255))
        text_rect5 = text5.get_rect()
        text_rect5.center = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 ]

        text6 = font.render(str("Something important in life"), True, (255, 255, 255))
        text_rect6 = text6.get_rect()
        text_rect6.center = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50]

        text7 = font.render(str("Tap space to start"), True, (255, 255, 255))
        text_rect7 = text7.get_rect()
        text_rect7.center = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100]

        text8 = font.render(str("And use direction keys to control"), True, (255, 255, 255))
        text_rect8 = text8.get_rect()
        text_rect8.center = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150]

        screen.blit(text1, text_rect1)
        screen.blit(text2, text_rect2)
        screen.blit(text3, text_rect3)
        screen.blit(text4, text_rect4)
        screen.blit(text5, text_rect5)
        screen.blit(text6, text_rect6)
        screen.blit(text7, text_rect7)
        screen.blit(text8, text_rect8)

        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_SPACE]:
            return

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


def win():
    font = pygame.font.Font(None, 36)  # 字体大小的
    clock = pygame.time.Clock()
    while 1:
        clock.tick(60)
        screen.fill(0)
        text1 = font.render(str("Congratulations! You made it"), True, (255, 255, 255))
        text_rect1 = text1.get_rect()
        text_rect1.center = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 200]

        text2 = font.render(str("At some point, we can change the rule"), True, (255, 255, 255))
        text_rect2 = text2.get_rect()
        text_rect2.center = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 150]

        text3 = font.render(str("Make inevitable to possible"), True, (255, 255, 255))
        text_rect3 = text3.get_rect()
        text_rect3.center = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 100]

        text4 = font.render(str("Don't always try to delay, try to change the rule"), True, (255, 255, 255))
        text_rect4 = text4.get_rect()
        text_rect4.center = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50]

        text5 = font.render(str("And you will find a new life"), True, (255, 255, 255))
        text_rect5 = text5.get_rect()
        text_rect5.center = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]

        text6 = font.render(str("Tap space key to restart the game"), True, (255, 255, 255))
        text_rect6 = text6.get_rect()
        text_rect6.center = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 100]

        screen.blit(text1, text_rect1)
        screen.blit(text2, text_rect2)
        screen.blit(text3, text_rect3)
        screen.blit(text4, text_rect4)
        screen.blit(text5, text_rect5)
        screen.blit(text6, text_rect6)

        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_SPACE]:
            return

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

def game():
    clock = pygame.time.Clock()

    player_number = 0
    player_pos = [10, SCREEN_HEIGHT/2]
    player = Player(player_img, player_move_img, player_fire_img, player_pos, SCREEN_WIDTH, SCREEN_HEIGHT)

    resource_group = pygame.sprite.Group()
    resource_frequence = 0
    resource_interval = 100
    resource_list = []
    fire_wall = Fire_wall(fire_ball_img, SCREEN_WIDTH)
    resource_count = 0

    while 1:
        # 控制游戏最大帧率为60
        clock.tick(60)
        # 绘制背景
        screen.fill(0)
        # screen.blit(background, (0, 0))

        if resource_frequence == resource_interval:
            pos_x = random.randint(0, fire_wall.rect.left)
            pos_y = random.randint(0, SCREEN_HEIGHT)
            resource = Resource(resource_img, (pos_x, pos_y))
            resource_group.add(resource)
            resource_frequence = 0

        if pygame.sprite.collide_rect(player, fire_wall) and not player.flag_fire:
            return 1
        if player.rect.left >= SCREEN_WIDTH - 80:
            return 0

        for one in resource_group:
            if pygame.sprite.collide_rect(player, one):
                resource_group.remove(one)
                fire_wall.move_right()
                resource_count += 1

        key_pressed = pygame.key.get_pressed()
        player.flag_move = False
        if key_pressed[K_w] or key_pressed[K_UP]:
            player.move_up()
            player.flag_move = True
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            player.move_down()
            player.flag_move = True
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            player.move_left()
            player.flag_move = True
            if player.orientation == 1:
                player.flip()
                # print("debug0: ", player.orientation)
                player.orientation = 0

        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            player.move_right()
            player.flag_move = True
            if player.orientation == 0:
                player.flip()
                # print("debug1: ", player.orientation)
                player.orientation = 1

        if resource_count >= 10:
            player.on_fire()

        if player.flag_fire:
            player.fire_change()
            screen.blit(player.player_fire_img[player.fire_index], player.rect)
        else:
            if player.flag_move:
                screen.blit(player.player_move_img[player.move_index], player.rect)
            else:
                screen.blit(player.player_img[0], player.rect)
                player.move_index = 0

        fire_wall.move_left()
        for one in fire_wall.rect_list:
            screen.blit(fire_ball_img, one)
        for one in resource_group:
            screen.blit(resource_img, one)

        resource_frequence += 1
        # 更新屏幕
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

if __name__ == '__main__':
    open()
    while(1):
        res = game()
        if res:
            open()
        else:
            win()

        
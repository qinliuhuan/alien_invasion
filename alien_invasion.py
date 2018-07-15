# import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # screen = pygame.display.set_mode((1200, 800))
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    aliens = Group()
    # 创建一个外星人
    # alien = Alien(ai_settings, screen)
    #创建一群外星人
    gf.create_fleet(ai_settings, screen, ship, aliens)


    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        # 删除已经消失的子弹
        gf.update_bullets(bullets)
        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        # 让最近绘制的屏幕可见


run_game()
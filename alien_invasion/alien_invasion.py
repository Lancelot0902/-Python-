import sys
import pygame
import game_functions as gf
from ship import Ship
from alien import Alien
from button import Button
from settings import Settings
from pygame.sprite import Group
from game_stats import Gamestats
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建开始按钮
    play_button = Button(ai_settings, screen, "play")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于管理子弹的编组
    bullets = Group()

    #创建一个外星人编组
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建一个用于统计游戏信息的实例
    stats = Gamestats(ai_settings)
    score = Scoreboard(ai_settings,screen,stats)

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, score, ship, aliens, bullets, play_button)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, score, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, score, screen, ship, aliens, bullets)

        #每次循环都重绘屏幕并使之可见
        gf.update_screen(ai_settings, stats, score, screen, ship,
                        aliens, bullets, play_button)


run_game()

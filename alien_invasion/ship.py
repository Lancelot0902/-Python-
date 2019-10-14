import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_setttings, screen):
        """ 初始化飞船并设置其初始位置 """
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_setttings

        """ 加载飞船图像并获取其外接矩形 """
        self.image = pygame.image.load(
            r'F:\Python\program\alien_invasion\images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        """ 将每艘新飞船放到底部中央 """
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        """ 在飞船的属性center中存储小数值 """
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        """ 移动标志 """
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

        self.screen_top = self.rect.top

    def update(self):
        """ 根据标志位移动飞船 """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.top < self.screen_top:
            self.centery += self.ai_settings.ship_speed_factor

        """ 根据center更新rect对象 """
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """ 在指定位置绘制新飞船 """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """ 让飞船在屏幕上居中 """
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.bottom

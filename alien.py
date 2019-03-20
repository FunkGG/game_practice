import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示外星人的类"""
    def __init__(self, ai_settings, screen):
        """初始化外星人并设置起始外置"""
        super().__init__()
        self.screen = screen
        self.settings = ai_settings
        # 加载外星人图像并设置其rect属性
        self.image = pygame.image.load('images/alien1.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height / 2

        # 储存外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edge(self):
        if self.rect.right >= self.settings.screen_width:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self):
        """向左或右移动外星人"""
        self.x += self.settings.fleet_speed * self.settings.fleet_direction
        self.rect.x = self.x
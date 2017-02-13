import sys
import pygame
class Ship():
    """创建飞船"""
    def __init__(self, screen):
        """初始化飞船"""
        self.screen = screen

        #加载飞船图像并获取其外界矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect =screen.get_rect()

        #每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitem(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

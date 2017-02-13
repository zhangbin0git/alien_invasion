#导入 pygame
import sys
import pygame
from settings import Settings
#导入飞船
from ship import Ship
def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai = Settings()
    screen = pygame.display.set_mode((ai.screen_width, ai.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建飞船
    ship = Ship(screen)
    #设置背景颜色
    # bg_color = (230, 230, 230)
    #start 主循环
    while True:
        #监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #每次重绘屏幕
        screen.fill(ai.bg_color)
        #绘制飞船
        ship.blitem()
        #让最近绘制的屏幕可见
        pygame.display.flip()
run_game()


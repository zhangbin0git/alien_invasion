#导入 pygame
import pygame
from settings import Settings
import game_functions as gf
#导入飞船
from ship import Ship
def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai = Settings()
    screen = pygame.display.set_mode((ai.screen_width, ai.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建飞船
    ship = Ship(ai, screen)
    #设置背景颜色
    # bg_color = (230, 230, 230)
    #start 主循环
    while True:
        #监听键盘和鼠标事件
        gf.check_events(ship)
        ship.update()
        #每次重绘屏幕
        gf.update_screen(ai, screen, ship)
run_game()


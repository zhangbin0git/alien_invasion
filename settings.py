class Settings():
    """储存游戏的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        #screen set
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #船的设置
        self.ship_speed_factor = 1.5
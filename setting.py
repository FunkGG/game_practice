class Settings:
    """储存Alien Alien Invasion的所有设置类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed = 3

        # 子弹的设置
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_maximum = 5

        # 外星人设定
        self.fleet_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1



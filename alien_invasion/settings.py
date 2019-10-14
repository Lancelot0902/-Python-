class Settings():
    """存储游戏中所有设置的类"""

    def __init__(self):   # init前后都有两个下划线
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ships_limit = 3

        # 外星人设置
        self.fleet_drop_speed = 10

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.5
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

    def initialize_dynamic_settings(self):
        # 飞船 外星人 子弹的速度
        self.ship_speed_factor = 1.5
        self.alien_speed_factor = 1
        self.alien_points = 50
        self.bullet_speed_factor = 1
        # 外星人移动标志 1表示向右移 -1表示向左移
        self.fleet_direction = 1

    def increase_speed(self):
        """ 提高速度设置 """
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_points *= int(self.alien_points * self.score_scale)

class Gamestats():
    """ 跟踪游戏的统计信息 """

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

        # 最任何情况下都不应该重置的最高得分
        with open(r'F:\Python\program\alien_invasion\high_score.txt') as filename:
            high_str = filename.read()
            self.high_score = int(high_str)

    def reset_stats(self):
        """ 初始化在游戏运行期间可能变化的信息 """
        self.ships_left = self.ai_settings.ships_limit
        self.score = 0
        self.level = 1

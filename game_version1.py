from pygame.sprite import Group
from ship import Ship
from game_function import *
from setting import Settings


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()  # 导入设置
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    creat_fleet(ai_settings, aliens, screen)

    # 开始游戏的主循环
    start_game()
    while 1:
        # 监视键盘和鼠标事件
        check_event(ai_settings, screen, ship, bullets)
        ship.update()
        update_bullets(bullets, aliens, ai_settings, screen)
        update_aliens(aliens, ai_settings)
        update_screen(screen, ai_settings.bg_color, ship, bullets, aliens)


if __name__ == '__main__':
    run_game()






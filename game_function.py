'''这个文件保存游戏开始后需要的操作
    check_event:检测玩家的操作，修改对应对象的参数
    update_screen:根据修改后的参数刷新屏幕
'''

import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_event(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_event_keydown(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_event_keyup(event, ship)


def check_event_keydown(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(bullets,ai_settings, screen, ship)
    elif event.key == pygame.K_q:
        sys.exit()


def check_event_keyup(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def fire_bullet(bullets,ai_settings, screen, ship):
    new_bullet = Bullet(ai_settings, screen, ship)  # 玩家按下空格，创建一个Bullet对象
    if len(bullets) < ai_settings.bullets_maximum:
        bullets.add(new_bullet)  # 将新建的bullet加入bullets中


def creat_fleet(ai_settings, aliens, screen):
    alien = Alien(ai_settings, screen)
    aliens_per_row = int(ai_settings.screen_width/(2 * alien.rect.width)-1)
    aliens_row_number = int(.5 * ai_settings.screen_height/(1.5 * alien.rect.height))
    for row_number in range(aliens_row_number):
        aliens_height = 1.5 * alien.rect.height * row_number + alien.rect.height
        creat_aliens(aliens, screen, ai_settings, aliens_per_row, aliens_height)


def creat_aliens(aliens, screen,ai_settings , aliens_per_row, aliens_height):
    for alien_number in range(aliens_per_row):
        alien = Alien(ai_settings, screen)
        alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = aliens_height
        aliens.add(alien)


def update_screen(screen, bg_color, ship, bullets, aliens):
    screen.fill(bg_color)
    for bullet in bullets:  # 更新所有bullet的位置
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets, aliens, ai_settings, screen):
    bullets.update()
    for bullet in bullets:  # 更新所有bullet的位置
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 检查是否有子弹击中了外星人
    # 如果击中就删除相应的子弹和外星人
    check_bullet_alien_collisions(bullets, aliens, ai_settings, screen)


def check_bullet_alien_collisions(bullets, aliens, ai_settings, screen):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        creat_fleet(ai_settings, aliens, screen)


def change_fleet_direction(aliens, ai_settings):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_fleet_edges(aliens, ai_settings):
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(aliens, ai_settings)
            break

def update_aliens(aliens, ai_settings):
    """更新外星人群的位置"""
    check_fleet_edges(aliens, ai_settings)
    aliens.update()






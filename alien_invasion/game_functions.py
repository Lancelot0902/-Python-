import sys
import pygame
from time import sleep
from alien import Alien
from bullet import Bullet


def check_keydown_events(event, ai_settings, stats, screen, ship, bullets):
    """ 响应按键 """
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        # 向上移动飞船
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        # 向下移动飞船
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # 创建一个新的子弹并加入到子弹编组中
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        record_high_score(stats)
        sys.exit()


def check_keyup_events(event, ship):
    """ 响应松开 """
    if event.key == pygame.K_RIGHT:
        # 停止
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 停止
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        # 停止
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        # 停止
        ship.moving_down = False


def check_events(ai_settings, screen, stats, score, ship, aliens, bullets, play_button):
    """ 响应按键和鼠标事件 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            record_high_score(stats)
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, stats, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, score, play_button,
                              ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, score, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """ 在玩家点击play时开始游戏 """
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()

        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 重设游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        score.prep_score()
        score.prep_high_score
        score.prep_level()
        score.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人并让飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < 3:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(ai_settings, screen, stats, score, ship, aliens, bullets):
    # 更新子弹位置
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # 检查外星人和子弹是否碰撞
    check_bullet_alien_collisions(
        ai_settings, screen, stats, score, ship, aliens, bullets)


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # 创建一个外星人并将其加入当前行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """ 创建外星人群 """
    # 创建一个外星人并计算能容纳多少个外星人
    # 外星人间的间距为外星人的宽度
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_alien_x(ai_settings, alien.rect.width)
    row_numbers = get_number_alien_y(
        ai_settings, ship.rect.height, alien.rect.height)
    # 创建第一行外星人
    for row_number in range(row_numbers):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_alien_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x


def get_number_alien_y(ai_settings, ship_height, alien_height):
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows


def check_bullet_alien_collisions(ai_settings, screen, stats, score, ship, aliens, bullets):
    # 检查子弹是否击中了外星人，如果击中那么让外星人消失
    # 检查aliens群组和bullets群组是否有重叠，并返回记录重叠的字典
    collections = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collections:
        for aliens in collections.values():
            stats.score += ai_settings.alien_points * len(aliens)
            score.prep_score()
        check_hight_score(stats, score)

    # 检查外星人群组是否为空，如果为空则生成新的外星人群组
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)
        stats.level += 1
        score.prep_level()


def check_fleet_edges(ai_settings, aliens):
    """ 有外星人到达边缘时采取相应措施 """
    for alien in aliens:
        if alien.check_edges():
            change_fleet_directions(ai_settings, aliens)
            break


def change_fleet_directions(ai_settings, aliens):
    """ 将外星人下移并改变他们的方向 """
    for alien in aliens:
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_aliens_bottom(ai_settings, stats, score, screen, ship, aliens, bullets):
    """ 检查是否有外星人到了屏幕的低端 """
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, score, screen, ship, aliens, bullets)
            break


def ship_hit(ai_settings, stats, score, screen, ship, aliens, bullets):
    """ 响应被外星人撞到的飞船 """

    if stats.ships_left > 0:
        # ships_left - 1
        stats.ships_left -= 1
        score.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_hight_score(stats, score):
    """ 检查是否诞生了最高分 """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score.prep_high_score()


def record_high_score(stats):
    file_name = r'F:\Python\program\alien_invasion\high_score.txt'
    with open(file_name,'w') as file_object:
        file_object.write(str(stats.high_score))


def update_aliens(ai_settings, stats, score, screen, ship, aliens, bullets):
    """ 检查是否有外星人处于边缘，并更新 """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检查外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, score, screen, ship, aliens, bullets)

    # 检查是否有外星人到了屏幕底端
    check_aliens_bottom(ai_settings, stats, score,
                        screen, ship, aliens, bullets)


def update_screen(ai_settings, stats, score, screen, ship, aliens, bullets, play_button):
    """ 更新屏幕上的图像，并切换到新屏幕 """
    screen.fill(ai_settings.bg_color)
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    score.show_score()
    # 如果游戏处于非活动状态，那么绘制button
    if not stats.game_active:
        play_button.draw_button()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

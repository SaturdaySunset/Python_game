import pygame
import sys
from button import ImageButton
import os
import random
import game_button
from enemy import Enemy
import math


pygame.init()

icon = pygame.image.load("assets/photos/icon.png")
pygame.display.set_icon(icon)

pygame.mixer.music.load("assets/audio/background_music.mp3")
pygame.mixer.music.play(-1)

WIDTH, HEIGHT = 960, 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kingdom_Defence")
main_background = pygame.image.load("assets/photos/background_menu960.jpg").convert_alpha()
clock = pygame.time.Clock()

cursor = pygame.image.load("assets/photos/cursor_2.png")
pygame.mouse.set_visible(False)

level = 1
TOWER_COST = 5000
high_score = 0
level_reset_time = 0

if os.path.exists('score.txt'):
    with open('score.txt', 'r') as file:
        highscore = int(file.read())

WHITE = (255, 255, 255)
GREY = (100, 100, 100)

font = pygame.font.SysFont('Futura', 30)
font_60 = pygame.font.SysFont('Futura', 60)

bg = pygame.image.load('assets/photos/bg.png').convert_alpha()

castle_img_100 = pygame.image.load('assets/photos/castle/castle_100.png').convert_alpha()
castle_img_50 = pygame.image.load('assets/photos/castle/castle_50.png').convert_alpha()
castle_img_25 = pygame.image.load('assets/photos/castle/castle_25.png').convert_alpha()

tower_img_100 = pygame.image.load('assets/photos/tower/tower_100.png').convert_alpha()
tower_img_50 = pygame.image.load('assets/photos/tower/tower_50.png').convert_alpha()
tower_img_25 = pygame.image.load('assets/photos/tower/tower_25.png').convert_alpha()

bullet_img = pygame.image.load('assets/photos/bullet.png').convert_alpha()
b_w = bullet_img.get_width()
b_h = bullet_img.get_height()
bullet_img = pygame.transform.scale(bullet_img, (int(b_w * 0.075), int(b_h * 0.075)))

enemy_animations = []
enemy_types = ['knight', 'goblin', 'purple_goblin', 'red_goblin']
enemy_health = [75, 100, 125, 150]

animation_types = ['walk', 'attack', 'death']
for enemy in enemy_types:

    animation_list = []
    for animation in animation_types:

        temp_list = []

        num_of_frames = 20
        for i in range(num_of_frames):
            img = pygame.image.load(f'assets/photos/enemies/{enemy}/{animation}/{i}.png').convert_alpha()
            e_w = img.get_width()
            e_h = img.get_height()
            img = pygame.transform.scale(img, (int(e_w * 0.2), int(e_h * 0.2)))
            temp_list.append(img)
        animation_list.append(temp_list)
    enemy_animations.append(animation_list)

repair_img = pygame.image.load('assets/photos/repair.png').convert_alpha()

armour_img = pygame.image.load('assets/photos/armour.png').convert_alpha()


def main_menu():
    start_button = ImageButton(WIDTH / 2 - (252 / 2),
                               130,
                               252,
                               74,
                               "START",
                               "assets/photos/Button.png",
                               "assets/photos/Button_light.png",
                               "assets/audio/Sound.mp3")

    settings_button = ImageButton(WIDTH / 2 - (252 / 2),
                                  240,
                                  252,
                                  74,
                                  "SETTINGS",
                                  "assets/photos/Button.png",
                                  "assets/photos/Button_light.png",
                                  "assets/audio/Sound.mp3")

    exit_button = ImageButton(WIDTH / 2 - (252 / 2),
                              350,
                              252,
                              74,
                              "EXIT",
                              "assets/photos/Button.png",
                              "assets/photos/Button_light.png",
                              "assets/audio/Sound.mp3")
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        text_surface = font.render("MENU", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH/2, 70))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == start_button:
                fade()
                start_game()

            if event.type == pygame.USEREVENT and event.button == settings_button:
                fade()
                settings_menu()

            if event.type == pygame.USEREVENT and event.button == exit_button:
                fade()
                pygame.quit()
                sys.exit()

            for btn in [start_button, settings_button, exit_button]:
                btn.alignment(WIDTH / 2 - (252 / 2))

            for btn in [start_button, settings_button, exit_button]:
                btn.handle_event(event)

        for btn in [start_button, settings_button, exit_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x-30, y-15))

        pygame.display.flip()


def settings_menu():
    audio_button = ImageButton(WIDTH / 2 - (252 / 2),
                               130,
                               252,
                               74,
                               "AUDIO",
                               "assets/photos/Button.png",
                               "assets/photos/Button_light.png",
                               "assets/audio/Sound.mp3")

    back_button = ImageButton(WIDTH / 2 - (252 / 2),
                              240,
                              252,
                              74,
                              "BACK",
                              "assets/photos/Button.png",
                              "assets/photos/Button_light.png",
                              "assets/audio/Sound.mp3")
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        text_surface = font.render("SETTINGS", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH/2, 70))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == audio_button:
                fade()
                audio_menu()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False

            for btn in [audio_button, back_button]:
                btn.alignment(WIDTH / 2 - (252 / 2))

            for btn in [audio_button, back_button]:
                btn.handle_event(event)

        for btn in [audio_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x-30, y-15))

        pygame.display.flip()


def fade():
    running = True
    fade_alpha = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

        fade_alpha += 5
        if fade_alpha >= 105:
            fade_alpha = 255
            running = False

        pygame.display.flip()
        clock.tick(20)


def audio_menu():
    music_on_button = ImageButton(WIDTH / 2 - (252 / 2),
                                  150,
                                  252,
                                  74,
                                  "MUSIC ON",
                                  "assets/photos/Button.png",
                                  "assets/photos/Button_light.png",
                                  "assets/audio/Sound.mp3")

    music_off_button = ImageButton(WIDTH / 2 - (252 / 2),
                                   260,
                                   252,
                                   74,
                                   "MUSIC OFF",
                                   "assets/photos/Button.png",
                                   "assets/photos/Button_light.png",
                                   "assets/audio/Sound.mp3")

    back_button = ImageButton(WIDTH / 2 - (252 / 2),
                              370,
                              252,
                              74,
                              "BACK",
                              "assets/photos/Button.png",
                              "assets/photos/Button_light.png",
                              "assets/audio/Sound.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        text_surface = font.render("AUDIO SETTINGS", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH/2, 70))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == music_on_button:
                pygame.mixer.music.unpause()

            if event.type == pygame.USEREVENT and event.button == music_off_button:
                pygame.mixer.music.pause()

            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False

            for btn in [music_on_button, music_off_button, back_button]:
                btn.alignment(WIDTH / 2 - (252 / 2))

            for btn in [music_on_button, music_off_button, back_button]:
                btn.handle_event(event)

        for btn in [music_on_button, music_off_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x - 30, y - 15))

        pygame.display.flip()


def draw_text(text, fnt, text_col, x, y):
    image = fnt.render(text, True, text_col)
    screen.blit(image, (x, y))


def show_info():
    draw_text('Money: ' + str(castle.money), font, GREY, 10, 10)
    draw_text('Score: ' + str(castle.score), font, GREY, 180, 10)
    draw_text('High Score: ' + str(highscore), font, GREY, 180, 30)
    draw_text('Level: ' + str(level), font, GREY, WIDTH // 2, 10)
    draw_text('Health: ' + str(castle.health) + " / " + str(castle.max_health), font, GREY, WIDTH - 230,
              HEIGHT - 50)

    draw_text('1000', font, GREY, WIDTH - 220, 70)
    draw_text(str(TOWER_COST), font, GREY, WIDTH - 150, 70)
    draw_text('500', font, GREY, WIDTH - 70, 70)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = math.radians(angle)
        self.speed = 10

        self.dx = math.cos(self.angle) * self.speed
        self.dy = -(math.sin(self.angle) * self.speed)

    def update(self):
        if self.rect.right < 0 or self.rect.left > WIDTH or self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()

        self.rect.x += self.dx
        self.rect.y += self.dy


class Castle:
    def __init__(self, image100, image50, image25, x, y, scale):
        self.image = None
        self.angle = None
        self.health = 1000
        self.max_health = self.health
        self.fired = False
        self.money = 0
        self.score = 0

        width = image100.get_width()
        height = image100.get_height()

        self.image100 = pygame.transform.scale(image100, (int(width * scale), int(height * scale)))
        self.image50 = pygame.transform.scale(image50, (int(width * scale), int(height * scale)))
        self.image25 = pygame.transform.scale(image25, (int(width * scale), int(height * scale)))
        self.rect = self.image100.get_rect()
        self.rect.x = x
        self.rect.y = y

    def shoot(self):
        pos = pygame.mouse.get_pos()
        x_dist = pos[0] - self.rect.midleft[0]
        y_dist = -(pos[1] - self.rect.midleft[1])
        self.angle = math.degrees(math.atan2(y_dist, x_dist))

        if pygame.mouse.get_pressed()[0] and self.fired is False and pos[1] > 70:
            self.fired = True
            bullet = Bullet(bullet_img, self.rect.midleft[0], self.rect.midleft[1], self.angle)
            bullet_group.add(bullet)

        if not pygame.mouse.get_pressed()[0]:
            self.fired = False

    def draw(self):

        if self.health <= 250:
            self.image = self.image25
        elif self.health <= 500:
            self.image = self.image50
        else:
            self.image = self.image100

        screen.blit(self.image, self.rect)

    def repair(self):
        if self.money >= 1000 and self.health < self.max_health:
            self.health += 500
            self.money -= 1000
            if castle.health > castle.max_health:
                castle.health = castle.max_health

    def armour(self):
        if self.money >= 500:
            self.max_health += 250
            self.money -= 500


class Tower(pygame.sprite.Sprite):
    def __init__(self, image100, image50, image25, x, y, scale):
        pygame.sprite.Sprite.__init__(self)

        self.got_target = False
        self.angle = 0
        self.last_shot = pygame.time.get_ticks()

        width = image100.get_width()
        height = image100.get_height()

        self.image100 = pygame.transform.scale(image100, (int(width * scale), int(height * scale)))
        self.image50 = pygame.transform.scale(image50, (int(width * scale), int(height * scale)))
        self.image25 = pygame.transform.scale(image25, (int(width * scale), int(height * scale)))
        self.image = self.image100
        self.rect = self.image100.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, enemies):
        self.got_target = False
        target_x, target_y = 0, 0

        for enem in enemies:
            if enem.alive:
                target_x, target_y = enem.rect.midbottom
                self.got_target = True
                break

        if self.got_target:
            x_dist = target_x - self.rect.midleft[0]
            y_dist = -(target_y - self.rect.midleft[1])
            self.angle = math.degrees(math.atan2(y_dist, x_dist))

            shot_cooldown = 1000

            if pygame.time.get_ticks() - self.last_shot > shot_cooldown:
                self.last_shot = pygame.time.get_ticks()
                bullet = Bullet(bullet_img, self.rect.midleft[0], self.rect.midleft[1], self.angle)
                bullet_group.add(bullet)

        if castle.health <= 250:
            self.image = self.image25
        elif castle.health <= 500:
            self.image = self.image50
        else:
            self.image = self.image100


class Crosshair:
    def __init__(self, scale):
        image = pygame.image.load('assets/photos/crosshair.png').convert_alpha()
        width = image.get_width()
        height = image.get_height()

        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()

        pygame.mouse.set_visible(False)

    def draw(self):
        mx, my = pygame.mouse.get_pos()
        self.rect.center = (mx, my)
        screen.blit(self.image, self.rect)


castle = Castle(castle_img_100, castle_img_50, castle_img_25, WIDTH - 250, HEIGHT - 300, 0.2)

crosshair = Crosshair(0.025)

repair_button = game_button.Button(WIDTH - 220, 10, repair_img, 0.5)
tower_button = game_button.Button(WIDTH - 140, 10, tower_img_100, 0.1)
armour_button = game_button.Button(WIDTH - 75, 10, armour_img, 1.5)

tower_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()


def start_game():

    global level, highscore, level_reset_time
    level_difficulty = 0
    target_difficulty = 1000
    difficulty_multiplier = 1.1
    game_over = False
    next_level = False
    enemy_timer = 1000
    last_enemy = pygame.time.get_ticks()
    max_towers = 4
    tower_cost = 5000
    tower_positions = [
        (WIDTH - 250, HEIGHT - 200),
        (WIDTH - 200, HEIGHT - 150),
        (WIDTH - 150, HEIGHT - 150),
        (WIDTH - 100, HEIGHT - 150),
    ]

    running = True
    while running:
        clock.tick(FPS)

        if not game_over:
            screen.blit(bg, (0, 0))

            castle.draw()
            castle.shoot()

            tower_group.draw(screen)
            tower_group.update(enemy_group)

            crosshair.draw()

            bullet_group.update()
            bullet_group.draw(screen)

            enemy_group.update(screen, castle, bullet_group)

            show_info()

            if repair_button.draw(screen):
                castle.repair()
            if tower_button.draw(screen):
                if castle.money >= tower_cost and len(tower_group) < max_towers:
                    tower = Tower(
                        tower_img_100,
                        tower_img_50,
                        tower_img_25,
                        tower_positions[len(tower_group)][0],
                        tower_positions[len(tower_group)][1],
                        0.2
                    )
                    tower_group.add(tower)

                    castle.money -= tower_cost
            if armour_button.draw(screen):
                castle.armour()

            if level_difficulty < target_difficulty:
                if pygame.time.get_ticks() - last_enemy > enemy_timer:
                    e = random.randint(0, len(enemy_types) - 1)
                    enem = Enemy(enemy_health[e], enemy_animations[e], -100, HEIGHT - 100, 1)
                    enemy_group.add(enem)

                    last_enemy = pygame.time.get_ticks()

                    level_difficulty += enemy_health[e]

            if level_difficulty >= target_difficulty:

                enemies_alive = 0
                for e in enemy_group:
                    if e.alive:
                        enemies_alive += 1

                if enemies_alive == 0 and not next_level:
                    next_level = True
                    level_reset_time = pygame.time.get_ticks()

            if next_level:
                draw_text('LEVEL COMPLETE!', font_60, WHITE, 200, 300)

                if castle.score > highscore:
                    highscore = castle.score
                    with open('score.txt', 'w') as File:
                        File.write(str(highscore))

                if pygame.time.get_ticks() - level_reset_time > 1500:
                    next_level = False
                    level += 1
                    last_enemy = pygame.time.get_ticks()
                    target_difficulty *= difficulty_multiplier
                    level_difficulty = 0
                    enemy_group.empty()

            if castle.health <= 0:
                game_over = True

        else:
            draw_text('GAME OVER!', font, GREY, 300, 300)
            draw_text('PRESS "SPACE" TO PLAY AGAIN!', font, GREY, 250, 360)
            pygame.mouse.set_visible(True)
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                game_over = False
                level = 1
                target_difficulty = 1000
                level_difficulty = 0
                last_enemy = pygame.time.get_ticks()
                enemy_group.empty()
                tower_group.empty()
                castle.score = 0
                castle.health = 1000
                castle.max_health = castle.health
                castle.money = 0
                pygame.mouse.set_visible(False)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()


if __name__ == "__main__":
    main_menu()

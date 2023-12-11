import pygame
import sys
from button import ImageButton
from player import Player
from enemy import Enemy


pygame.init()

icon = pygame.image.load("assets/photos/icon.png")
pygame.display.set_icon(icon)

pygame.mixer.music.load("assets/audio/background_music.mp3")
pygame.mixer.music.play(-1)

WIDTH, HEIGHT = 960, 600
MAX_FPS = 60

SCORE = 0
font = pygame.font.Font(None, 72)
scoreboard_text = font.render(f"Score: {SCORE}", 1, (255, 255, 255))
score_pos = scoreboard_text.get_rect(topleft=(10, 10))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python_game")
main_background = pygame.image.load("assets/photos/background_menu960.jpg")
background_game = pygame.image.load("assets/photos/game_background960.jpg")
clock = pygame.time.Clock()

cursor = pygame.image.load("assets/photos/cursor_2.png")
crosshair = pygame.image.load("assets/photos/Crosshair_yellow.png")
pygame.mouse.set_visible(False)

enemies = []


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
                running = False
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
                running = False
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

    video_button = ImageButton(WIDTH / 2 - (252 / 2),
                               240,
                               252,
                               74,
                               "VIDEO",
                               "assets/photos/Button.png",
                               "assets/photos/Button_light.png",
                               "assets/audio/Sound.mp3")

    back_button = ImageButton(WIDTH / 2 - (252 / 2),
                              350,
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
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == video_button:
                fade()
                video_menu()

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

            for btn in [audio_button, video_button, back_button]:
                btn.alignment(WIDTH / 2 - (252 / 2))

            for btn in [audio_button, video_button, back_button]:
                btn.handle_event(event)

        for btn in [audio_button, video_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x-30, y-15))

        pygame.display.flip()


def video_menu():

    res_1_button = ImageButton(WIDTH / 2 - (252 / 2),
                               130,
                               252,
                               74,
                               "960 X 600",
                               "assets/photos/Button.png",
                               "assets/photos/Button_light.png",
                               "assets/audio/Sound.mp3")

    res_2_button = ImageButton(WIDTH / 2 - (252 / 2),
                               240,
                               252,
                               74,
                               "1024 X 768",
                               "assets/photos/Button.png",
                               "assets/photos/Button_light.png",
                               "assets/audio/Sound.mp3")

    res_3_button = ImageButton(WIDTH / 2 - (252 / 2),
                               350,
                               252,
                               74,
                               "1920 X 1080",
                               "assets/photos/Button.png",
                               "assets/photos/Button_light.png",
                               "assets/audio/Sound.mp3")

    back_button = ImageButton(WIDTH / 2 - (252 / 2),
                              460,
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

        text_surface = font.render("VIDEO SETTINGS", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH/2, 70))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == res_1_button:
                change_screen_res(960, 600)
                fade()

            if event.type == pygame.USEREVENT and event.button == res_2_button:
                change_screen_res(1024, 768)
                fade()

            if event.type == pygame.USEREVENT and event.button == res_3_button:
                change_screen_res(1920, 1080, pygame.FULLSCREEN)
                fade()

            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False

            for btn in [res_1_button, res_2_button, res_3_button, back_button]:
                btn.alignment(WIDTH / 2 - (252 / 2))

            for btn in [res_1_button, res_2_button, res_3_button, back_button]:
                btn.handle_event(event)

        for btn in [res_1_button, res_2_button, res_3_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x - 30, y - 15))

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


def change_screen_res(width, height, fullscreen=0):
    global WIDTH, HEIGHT, screen, main_background, background_game
    WIDTH, HEIGHT = width, height
    screen = pygame.display.set_mode((WIDTH, HEIGHT), fullscreen)
    main_background = pygame.image.load(f'assets/photos/background_menu{WIDTH}.jpg')
    background_game = pygame.image.load(f"assets/photos/game_background{WIDTH}.jpg")


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
                running = False
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


def start_game():

    enemy_x = WIDTH - 100
    enemy_y = HEIGHT * 0.63

    player = Player(WIDTH * 0.105,
                    HEIGHT * 0.63,
                    120,
                    120,
                    "assets/photos/Hero_0.png",
                    "assets/audio/Arrow_sound.mp3")

    enemy = Enemy(enemy_x,
                  enemy_y,
                  120,
                  120,
                  "assets/photos/Enemy_1.png")

    running = True
    while running:

        speed = 5
        enemy_x -= speed

        screen.fill((0, 0, 0))
        screen.blit(background_game, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if player.sound:
                        player.sound.play()

                    attack_images = [
                        pygame.image.load("assets/photos/Hero_2.png"),
                        pygame.image.load("assets/photos/Hero_3.png")
                    ]

                    start_time = pygame.time.get_ticks()
                    current_time = 0
                    current_image_index = 0

                    while current_time < 400:
                        current_time = pygame.time.get_ticks() - start_time

                        if current_time < 200:
                            current_image_index = 0
                        elif current_time < 400:
                            current_image_index = 1

                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        screen.blit(pygame.image.load("assets/photos/Crosshair_yellow.png"), (mouse_x - 29, mouse_y - 30))

                        screen.blit(attack_images[current_image_index], player.rect.topleft)
                        pygame.display.flip()

                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    screen.blit(pygame.image.load("assets/photos/Crosshair_yellow.png"), (mouse_x - 29, mouse_y - 30))

                    screen.blit(player.image, player.rect.topleft)
                    pygame.display.flip()

        player.draw(screen)
        enemy.draw(screen)
        screen.blit(scoreboard_text, score_pos)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.blit(crosshair, (mouse_x - 29, mouse_y - 30))
        pygame.display.update()


if __name__ == "__main__":
    main_menu()

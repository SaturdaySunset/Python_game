import pygame
import sys
from button import ImageButton


pygame.init()

icon = pygame.image.load("photos/icon.png")
pygame.display.set_icon(icon)

pygame.mixer.music.load("audio/background_music.mp3")
pygame.mixer.music.play(-1)

WIDTH, HEIGHT = 960, 600
MAX_FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python_game")
main_background = pygame.image.load("photos/background_menu960.jpg")
clock = pygame.time.Clock()

cursor = pygame.image.load("photos/cursor_2.png")
pygame.mouse.set_visible(False)


def main_menu():
    start_button = ImageButton(WIDTH / 2 - (252 / 2),
                               130,
                               252,
                               74,
                               "START",
                               "photos/Button.png",
                               "photos/Button_light.png",
                               "audio/Sound.mp3")

    settings_button = ImageButton(WIDTH / 2 - (252 / 2),
                                  240,
                                  252,
                                  74,
                                  "SETTINGS",
                                  "photos/Button.png",
                                  "photos/Button_light.png",
                                  "audio/Sound.mp3")

    exit_button = ImageButton(WIDTH / 2 - (252 / 2),
                              350,
                              252,
                              74,
                              "EXIT",
                              "photos/Button.png",
                              "photos/Button_light.png",
                              "audio/Sound.mp3")
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("MENU", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH/2, 70))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

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
                               "photos/Button.png",
                               "photos/Button_light.png",
                               "audio/Sound.mp3")

    video_button = ImageButton(WIDTH / 2 - (252 / 2),
                               240,
                               252,
                               74,
                               "VIDEO",
                               "photos/Button.png",
                               "photos/Button_light.png",
                               "audio/Sound.mp3")

    back_button = ImageButton(WIDTH / 2 - (252 / 2),
                              350,
                              252,
                              74,
                              "BACK",
                              "photos/Button.png",
                              "photos/Button_light.png",
                              "audio/Sound.mp3")
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        font = pygame.font.Font(None, 72)
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
                for btn in [audio_button, video_button, back_button]:
                    btn.alignment(WIDTH / 2 - (252 / 2))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False

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
                               "photos/Button.png",
                               "photos/Button_light.png",
                               "audio/Sound.mp3")

    res_2_button = ImageButton(WIDTH / 2 - (252 / 2),
                               240,
                               252,
                               74,
                               "1024 X 768",
                               "photos/Button.png",
                               "photos/Button_light.png",
                               "audio/Sound.mp3")

    res_3_button = ImageButton(WIDTH / 2 - (252 / 2),
                               350,
                               252,
                               74,
                               "1920 X 1080",
                               "photos/Button.png",
                               "photos/Button_light.png",
                               "audio/Sound.mp3")

    back_button = ImageButton(WIDTH / 2 - (252 / 2),
                              460,
                              252,
                              74,
                              "BACK",
                              "photos/Button.png",
                              "photos/Button_light.png",
                              "audio/Sound.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        font = pygame.font.Font(None, 72)
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

            for btn in [res_1_button, res_2_button, res_3_button, back_button]:
                btn.alignment(WIDTH / 2 - (252 / 2))

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
        clock.tick(MAX_FPS)


def change_screen_res(width, height, fullscreen=0):
    global WIDTH, HEIGHT, screen, main_background
    WIDTH, HEIGHT = width, height
    screen = pygame.display.set_mode((WIDTH, HEIGHT), fullscreen)
    main_background = pygame.image.load(f'photos/background_menu{WIDTH}.jpg')


def start_game():
    pass


if __name__ == "__main__":
    main_menu()

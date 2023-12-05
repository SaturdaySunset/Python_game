import pygame
import sys
from button import ImageButton


pygame.init()

WIDTH, HEIGHT = 960, 600
MAX_FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Здесь могла быть ваша реклама!")
main_background = pygame.image.load("background_menu.jpg")
clock = pygame.time.Clock()

cursor = pygame.image.load("cursor_2.png")
pygame.mouse.set_visible(False)


def main_menu():
    start_button = ImageButton(WIDTH / 2 - (252 / 2),
                               130,
                               252,
                               74,
                               "START",
                               "Button.png",
                               "Button_light.png",
                               "Sound.mp3")

    settings_button = ImageButton(WIDTH / 2 - (252 / 2),
                                  240,
                                  252,
                                  74,
                                  "SETTINGS",
                                  "Button.png",
                                  "Button_light.png",
                                  "Sound.mp3")

    exit_button = ImageButton(WIDTH / 2 - (252 / 2),
                              350,
                              252,
                              74,
                              "EXIT",
                              "Button.png",
                              "Button_light.png",
                              "Sound.mp3")
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (-100, -350))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("MENU", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(480, 70))
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
                               "Button.png",
                               "Button_light.png",
                               "Sound.mp3")

    video_button = ImageButton(WIDTH / 2 - (252 / 2),
                               240,
                               252,
                               74,
                               "VIDEO",
                               "Button.png",
                               "Button_light.png",
                               "Sound.mp3")

    back_button = ImageButton(WIDTH / 2 - (252 / 2),
                              350,
                              252,
                              74,
                              "BACK",
                              "Button.png",
                              "Button_light.png",
                              "Sound.mp3")
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (-100, -350))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("SETTINGS", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(480, 70))
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


def start_game():
    pass


def exit_game():
    pass


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


if __name__ == "__main__":
    main_menu()

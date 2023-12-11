import pygame
import math


class Player:

    def __init__(self,
                 x,
                 y,
                 width,
                 height,
                 image_path,
                 attack_sound_path=None):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image_path = image_path

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = None
        if attack_sound_path:
            self.sound = pygame.mixer.Sound(attack_sound_path)

    def alignment(self, x, y):
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        current_image = self.image
        screen.blit(current_image, self.rect.topleft)

    def attack(self, event, screen):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.sound:
                self.sound.play()

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

                screen.blit(attack_images[current_image_index], self.rect.topleft)
                pygame.display.flip()

            mouse_x, mouse_y = pygame.mouse.get_pos()
            screen.blit(pygame.image.load("assets/photos/Crosshair_yellow.png"), (mouse_x - 29, mouse_y - 30))

            screen.blit(self.image, self.rect.topleft)
            pygame.display.flip()

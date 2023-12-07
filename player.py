import pygame


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
        for i in [1, 2, 3, 0]:
            pose = f"photos/Hero_{i}.png"
            screen.blit(pygame.image.load(pose), self.rect.topleft)
            if pose == "photos/Hero_3.png":
                if self.sound:
                    self.sound.play()

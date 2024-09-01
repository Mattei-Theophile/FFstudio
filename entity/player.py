import pygame

import settings


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("graphique/player/idle/player_static.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 10

        self.direction = pygame.math.Vector2(0, 0)

    def horizontal_collision(self):
        pass

    def vertical_collision(self):
        pass

    def move_right(self):
        self.direction.x = 1

    def move_left(self):
        self.direction.x = -1
    def static(self):
        self.direction.x = 0

    def is_dead(self):
        if self.rect.y > settings.screen_width:
            self.kill()

        if self.alive():
            return True
        return False

    def update(self):
        self.rect.x += self.direction.x * self.speed

import pygame


class Blob(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("graphique/monster/blob/idle/static_blob.png")
        self.rect = self.image.get_rect(topleft=pos)


class CuteDemon(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("graphique/monster/cute demon/idle/static_cute_demon.png")
        self.rect = self.image.get_rect(topleft=pos)


class LostSoul(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("graphique/monster/lost soul/idle/static_lost_soul.png")
        self.rect = self.image.get_rect(topleft=pos)

import pygame
import pygame_menu
from pygame_menu.controls import Controller
print("test")
import sys
print("test2")

import Levels.level
print("test")
import settings
print("test3")
pygame.init()
screen_width, screen_height = settings.screen_size()


class Game:
    def main_menu(self):
        """ Cette méthode permet de gérer l'affichage de
        le menu de notre Plateformer"""

        while True:

            surface = pygame.display.set_mode((screen_width, screen_height))

            menu = pygame_menu.Menu('Plateformer révolutionnaire', 800, 600,
                                    theme=pygame_menu.themes.THEME_DARK)


            menu.add.button('Play', self.start_game)
            menu.add.button('Quit', pygame_menu.events.EXIT)
            menu.mainloop(surface)
            pygame.display.update()

    def break_menu(self):
        run_break = True
        custom_controller = Controller()
        def test():
            run_break = False

        while run_break:
            pygame_menu.controls.KEY_CLOSE_MENU = pygame.K_h
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        test()
                    if event.key == pygame.K_ESCAPE:
                        run_break = False
                        self.run_game = False

            theme = pygame_menu.Theme(background_color=(30, 30, 30, 200), widget_font=pygame_menu.font.FONT_MUNRO)
            menu = pygame_menu.Menu('Pause', 200, 200,
                                    theme=theme)

            resume = menu.add.button('stay in life', test)
            menu.add.button('Dead', pygame_menu.events.EXIT)


            if menu.is_enabled():
                menu.update(events)
                menu.draw(settings.screen)
            resume.set_controller(custom_controller)
            pygame.display.update()
    def start_game(self):
        self.run_game = True
        clock = pygame.time.Clock()
        level = Levels.level.Level(settings.screen)
        background = pygame.image.load('graphique/background/bg_tree.png')

        while self.run_game:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.break_menu()
                elif event.type == pygame.QUIT:
                    pygame.quit()

            pygame.Surface.blit(settings.screen, source=background, dest=(0, 0))
            level.build_level()
            self.run_game = level.run()

            pygame.display.update()
            print("t")
            clock.tick(60)

    def end_game(self):
        self.main_menu()


while True:
    Game().main_menu()

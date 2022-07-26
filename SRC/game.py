from SRC.map import MapManager
from player import *

import pygame
from dialogue import DialogBox


class Game:

    def __init__(self):
        # Démarrage
        self.running = True
        self.map = "world"
        self.screen = pygame.display.set_mode((800, 600))  # Affichage de la fenêtre
        pygame.display.set_caption("WOWGEMON")
        # Générer le player
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)
        self.dialog_box = DialogBox()
        # # Définir le logo du jeu
        # pygame.display.set_icon(self.player.change_animation())

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_ESCAPE]:
            self.running = False
        elif pressed[pygame.K_UP]:
            self.player.move_player("up")
        elif pressed[pygame.K_DOWN]:
            self.player.move_player("down")
        elif pressed[pygame.K_RIGHT]:
            self.player.move_player("right")
        elif pressed[pygame.K_LEFT]:
            self.player.move_player("left")

    def update(self):
        self.map_manager.update()

    def run(self):
        clock = pygame.time.Clock()

        # Clock
        while self.running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            self.dialog_box.render(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.K_DOWN:
                    if event.key == pygame.K_SPACE:
                        self.map_manager.check_npc_collisions(self.dialog_box)

            clock.tick(60)

        pygame.quit()

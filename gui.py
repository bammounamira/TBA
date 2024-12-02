import pygame
from game import Game

# Initialisation de Pygame
pygame.init()

# Dimensions et paramètres
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FONT_SIZE = 24

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 182, 193)
PURPLE = (128, 0, 128)


class GUI:
    def __init__(self):
        # Configuration de l'écran
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("MIMI Shopping Adventure")

        # Charger Times New Roman (méthode SysFont ou fichier)
        try:
            self.font = pygame.font.SysFont("timesnewroman", FONT_SIZE)
        except:
            print("Failed to load Times New Roman via SysFont. Using default font.")
            self.font = pygame.font.Font(None, FONT_SIZE)

        # Créer le jeu
        self.game = Game()
        self.game.setup()

        # Texte actuel affiché
        self.current_text = self.game.player.current_room.get_long_description()

    def draw_text(self, text, x, y):
        """
        Affiche du texte à une position donnée.
        """
        lines = text.splitlines()
        for i, line in enumerate(lines):
            rendered_text = self.font.render(line, True, PINK)
            self.screen.blit(rendered_text, (x, y + i * FONT_SIZE))

    def main_loop(self):
        """
        Boucle principale du jeu.
        """
        running = True
        input_box = pygame.Rect(50, SCREEN_HEIGHT - 50, 700, 32)
        user_text = ""
        clock = pygame.time.Clock()

        while running:
            self.screen.fill(WHITE)
            clock.tick(30)

            # Afficher le texte principal
            self.draw_text(self.current_text, 50, 50)

            # Dessiner la boîte d'entrée
            pygame.draw.rect(self.screen, PURPLE, input_box)
            pygame.draw.rect(self.screen, BLACK, input_box, 2)

            # Afficher le texte entré
            text_surface = self.font.render(user_text, True, BLACK)
            self.screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print(f"Command entered: {user_text}")  # Débogage
                        user_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

        pygame.quit()


# Lancer l'interface
if __name__ == "__main__":
    gui = GUI()
    gui.main_loop()

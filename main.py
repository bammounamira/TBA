"""
This module serves as the entry point for the game. It initializes the game,
sets up the environment, and starts the gameplay loop.
"""

from game import Game
from actions import Actions

def main():
    """
    Main function to initialize and start the game.

    Steps:
        1. Create a `Game` object.
        2. Set up the game environment (rooms, items, characters, etc.).
        3. Create an `Actions` object to manage game actions.
        4. Start the game loop by calling the `play` method.

    This function orchestrates the game setup and gameplay by coordinating 
    interactions between the player, game world, and actions.
    """
    # Create a game object and play the game
    game = Game()
    game.setup()
    actions = Actions()
    actions.play(game.player, game)

if __name__ == "__main__":
    main()

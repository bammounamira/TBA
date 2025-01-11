from game import Game 
from Item import Item
from character import Character
from command import Command
from player import Player
from room import Room
from actions import Actions


def main():
    # Create a game object and play the game
    game = Game()
    game.setup()
    actions=Actions()
    actions.play(game.player, game)

if __name__ == "__main__":
    main()


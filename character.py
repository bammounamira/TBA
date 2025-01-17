"""
This module defines the Character class, which represents a character in the game.

The Character class includes attributes and methods to describe and interact
with characters in the game world.
"""
import random
class Character:
    """
    Represents a character in the game.

    Attributes:
        name (str): The name of the character.
        description (str): A brief description of the character.
        current_room (str): The current room where the character is located.
        dialogues (list of str): A list of dialogues associated with the character.

    Methods:
        speak():
            Prints the dialogues of the character, enumerated for clarity.
        interact():
            Prints the first dialogue of the character as part of an interaction.
    """

    def __init__(self, name, description, current_room, dialogues):
        """
        Initializes a Character instance.

        Args:
            name (str): The name of the character.
            description (str): A brief description of the character.
            current_room (str): The current room where the character is located.
            dialogues (list of str): A list of dialogues associated with the character.
        """
        self.name = name
        self.description = description
        self.current_room = current_room
        self.dialogues = dialogues

    def get_description(self) -> str:
        """
        Retrieves the description of the character.

        Returns:
            str: A brief description of the character.
        """
        return self.description
    def move_to_random_room(self, rooms: list) -> None:
        """
        Moves the character to a random room from a list of available rooms.

        Args:
            rooms (list of str): A list of room names available for the character to move to.

        Returns:
            None
        """
        if rooms:
            new_room = random.choice(rooms)
            self.current_room = new_room
            print(f"{self.name} has randomly moved to {self.current_room}.")
        else:
            print("No rooms available for movement.")

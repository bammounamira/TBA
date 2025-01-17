"""
This module defines the Room class, which represents a room in the game.

The Room class includes attributes and methods to manage room details, such as
description, characters, items, and exits.
"""

class Room:
    """
    Represents a room in the game.

    Attributes:
        name (str): The name of the room.
        description (str): A description of the room.
        character (list): Characters present in the room.
        items (set): A set of items present in the room.
        exits (dict): A dictionary of exits with directions as keys and Room objects as values.

    Methods:
        __init__(name, description, character, exits):
            Constructor of the class.
        get_exit(direction):
            Returns the room in the given direction if it exists.
        add_exit(direction, room):
            Adds an exit to the room in a specified direction.
        get_exit_string():
            Returns a string describing the room's exits.
        get_long_description():
            Returns a long description of the room including its exits.
        print_inventory():
            Prints the inventory of items in the room.
    """

    def __init__(self, name: str, description: str, character: list, exits: dict):
        """
        Initializes a Room instance.

        Args:
            name (str): The name of the room.
            description (str): A description of the room.
            character (list): Characters present in the room.
            exits (dict): Dictionary of exits with directions as keys and Room objects as values.
        """
        self.name = name
        self.description = description
        self.character = character if character else []
        self.items = set()  # Using a set to store unique items.
        self.exits = exits

    def get_exit(self, direction: str):
        """
        Returns the room in the given direction if it exists.

        Args:
            direction (str): The direction to check for an exit.

        Returns:
            Room or None: The room object in the given direction, or None if it does not exist.
        """
        return self.exits.get(direction)

    def add_exit(self, direction: str, room):
        """
        Adds an exit to the room in a specified direction.

        Args:
            direction (str): The direction of the exit (e.g., "north").
            room (Room): The room object that the exit leads to.
        """
        self.exits[direction] = room

    def get_exit_string(self) -> str:
        """
        Returns a string describing the room's exits.

        Returns:
            str: A string listing the exits of the room.
        """
        return "Exits: " + ", ".join(self.exits.keys())

    def get_long_description(self) -> str:
        """
        Returns a long description of the room including its exits.

        Returns:
            str: A detailed description of the room.
        """
        return f"\nYou are {self.description}.\n{self.get_exit_string()}"

    def print_items(self):
        """
        Prints the list of items in the room.

        Returns:
            bool: True if the room has no items, False otherwise.
        """
        if not self.items:
            print("This room doesn't contain any items.")
            return True

        print("\nThis room contains:")
        for item in self.items:
            print(f"  - {item.name}: {item.description}")
        return False

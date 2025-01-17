"""
This module defines the Command class, which represents a command in the game.

The Command class encapsulates the logic for a specific action, including its
name, description, required arguments, and the associated function to execute.
"""
class Command:
    """
    Represents a command in the game, composed of a name, description, action,
    and number of arguments.

    Attributes:
        name (str): The name of the command (e.g., 'move', 'look').
        description (str): A brief description of the command.
        action (function): The function to execute when the command is called.
        number_of_arguments (int): The number of parameters expected by the command.
        help_string (str): Detailed help text for the command.
    """

    def __init__(self, name: str, description: str,
                action, number_of_arguments: int, help_string: str = None):
        """
        Initializes a Command instance.

        Args:
            name (str): The name of the command.
            description (str): A brief description of the command.
            action (function): The function to execute when the command is called.
            number_of_arguments (int): The number of parameters expected by the command.
            help_string (str, optional): Detailed help text for the command. Defaults to None.
        """
        self.name = name
        self.description = description
        self.action = action
        self.number_of_arguments = number_of_arguments
        self.help_string = help_string or f"{name}: {description}"

    def execute(self, player, game, *args) -> None:
        """
        Executes the command.

        Args:
            player (Player): The player object.
            game (Game): The game object.
            *args: Arguments required by the command.

        Returns:
            None: Prints an error message if the command is called with insufficient arguments.
        """
        if len(args) < self.number_of_arguments:
            print(
                f"Error: '{self.name}' requires {self.number_of_arguments} argument(s). "
                f"{len(args)} provided."
            )
            return

        # Call the action with the provided arguments
        self.action(player, game, *args)

    def validate_arguments(self, *args) -> bool:
        """
        Validates the number of arguments passed to the command.

        Args:
            *args: The arguments to validate.

        Returns:
            bool: True if the number of arguments is valid, False otherwise.
        """
        return len(args) >= self.number_of_arguments

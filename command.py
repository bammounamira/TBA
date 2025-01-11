class Command:
    """
    This class represents a command. A command is composed of a command word, a help string, an action, and a number of parameters.

    Attributes:
        name (str): The name of the command (e.g., 'move', 'look').
        description (str): A brief description of the command.
        action (function): The action to execute when the command is called.
        number_of_arguments (int): The number of parameters expected by the command.
        help_string (str): Detailed help text for the command.
    """

    def __init__(self, name, description, action, number_of_arguments, help_string=None):
        self.name = name
        self.description = description
        self.action = action  # Function to execute
        self.number_of_arguments = number_of_arguments
        self.help_string = help_string or f"{name}: {description}"

    def execute(self, player, game, *args):
        """
        Executes the command.

        Args:
            player (Player): The player object.
            game (Game): The game object.
            *args: Arguments required by the command.

        Returns:
            str: The result of executing the command.
        """
        if len(args) < self.number_of_arguments:
            print(f"Error: '{self.name}' requires {self.number_of_arguments} argument(s).")
            return

        # Call the action with the provided arguments
        self.action(player, game, args)

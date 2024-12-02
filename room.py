#Define the Room class.
class Room():
    """
    This class represent de different rooms that exist in the game. A room is composed of a name, a description, items and an exit.

    Attributes:
        name (str): The name of the room.
        items (str) : the items in the room.
        description (str): The description of the room.
        exits (dict): The differents exits of a room.

    Methods:
        __init__ : constructor of the class
        get_exit : methods which take the direction given by the player in order to check if the exit direction exist.
        get_exit_string : method which returns the description of the room's exit.
        get_long_description :method which returns a long description of the room's exit.
    """
    #Define the constructor.
    def __init__(self, name, description, character, items, exits):
        self.name=name 
        self.description=description
        self.character=character
        self.items=set()
        self.exits=exits

    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits:
            return self.exits[direction]
        else:
            return None
    
    def add_exit(self, direction: str, room):
        """
    Adds an exit to the room in a specified direction.

    Parameters:
        direction (str): The direction of the exit (e.g., "north").
        room (Room): The room that the exit leads to.
        """
        self.exits[direction] = room


# Return a string describing the room's exits.
    def get_exit_string(self) -> str:
        exit_string = "Exits: " 
        for exit in self.exits: 
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self) -> str:
        return f"\nYou are {self.description}\n\n{self.get_exit_string()}\n"
    
    def print_inventory(self):
       
        if len(self.inventory) == 0:
            print("This room doesn't contain any item.")
            return True
        
        print("\nThis room contains :\n")
        for i in self.inventory:
            print("   ", i.name, ":", i.description)

        return True













































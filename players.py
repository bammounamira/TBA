#Define the Player class
class Player(): 
"""
    This class represent the player of the game.

    Attributes:
    name (str): The name chosen by the player.
    hair (str): The hair color or style of the player.
    eyes (str): The eye color of the player.
    height (int): The height of the player in centimeters.
    style (str): The clothing style or appearance of the player.
    current_room (Room): The current room where the player is.
    cart (str) : the list of items the player has collected. A dictionary where keys are items and values are their prices.
    credit (str): the amount of credit the player has. 
    

    Methods:
        __init__ : Constructor of the class
        Checks if the direction chosen by the player exists 
        in the current room's exits. If it does, changes the
        player's current room to the next room in that direction 
        and returns a description of the new room.
"""
    Examples :

    >>> player = Player("Myriam")
    >>> player.name
    'Myriam'
    >>> player.current_room
    None

#Define the constructor
    def __init__(self, name, hair, eyes, height, style, cadi, total, credit, current_room):
        self.name = name
        self.hair = hair
        self.eyes = eyes
        self.height = height
        self.style = style
        self.total = 0
        self.cart= {} # Initialize an empty list to hold the player's inventory
        self.credit= credit #Initialize the player's credit balance
        self.current_room= None #By default, the player has no room assigned

#define the move method 
def move(self, direction):
 """
    Checks if the direction chosen by the player exists in the current room's exits.
    If it does, changes the player's current room to the next room in that direction
    and returns a description of the new room. If the direction is invalid, returns
    an error message.

    Parameters:
        direction (str): The direction in which the player wants to move.

    Returns:
        str: A description of the new room if the move is successful, or an error message.
"""
    if direction in self.current_room.exits:
        next_room = self.current_room.exits[direction]
        self.current_room = next_room
        return f"You move {direction}. {next_room.description}"
    else:
        return f"There is no exit to the {direction}."

def add_item(self,item : str, price : int):
"""
    Adds item with thir price to cadi. 
    
    Parameters :
    item(str) : every item that the player selected 
    price(int) : the price of every item selected 
"""

     # Add or update the item in the cadi dictionary
    self.cart.update({item:price}) # Using update to add the item and its price
    self.total +=   # Update the total cost of items in the cadi
    return f"{item} is added to your cart for {price}."

def show_cart(self):
    """Displays the item in the player's cadi 

    Returns : A summary of the items.
    """
    if not self.cadi: 
        return "Your cart is empty."
    all_items = "Items in your cart:\n"
    for items in self.cart.keys():
    return all_items 




















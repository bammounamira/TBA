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
    gift_card (str): the total value of the player's gift card. 
    

    Methods:
        __init__ : Constructor of the class
        Checks if the direction chosen by the player exists 
        in the current room's exits. If it does, changes the
        player's current room to the next room in that direction 
        and returns a description of the new room.
"""
#Define the constructor
    def __init__(self, name, hair, eyes, height, style, cart, total, gift_card, current_room, room_history):
        self.name = name
        self.hair = hair
        self.eyes = eyes
        self.height = height
        self.style = style
        self.total = 0
        self.gift_card=0 # Gift card value will be assigned later
        self.cart= {} # Initialize an empty list to hold the player's inventory
        self.current_room= None #By default, the player has no room assigned
        self.room_history= [] # Stack to track the history of visited rooms
    
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

    def add_item(self,item, price, quantity):
        """
    Adds item with thir price to cadi. 
    
    Parameters :
    item(str) : every item that the player selected 
    price(int) : the price of every item selected 
"""

        # Add or update the item in the cadi dictionary
        if self.name in self.cart:
            self.cart[self.name][1] += quantity  # Increment quantity
        else:
            self.cart[self.name] = [int(price), quantity]
        self.total += int(price) * quantity
        return f"{item} is added to your cart for {price}."

    def show_cart(self):
        """
    Displays the item in the player's cadi 

    Returns : A summary of the items.
        """
        if not self.cart: 
            return "Your cart is empty."
        all_items = "Items in your cart:\n"
        for items in self.cart.keys():
            return all_items 

    def assign_gift_card(self):
        """
    Assigns a random gift card value between 50 and 300 to the player.
        """
        import random  # Ensure the random module is imported
        self.gift_card=random.randint(50,300)








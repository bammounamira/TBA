# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.

from game import Game
from character import Character
from rooms import Room
import random
class Actions: 
    """
    A class that defines all the possible actions a player can take in the game.
    """
    def play(player, game):
        """
        Starts or restarts the game.

        Args:
            player (Player): The player object.
            game (Game): The game object, which contains the game world.

        Returns:
            str: A welcome message and instructions for the player.
        """
        # Reset the game
        game.setup()
        player.current_room = game.rooms[0]  # Assume the first room is the starting room
        player.cart = {}
        player.total = 0
        player.gift_card=random.randint(50,300)

        # Welcome message
        return (f"Welcome to MIMI, {player.name}! Your shopping adventure begins now. Your challenge is to shop wisely. Can you stay within your budget and find the perfect items?\n"
                f"You have a random gift card.\n"
                f"Explore the store, pick items you love, but don't exceed your budget!\n"
                f"You are currently in: {player.current_room.name}\n"
                f"{player.current_room.description}") 
  

    #define the move method 
    def move(player, direction):
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
        if direction in player.current_room.exits:
            player.current_room = player.current_room.exits[direction]
            return f"You move {direction}. {player.current_room.description}"
        return f"There is no exit to the {direction}."

    def take(player, item): 
        """
        Allows the player to take an item from the room.

        Args:
            player (Player): The player object.
            item (Item): The item to be taken.

        Returns:
            str: A message indicating the result of the action.
        """ 
        if item in player.current_room.inventory:
            player.add_item(item.name, item.price)
            self.total +=   # Update the total cost of items in the cadi
            return f"you have taken the {item.name}"
        return f"{item.name} is not in this room"
        
    def look(player):
        """
        Displays the items in the current room.

        Args:
            player (Player): The player object.

        Returns:
            str: A description of the room's inventory.
        """
        if not player.current_room.inventory: 
            return "The room is empty"
        return "You see the following items :\n" + "\n".join[item.name for item in player.current_room.inventory]"     
        
    def go(player,direction):
        """ 
        Allows the player to go a specific direction

        Args : 
            player (Player) : The player object.
            direction (str): The direction in which the player wants to move.

        Returns : 
            str : the player going to the direction desired 
        """
        if direction in player.current_room.exits:
            next_room = player.current_room.exits[direction]
            player.current_room = next_room
            return f"You go {direction}. You are now in {next_room.name}"
        return f"You can't go {direction}. There is no exit to the {direction}."
        
    def back(player, direction):
        """
        Allows the player to go to the previous room.

        Args: 
            player (Player) : the player object.
            direction (str): The direction in which the player wants to move.

        Returns : 
            str : the player going to the previous room 
        """
        if player.room_history:
            previous_room = player.room_history.pop()
            player.current_room=previous_room
            return f"You go back. You are now in {previous_room.name}."
        else:
            return "You can't go back. There is no previous room in your history."

    def drop(player, item): 
        """
        Allows the player to drop an item from the cart.

        Args:
            player (Player): The player object.
            item_name (Item): The name of the item to be dropped.

        Returns:
            str: A message indicating the result of the action.
        """ 
        if item_name in player.cart:
            del player.cart[item_name]
            player.total -= item_price  # Update the total cost of items in the cart
            return f"you have dropped the {item.name}"
        return f"{item.name} is not in your cart"

    def buy(player):
        """ 
        Finalizes the game and checks whether the player exceeded the gift card or not.

        Args: 
            player : the object player.
        
        Returns: 
            A message indicating whether the player succeded or failed. 
        """
        if player.total > player.gift_card :
            return (f"Game Over! Your cart total is {player.total}€, "
                f"but your gift card is only {player.gift_card}€. "
                "You exceeded your budget!")
        else : 
            return (f"Congratulations! You successfully completed your shopping.\n"
                    f"Cart total: {player.total}€\n"
                    f"Gift card value: {player.gift_card}€\n"
                    f"Remaining credit: {remaining_credit}€\n"
                    f"Thanks for playing!")
        
def receipt(player):
    """
    Displays a detailed summary of the player's cart without finalizing the purchase.

    Args:
        player (Player): The player object.

    Returns:
        str: A detailed receipt of the cart's contents and the total cost.
    """
    # Check if the cart is empty
    if not player.cart:
        return "Your cart is empty. Add some items before viewing the receipt!"

    # Build the receipt string
    receipt = "----- Receipt -----\n"
    for item_name, price in player.cart.items():
        receipt += f"{item_name}: {price}€\n"
    receipt += "-------------------\n"
    receipt += f"Cart Total: {player.total}€\n"
    receipt += f"Gift Card Value: {player.gift_card}€\n"
    receipt += f"Remaining Credit: {player.gift_card - player.total}€\n"
    receipt += "-------------------\n"
    
    return receipt        
        



























































































































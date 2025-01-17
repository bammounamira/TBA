"""
This module defines the Player class, which represents the player in the game.

The Player class includes attributes and methods to manage the player's
characteristics, current location, cart, and interactions with the game world.
"""

import random


class Player:
    """
    Represents the player of the game.

    Attributes:
        personal_info (dict): Dictionary containing personal
        attributes like name, hair, eyes, and height.
        style (str): The clothing style or appearance of the player.
        current_room (Room): The current room where the player is.
        cart (dict): The list of items the player has collected.
        Keys are items, values are [price, quantity].
        gift_card (int): The total value of the player's gift card.
        room_history (list): A stack to track the history of visited rooms.

    Methods:
        move(direction):
            Moves the player to the next room if the direction is valid.
        add_item(item, price, quantity):
            Adds an item with its price and quantity to the player's cart.
        show_cart():
            Displays the items in the player's cart.
        assign_gift_card():
            Assigns a random gift card value between 50 and 200 to the player.
    """

    def __init__(self,name: str, height: str, eyes: str, hair: str,style: str, current_room=None):
        """
        Initializes the Player instance.

        Args:
            name (str): The name of the player.
            hair (str): The hair color or style of the player.
            eyes (str): The eye color of the player.
            height (int): The height of the player in centimeters.
            style (str): The clothing style or appearance of the player.
            current_room (Room, optional): The initial room where the player starts.
            Defaults to None.
        """
        self.personal_info = {"name": name, "hair": hair, "eyes": eyes, "height": height}
        self.style = style
        self.cart = {}
        self.gift_card = random.randint(50, 200)
        self.current_room = current_room
        self.room_history = []

    def move(self, direction: str) -> str:
        """
        Moves the player in the specified direction if it exists.

        Args:
            direction (str): The direction in which the player wants to move.

        Returns:
            str: A description of the new room if the move is successful, or an error message.
        """
        if direction in self.current_room.exits:
            next_room = self.current_room.exits[direction]
            self.room_history.append(self.current_room)
            self.current_room = next_room
            return f"You move {direction}. {next_room.description}"
        return f"There is no exit to the {direction}."

    def add_item(self, item: str, price: int, quantity: int) -> str:
        """
        Adds an item with its price and quantity to the player's cart.

        Args:
            item (str): The item to add.
            price (int): The price of the item.
            quantity (int): The quantity of the item.

        Returns:
            str: Confirmation that the item has been added to the cart.
        """
        if item in self.cart:
            self.cart[item][1] += quantity
        else:
            self.cart[item] = [price, quantity]
        return f"{item} has been added to your cart for ${price} each (x{quantity})."

    def show_cart(self) -> str:
        """
        Displays the items in the player's cart.

        Returns:
            str: A summary of the items in the cart, or a message if the cart is empty.
        """
        if not self.cart:
            return "Your cart is empty."

        all_items = "Items in your cart:\n"
        for item, (price, quantity) in self.cart.items():
            all_items += f"  - {item}: ${price} x {quantity}\n"
        return all_items

    def assign_gift_card(self):
        """
        Assigns a random gift card value between 50 and 200 to the player.
        """
        self.gift_card = random.randint(50, 200)

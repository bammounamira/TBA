"""
This module defines the Item class, representing an item in an inventory system.

The Item class allows you to store details about an item, including its name, 
description, price, quantity, and discount, and provides methods to calculate 
the discounted price and check availability.
"""

class Item:
    """
    Represents an item with details such as name, description, price, quantity, and discount.

    Attributes:
        name (str): The name of the item.
        description (str): A brief description of the item.
        price (int): The price of the item (before any discount).
        quantity (int): The quantity of the item in stock.
        discount (float): The discount on the item as a percentage (default is 0).

    Methods:
        discounted_price():
            Calculates and returns the price of the item after applying the discount.
        is_available():
            Checks if the item is available in stock.
    """

    def __init__(self, name: str, description: str, price: int, discount: float, quantity: int):
        """
        Initializes an Item instance with name, description, price, quantity, and discount.

        Args:
            name (str): The name of the item.
            description (str): A brief description of the item.
            price (int): The price of the item (before any discount).
            discount (float): The discount on the item as a percentage.
            quantity (int): The quantity of the item in stock.
        """
        self.name = name.strip()
        self.description = description
        self.price = int(price)
        self.discount = discount
        self.quantity = int(quantity)

    def discounted_price(self) -> float:
        """
        Calculates the discounted price of the item.

        Returns:
            float: The price of the item after applying the discount.
        """
        return self.price * (1 - self.discount / 100)

    def is_available(self) -> bool:
        """
        Checks if the item is available in stock.

        Returns:
            bool: True if the item is available (quantity > 0), False otherwise.
        """
        return self.quantity > 0

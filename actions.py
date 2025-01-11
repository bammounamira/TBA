from character import Character
from room import Room
from Item import Item
import random
import threading
import time

class Actions:
    """
    A class that defines all the possible actions a player can take in the game.
    """
    timer_expired = False

    def play(self, player, game):
        """
        Starts or restarts the game.

        Args:
            player (Player): The player object.
            game (Game): The game object, which contains the game world.
        """
        # Start the timer
        timer_thread = threading.Thread(target=self.start_timer, args=(300, player, game))  # 5 minutes timer
        timer_thread.daemon = True  # Ensures the timer ends with the main program
        timer_thread.start()

        # Welcome message
        print(f"Welcome to MIMI, {player.name}! Your shopping adventure begins now.")
        print(f"You have a random gift card.")
        print(f"Explore the store, pick items you love, but stay within your budget!")
        print(player.current_room.get_long_description())

        # Game loop
        while not game.finished:
            command = input("> ").strip()
            if command:  # Avoid processing empty commands
                self.process_command(command, player, game)

    def process_command(self, command_string, player, game):
        """
        Process a command string entered by the player.
        """
        command_parts = command_string.split()
        command_word = command_parts[0]
        if command_word in ("inventory", "i"):
            self.inventory(player, game, command_parts[1:])
        if command_word in game.commands:
            game.commands[command_word].action(player, game, command_parts[1:])
        else:
            print(f"Command '{command_word}' not recognized. Type 'help' for available commands.")

    def move(self, player, game, args):
        """
        Checks if the direction chosen by the player exists in the current room's exits.
        If it does, changes the player's current room to the next room in that direction
        and returns a description of the new room. If the direction is invalid, returns
        an error message.

        Args:
            player (Player): The player object.
            game (Game): The game object.
            args (list): The arguments passed with the command.
        """
        directions = {
            "N": "N", "NORTH": "N", "North": "N", "north": "N",
            "E": "E", "EAST": "E", "East": "E", "east": "E",
            "S": "S", "SOUTH": "S", "South": "S", "south": "S",
            "W": "W", "WEST": "W", "West": "W", "west": "W", "w": "W"
        }
        if not args:
            print("You need to specify a direction.")
            return

        direction = directions.get(args[0].upper())
        if not direction:
            print("Invalid direction. Please choose N, E, S, or W.")
            return

        if direction in player.current_room.exits:
            player.current_room = player.current_room.exits[direction]
            print(f"You move {direction}. {player.current_room.description}")
        else:
            print(f"There is no exit to the {direction}.")

    def take(self, player, game, args):
        """
        Allows the player to take an item from the room, applying discounts if applicable.
        """
        if not args:
            print("You must specify an item to take.")
            return

        item_name = " ".join(args).strip().lower()
        current_room = player.current_room

        if not current_room.items:
            print("There are no items in this room.")
            return

        for item in current_room.items:
            if isinstance(item, Item) and item.name.strip().lower() == item_name:
                if item.quantity > 0:
                    discounted_price = item.price * (1 - item.discount / 100) if hasattr(item, 'discount') else item.price
                    if item.name in player.cart:
                        player.cart[item.name] = (player.cart[item.name][0] + 1, discounted_price)
                    else:
                        player.cart[item.name] = (1, discounted_price)

                    item.quantity -= 1
                    player.total += discounted_price
                    print(f"You have taken the {item.name} at {discounted_price:.2f}€ (discount applied).")
                    return

        print(f"The item '{item_name}' is not in this room or is out of stock.")

    def look(self, player, game, args):
        """
        Displays the items in the current room, including discounts if applicable.
        """
        current_room = player.current_room

        if not current_room.items:
            print("This room does not contain any items.")
        else:
            print("You see the following items:")
            for item in current_room.items:
                discount_info = f" (Discount: {item.discount}%)" if hasattr(item, 'discount') and item.discount > 0 else ""
                print(f"   - {item.name}: {item.description}, Quantity: {item.quantity}, Price: {item.price}€{discount_info}")

    def go(self, player, game, args):
        """
    Moves the player in a specified direction.

    Args:
        player (Player): The player object.
        game (Game): The game object.
        args (list): The arguments passed with the command, expected to include a direction.

    Behavior:
        - Checks if the direction is valid and if an exit exists in that direction.
        - Moves the player to the next room if possible.
        - Displays the new room's details or an error message if the move fails.
    """
    # Check if a direction is provided
        directions = {"N": "N", "NORTH": "N", "North": "N", "north": "N",
                "E": "E", "EAST": "E", "East": "E", "east": "E",
                "S": "S", "SOUTH": "S", "South": "S", "south": "S",
                "W": "W", "WEST": "W", "West": "W", "west": "W"
    }
        if not args:
            print("You need to specify a direction to go.")
            return

    # Get the next room
        direction = args[0].upper()  # Extract the direction
        direction=directions.get(direction) #extract the values of the dictionnary
        current_room = player.current_room
        next_room = current_room.get_exit(direction)        
        if next_room:
        # Update the player's location
            player.room_history.append(player.current_room)  # Keep track of room history for 'back' functionality
            player.current_room = next_room
            print(f"You move {direction}.")
            print(next_room.get_long_description())  # Display the details of the new room
        else:
            print(f"There is no exit to the {direction}.")



    def back(self, player, game, args):
        """
        Allows the player to go to the previous room.
        """
        if player.room_history:
            previous_room = player.room_history.pop()
            player.current_room = previous_room
            print(f"You go back. You are now in {previous_room.name}.")
        else:
            print("You can't go back. There is no previous room in your history.")

    def drop(self, player, game, args):
        """
    Allows the player to drop an item from the cart.

    Args:
        player (Player): The player object.
        game (Game): The game instance containing the game state.
        args (list): The arguments passed with the command, expected to include the item name.

    Behavior:
        - Removes the specified item from the cart if it exists.
        - Updates the room's inventory.
        - Displays a message if the item is not found in the cart.
    """
    # Check if the player specified an item
        if not args:
            print("You must specify an item to drop.")
            return

    # Combine the arguments into the full item name
        item_name = " ".join(args).strip().lower()

    # Check if the item is in the cart
        found_item = None
        for cart_item_name in player.cart.keys():
            if cart_item_name.strip().lower() == item_name:
                found_item = cart_item_name
                break

        if not found_item:
            print(f"The item '{item_name}' is not in your cart.")
            return

    # Remove the item from the cart
        quantity, price = player.cart[found_item]
        if quantity > 1:
            player.cart[found_item] = (quantity - 1, price)
        else:
            del player.cart[found_item]

        player.total -= price

    # Return the item to the room
        for item in player.current_room.items:
            if item.name.strip().lower() == item_name:
                item.quantity += 1
                print(f"You have dropped the '{item.name}'. It has been returned to the room.")
                return

        print(f"The item '{item_name}' has been removed from your cart but could not be returned to the room.")

    def start_timer(self, duration, player, game):
        """
        Starts a countdown timer for the game.

        Args:
            duration (int): The duration of the timer in seconds.
        """
        time.sleep(duration)
        Actions.timer_expired = True
        print("Time's up! Game Over.")
        game.finished = True

    def help(self, player, game, args):
        """
        Displays a detailed list of available commands, including their descriptions and usage.

        Args:
            player (Player): The player object.
            game (Game): The game instance containing all commands.
            args (list): The arguments passed with the command (unused).
        """
        print("Available commands:")
        print("-------------------")
        print("play: Start or restart the game.")
        print("move <direction>: Move in a specific direction (e.g., N, E, S, W).")
        print("take <item>: Pick up an item from the current room.")
        print("drop <item>: Drop an item from your cart into the room.")
        print("look: View the items in the current room.")
        print("go <direction>: Move to another")

    def buy(self,player,game,args):
        """ 
        Finalizes the game and checks whether the player exceeded the gift card or not.

        Args: 
            player : the object player.
        
        Returns: 
            A message indicating whether the player succeded or failed. 
        """
        if Actions.timer_expired:
            return ("Time's up! Your shopping adventure has ended. "
                    f"Cart total: {player.total}€\n"
                    f"Gift card value: {player.gift_card}€\n"
                    f"Remaining credit: {player.gift_card - player.total}€.\n"
                    "Thanks for playing!")
        if not isinstance(player.gift_card, (int, float)):
            player.gift_card = player.gift_card[0] if isinstance(player.gift_card, tuple) else 0  # Fix tuple issue
        remaining_credit = player.gift_card - player.total
        if player.total > player.gift_card :
            print (f"Game Over! Your cart total is {player.total}€, "
                f"but your gift card is only {player.gift_card}€. "
                "You exceeded your budget!")
        else : 
            print (f"Congratulations! You successfully completed your shopping without exceeding the random gift card.\n"
                f"Cart total: {player.total}€\n"
                f"Gift card value: {player.gift_card}€\n"
                f"Remaining credit: {remaining_credit}€\n"
                f"Thanks for playing See you next time!")
        game.finished=True
            ####

    def receipt(self,player,game,args):
        """
        Displays a detailed summary of the player's cart without finalizing the purchase.

        Args:
            player (Player): The player object.

        Returns:
            str: A detailed receipt of the cart's contents and the total cost.
        """
        # Check if the cart is empty
        if not player.cart:
            print ("Your cart is empty. Add some items before viewing the receipt!")

    # Build the receipt string
        receipt = "----- Receipt -----\n"
        for item_name, price in player.cart.items():
            receipt += f"{item_name}: {price}€\n"
        receipt += "-------------------\n"
        receipt += f"Cart Total: {player.total}€\n"
        receipt += "-------------------\n"
        print(receipt)        
        
    def quit(self,player,game,args):
        """
        Exists the game.

        Returns:
            str: A farewall message.
        """
        game.finished=True
        print("Thanks for playing! Goodbye!") 

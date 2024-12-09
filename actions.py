# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.

from character import Character
from room import Room
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
        # Reset the game
        #
        # game.setup()

        #Start the timer 
        timer_thread = threading.Thread(target=Actions.start_timer, args=(300,))  # 5 minutes timer
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
        if command_word in game.commands:
            game.commands[command_word].action(player, game, command_parts[1:])
        else:
            print(f"Command '{command_word}' not recognized. Type 'help' for available commands.")

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

    def take(player,game,args): 
            """

    Allows the player to take an item from the room.

    Args:
        player (Player): The player object.
        game (Game): The current game instance.
        args (list): The arguments passed with the command (e.g., item name).

    Returns:
        None
    """
            if not args:
                print("You must specify an item to take.")
                return

    # Combine all arguments into a single item name
            item_name = " ".join(args).strip().lower()  # Normalize and strip whitespace
            current_room = player.current_room

    # Ensure the room has items
            if not current_room.items:
                return


    # Search for the item in the current room
            for item in current_room.items:
                if item.name.strip().lower() == item_name:  # Ensure names are stripped and normalized
                    player.add_item(item.name,item.price,)  # Add item to player's cart
                    print(f"You have taken the {item.name}.")
                    return

    # If no match is found
            print(f"The item '{item_name}' is not in this room.")

    # If no match is found
           
            print(f"The item '{item_name}' is not in this room.")
            
    #if the player took the item

            if item in player.current_room.inventory:
                discounted_price=item.discounted_price()
                player.cart[item.name]=discounted_price
                player.total=player.total+discounted_price
                player.current_room.inventory.remove(item) # Retire l'objet de la pièce
                player.add_item(item.name, item.price)
                self.total += item.price   # Update the total cost of items in the cart
                return f"you have taken the {item.name}.Price: {[discounted_price].euros. TOtal: player.total}euros"

    def look(player, game, args):
            """
    Displays the items in the current room.
    """
            current_room = player.current_room

    # Check if there are items in the room
            if not current_room.items:
                print("This room does not contain any items.")
            else:
                print("You see the following items:")
            for item in current_room.items:
                print(f"   - {item.name}: {item.description}")
    
    def go(player, game, args):
        """
        Moves the player in a specified direction.
        """
        if not args:
            print("You need to specify a direction (N, E, S, W).")
            return

        direction = args[0].upper()  # Extract the direction
        current_room = player.current_room
        next_room = current_room.get_exit(direction)
        
        if next_room:
            player.current_room = next_room
            player.room_history.append(current_room)
            print(f"You moved to {next_room.name}.")
            print(next_room.get_long_description())
        else:
            print("You cannot go in that direction.")

    def back(player, game, args):
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
                print(f"You go back. You are now in {previous_room.name}.")  # Use f-string for dynamic room name
            else :
                print ("You can't go back. There is no previous room in your history.")

    def drop(player, game, args):
            """
        Allows the player to drop an item from the cart.

        Args:
            player (Player): The player object.
            game (Game): The current game instance.
            args (list): The arguments passed with the command (e.g., item name).

        Returns:
            None
    """
            if not args:
                print("You must specify an item to drop.")
                return

        # Combine all arguments into a single item name
            item_name = " ".join(args).strip()
            print(f"Attempting to drop '{item_name}' from cart.")

    # Check if the item exists in the cart
            if item_name in player.cart:
                item_price = player.cart[item_name]
                del player.cart[item_name]
                player.total -= item_price
                print(f"You have dropped the {item_name}.")
            else:
                print(f"{item_name} is not in your cart.")

    def buy(player,game,args):
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

    def receipt(player,game,args):
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
        




    def help():
                """
        Displays a list of available commands.

        Returns: 
            str: A help message listing all available commands.
            """
                return ("Available commands:\n"
                    "- stplayart : starts the game.\n"
                    "- move <direction>: Move in a specific direction.\n"
                    "- take <item>: Take an item from the room.\n"
                    "- drop <item>: Drop an item from your cart.\n"
                    "- look: Look around the room.\n"
                    "- go <direction>: Move to another room.\n"
                    "- back: Go back to the previous room.\n"
                    "- buy: Finalize your shopping.\n"
                    "- quit: Exit the game.")
    

    def start_timer(duration: int):
        global timer_expired
        time.sleep(duration)
        Actions.timer_expired = True
        print("\nTime's up! Your shopping adventure has ended. Let's see how you did.\n")


    def quit(player,game,number_of_arguments):
            """
    Exists the game.

    Returns:
        str: A farewall message.
    """
            game.finished=True
            print("Thanks for playing! Goodbye!") 

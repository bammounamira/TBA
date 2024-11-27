# Description: Game class

# Import modules
from room import Room
from player import Player
import random
from Item import Item 
from character import Character
from command import Command 
from actions import Actions 

class Game :
    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.direction_ensemble = set()

 # Setup the game
    def setup(self):

        # Setup commands
        help = Command("help", " : Display a list of available commands.", Actions.help, 0,"Shows all available commands and their descriptions.")
        self.commands["help"] = help
        quit = Command("quit", " : Exit the store.", Actions.quit, 0,"Ends the game and exits.")
        self.commands["quit"] = quit
        go = Command("go", " <direction> : Move to another section of the store (N, E, S, W).", Actions.go, 1,"Move in a specified direction (e.g., 'go north').")
        self.commands["go"] = go
        back = Command("back", " : Return to the previous section.", Actions.back, 0,"Returns to the previous room you visited.")
        self.commands["back"] = back
        look = Command("look", " : View the inventory of items in the current section.", Actions.look, 0,"Adds an item to your cart from the current room.")
        self.commands["look"] = look
        take = Command("take", " <item> : Pick up an item from the current section.", Actions.take, 1, "Adds an item to your cart from the current room.")
        self.commands["take"] = take
        drop = Command("drop", " <item> : Return an item to the current section.", Actions.drop, 1,"Removes an item from your cart and returns it to the room.")
        self.commands["drop"] = drop
        buy = Command("buy", ":Finalize your shopping.", Actions.buy, 0,"Finalize your shopping and check if you stayed within yoour budget")
        self.commands["buy"] = buy
        play= Command("play","Start or restart the game.", Actions.play,0,"plays the game")
        self.commands["play"]= play
        receipt= Command("receipt","Give you the receipt.", Actions.receipt,0,"Shows a summary of the items in your cart and the total")
        self.commands["receipt"]= receipt

#setup rooms
        hall_entry = Room("hall entry", "The welcoming entrance of the hall, adorned with elegant decor and a grand chandelier.","Asistant_sales", items=set(), exits={}
        )
        self.rooms.append(hall_entry)
        hall_center = Room("hall center", "The heart of the hall, filled with mannequins showcasing winter novelties.","Asistant_sales", items=set() , exits={}
        )
        self.rooms.append(hall_center)
        hall_exit = Room("hall exit", "The final part of the hall, leading to the rest of the store. Displays elegant accessories.","Asistant_sales", items=set() , exits={}
        )
        self.rooms.append(hall_exit)
        sweaters_section = Room("Sweaters Section", "A cozy section filled with winter sweaters and warm cardigans.",None,items=set(),exits={}
        )
        self.rooms.append(sweaters_section)
        coats_section = Room("Coats Section", "Discover a variety of winter coats, from elegant wool designs to trendy puffer jackets.",None,items=set(),exits={}
        )
        self.rooms.append(coats_section)
        jewelry = Room("Jewelry", "An elegant section showcasing sparkling jewelry pieces perfect for the winter season.",None,items=set(),exits={}
        )
        self.rooms.append(jewelry)
        sunglasses_section = Room("Sunglasses Section", "A bright corner featuring sunglasses designed to protect your eyes during snowy days.",None,items=set(),exits={}
        )
        self.rooms.append(sunglasses_section)
        shoes_section = Room("Shoes Section", "Explore a wide selection of winter boots, stylish heels, and cozy slippers.",None,items=set(),exits={}
        )
        self.rooms.append(shoes_section)
        bottoms_section = Room("Bottoms Section", "A trendy section featuring a variety of jeans, shorts, and skirts for every winter occasion.",None,items=set(),exits={}
        )
        self.rooms.append(bottoms_section)
        accessories_section = Room("Accessories Section", "A stylish corner showcasing scarves, gloves, hats, and other winter accessories.",None,items=set(),exits={}
        )
        self.rooms.append(accessories_section)
        tops_section = Room("Tops Section", "Explore an array of tops, from button-ups and t-shirts to trendy crop tops.",None,items=set(),exits={}
        )
        self.rooms.append(tops_section)
        checkout = Room("Checkout", "The final stop where customers can review their items and make their purchases.","Cashier",items=set(),exits={}
        )
        self.rooms.append(checkout)
        Game.rooms=[hall_entry,hall_exit,hall_center, coats_section, sweaters_section, tops_section, jewelry, shoes_section, accessories_section, sunglasses_section, bottoms_section, checkout]

 # Setup player and starting room

        self.player = Player(
            name=input("\nEnter your name: "),
            hair=input("\nEnter your hair color: "),
            eyes=input("\nEnter your eye color: "),
            height=int(input("\nEnter your height in cm: ")),
            style=input("\nEnter your style: "),
            cart={},
            total=0,
            gift_card=random.randint(50,200),
            current_room=None,
            room_history=[]
        )
        self.player.current_room = hall_entry


#Create exits for rooms
        hall_entry.exits={"N":hall_center, "S": None , "W":checkout, "E":coats_section}
        hall_center.exits={"N":hall_exit, "S": hall_entry , "W":sunglasses_section, "E":sweaters_section}
        hall_exit.exits={"N":accessories_section, "S": hall_center , "W":jewelry, "E":bottoms_section}
        coats_section.exits={"N":sweaters_section, "S": None , "W": hall_entry , "E": None}
        sweaters_section.exits={"N":bottoms_section, "S": coats_section, "W":hall_center , "E":None}
        tops_section.exits={"N":None, "S": bottoms_section , "W":accessories_section , "E": None}
        bottoms_section.exits={"N":tops_section, "S": sweaters_section , "W":hall_exit , "E": None}
        sunglasses_section.exits={"N":jewelry, "S": checkout , "W":shoes_section , "E": tops_section}
        accessories_section.exits={"N": None, "S": hall_exit , "W":shoes_section, "E":tops_section }
        jewelry.exits={"N":shoes_section, "S": sunglasses_section , "W":None, "E":hall_exit }
        shoes_section.exits={"N":None, "S": jewelry,"W":None, "E": accessories_section}
        checkout.exits={"N":sunglasses_section ,"S":None , "W":None , "E":hall_entry}
    

#Setup Items
        sweater= Item("A pink sweater", "A cozy pink sweater, perfect for staying warm on chilly days","15")
        turtleneck= Item("A blue turtleneck", "A stylish blue turtleneck that adds elegance to your winter wardrobe.","18")
        jumper= Item("A Christmas jumper", "A festive Christmas sweater featuring cheerful holiday patterns","20")
        sweatshirt= Item("A white sweatshirt", "A casual white sweatshirt, ideal for a relaxed and sporty look","12")
        coat = Item("A black coat", "A classic black coat, perfect for formal and casual winter outings", "25")
        puffer = Item("A green puffer jacket", "A warm green puffer jacket, ideal for chilly weather", "30")
        trench = Item("A beige trench coat", "A timeless beige trench coat for a sophisticated winter look", "35")
        fur_coat = Item("A brown fur coat", "A luxurious brown fur coat that combines style and warmth", "40")
        shirt = Item("A blue shirt", "A classic blue shirt, versatile for both formal and casual occasions", "14")        
        tshirt = Item("A mauve round-neck T-shirt", "A comfortable mauve T-shirt with a round neck, perfect for layering", "10")
        bandeau = Item("A red bandeau", "A vibrant red bandeau that adds a chic touch to your outfit", "8")
        croptop = Item("A pastel yellow crop top", "A trendy pastel yellow crop top, great for pairing with high-waisted pants", "12")
        jeans = Item("A blue baggy jean", "A relaxed-fit blue baggy jean for a laid-back and stylish look", "20")
        pants = Item("A black straight-leg pant", "A sleek black straight-leg pant, ideal for a professional or casual style", "18")
        shorts = Item("A bottle-green short", "A bottle-green short, perfect for a chic and comfortable summer look", "12")
        skirt = Item("A caramel skirt", "A caramel-colored skirt that exudes elegance and sophistication", "15")
        watch = Item("A gold watch", "A luxurious gold watch that complements any outfit with a touch of class", "40")
        earrings = Item("A pair of gold earrings", "Elegant gold earrings, perfect for adding sparkle to your look", "25")
        necklace = Item("A silver necklace", "A delicate silver necklace, a timeless piece for any occasion", "20")
        ring = Item("A gold ring", "A chic gold ring that adds a subtle but striking detail to your style", "18")
        scarf1 = Item("A grey scarf", "A soft grey scarf to keep you cozy and stylish in cold weather", "10")
        gloves = Item("Black gloves", "Classic black gloves that combine warmth and sophistication", "8")
        beanie = Item("A red beanie", "A warm and vibrant red beanie, perfect for chilly winter days", "6")
        scarf2 = Item("A khaki scarf", "A lightweight khaki scarf that adds a touch of elegance to your outfit", "9")
        square_sunglasses = Item("Black square sunglasses", "Stylish black square sunglasses that offer both sun protection and flair", "12")
        leopard_sunglasses = Item("Leopard rectangular sunglasses", "Trendy leopard-print rectangular sunglasses for a bold statement", "15")
        oversized_sunglasses = Item("Oversized sunglasses", "Chic oversized sunglasses that provide full coverage and timeless elegance", "18")
        heels = Item("Black heels", "Sophisticated black heels, perfect for formal events or nights out", "25")
        boots = Item("Brown boots", "Durable brown boots, ideal for keeping your feet warm and stylish", "30")
        sneakers = Item("White sneakers", "Comfortable and versatile white sneakers, perfect for any casual outfit", "20")
        slippers = Item("Pink slippers", "Cozy pink slippers, designed for ultimate comfort and relaxation at home", "10")
# Add items
        def add_items_to_room(room, items):
            """
    Ajoute des items à une room après avoir vérifié que 'items' est un set.
    """
            if isinstance(room, Room):
                if isinstance(room.items, set):
                    room.items.update(items)
                else:
                    print(f"Erreur : {room.name}.items is not a set ! Type actuel : {type(room.items)}")
            else:
                print(f"Erreur : L'objet passé n'est pas une instance de Room.")


# Ajoutez les items aux salles
        add_items_to_room(sweaters_section, {sweater, turtleneck, jumper, sweatshirt})
        add_items_to_room(coats_section, {coat, puffer, trench, fur_coat})
        add_items_to_room(bottoms_section, {jeans, pants, skirt, shorts})
        add_items_to_room(tops_section, {bandeau, tshirt, shirt, croptop})
        add_items_to_room(sunglasses_section, {leopard_sunglasses, square_sunglasses, oversized_sunglasses})
        add_items_to_room(accessories_section, {scarf1, scarf2, beanie, gloves})
        add_items_to_room(shoes_section, {heels, boots, slippers, sneakers})
        add_items_to_room(jewelry, {ring, necklace, earrings, watch})
        # Setup characters
        cashier = Character("Cashier", "The person handling payments.", checkout )
        Sales_Assistant= Character("Sales Assistant","The person who helps customers find products or provides assistance.", hall_entry)

"""
import time

class Game:
    def __init__(self):
        self.start_time = time.time()
        self.time_limit = 600  # 10 minutes in seconds

    def check_time(self):
        elapsed_time = time.time() - self.start_time
        remaining_time = self.time_limit - elapsed_time
        if remaining_time <= 0:
            self.finished = True
            return "Time's up! You couldn't complete your shopping in time. Game Over!"
        return f"Time remaining: {int(remaining_time)} seconds."
    import random

def random_event(player):
    events = [
        "discount", 
        "bonus", 
        "lost_item"
    ]
    event = random.choice(events)
    if event == "discount":
        return "Special Event: Discounts! All items in this section are now 50% off."
    elif event == "bonus":
        player.gift_card += 10
        return "Lucky Event: You found a bonus voucher worth 10€!"
    elif event == "lost_item" and player.cart:
        lost_item = random.choice(list(player.cart.keys()))
        del player.cart[lost_item]
        return f"Unfortunate Event: You lost '{lost_item}' from your cart."
    return "No events at this time."
    
    
    """

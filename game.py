"""
This module contains the Game class that configures and manages the game.

The Game class initializes commands, rooms, items, characters,
and allows a player to interact with the game's environment.
"""
import random
from room import Room
from player import Player
from item import Item
from character import Character
from command import Command
from actions import Actions

class Game :
    """
    Cette classe représente le jeu principal.

    Attributs :
        finished (bool) : Indique si le jeu est terminé.
        rooms (list) : Liste des salles du jeu.
        commands (dict) : Dictionnaire des commandes disponibles.
        player (Player) : Représentation du joueur.
        actions (Actions) : Actions disponibles dans le jeu.
    """
    def __init__(self):
        """
    Initializes the Game class.

    This constructor sets up the foundational attributes required to manage the 
    game's state, player interactions, available commands, and game world.

    Attributes:
        finished: Indicates whether the game has ended. Defaults to False.
        rooms: An empty list to hold Room objects.
        commands: An empty dictionary to map command names to their respective Command objects.
        player: Represents the player in the game.
        direction_ensemble: A set to store valid movement directions.
        actions: An instance of the Actions class, which contains methods that will be used.
        """
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.direction_ensemble = set()
        self.actions = Actions()

    def setup(self):
        """Initializes the game commands."""
        self.commands = {
            "help" : Command(
                "help", " : Display a list of available commands.",
                self.actions.help, 0,
                "Shows all available commands and their descriptions."),
            "quit" : Command(
                "quit", " : Exit the store.",
                self.actions.quit, 0,"Ends the game and exits."),
            "go" : Command(
                "go", " <direction> : Move to another section of the store (N, E, S, W).",
                self.actions.go, 1,"Move in a specified direction (e.g., 'go north')."),
            "back" : Command(
                "back", " : Return to the previous section.",
                self.actions.back, 0,"Returns to the previous room you visited."),
            "look" : Command(
                "look", " : View the inventory of items in the current section.",
                self.actions.look, 0,"Shows the items in the current_room."),
            "take" : Command( 
                "take"," <item> : Pick up an item from the current section.",
                self.actions.take, 1, "Adds an item to your cart from the current room."),
            "drop" : Command(
                "drop", " <item> : Return an item to the current section.",
                self.actions.drop, 1,"Removes an item from your cart and returns it to the room."),
            "buy" : Command(
                "buy", ":Finalize your shopping.",
                self.actions.buy, 0,
                "Finalize your shopping and check if you stayed within yoour budget"),
            "play" : Command(
                "play","Start or restart the game.",
                self.actions.play,0,"plays the game"),
            "receipt" : Command(
                "receipt","Give you the receipt.",
                self.actions.receipt,0,"Shows a summary of the items in your cart and the total"),
            "talk" : Command(
                "talk"," : Talk to a character in the current room.",
                self.actions.talk,1,
                "Talk to a character in the room to get information or interact.")}
        self._setup_rooms()
        self._setup_items()
        self._setup_characters()
        self._setup_player()
    def _setup_rooms(self):
        """Creates and connects the game rooms."""
        hall_entry=Room(
            "hall entry",
            "The welcoming entrance of the hall.",
            "Asistant",
            exits={}
        )
        hall_entry.items = set()
        self.rooms.append(hall_entry)
        hall_center = Room(
            "hall center",
            "The heart of the hall, filled with mannequins showcasing winter novelties.",
            "Asistant",
            exits={}
        )
        hall_center.items = set()
        self.rooms.append(hall_center)
        hall_exit = Room(
            "hall exit",
            "The final part of the hall, leading to the rest of the store.",
            "Asistant",
            exits={}
        )
        hall_exit.items = set()
        self.rooms.append(hall_exit)
        sweaters_section = Room(
            "Sweaters Section",
            "A cozy section filled with winter sweaters and warm cardigans.",
            None,
            exits={}
        )
        sweaters_section.items = set()
        self.rooms.append(sweaters_section)
        coats_section = Room(
            "Coats Section",
            "Discover a variety of winter coats,from wool designs to puffer jackets.",
            None,
            exits={}
        )
        coats_section.items = set()
        self.rooms.append(coats_section)
        jewelry = Room(
            "Jewelry",
            "An elegant section showcasing sparkling jewelry pieces perfect for the winter season.",
            None,
            exits={}
        )
        jewelry.items = set()
        self.rooms.append(jewelry)
        sunglasses_section = Room(
            "Sunglasses Section",
            "A bright corner featuring sunglasses designed to protect your eyes during snowy days.",
            None,
            exits={}
        )
        sunglasses_section.items = set()
        self.rooms.append(sunglasses_section)
        shoes_section = Room(
            "Shoes Section",
            "Explore a wide selection of winter boots, stylish heels, and cozy slippers.",
            None,
            exits={}
        )
        shoes_section.items = set()
        self.rooms.append(shoes_section)
        bottoms_section = Room("Bottoms Section",
        "A trendy section featuring a variety of jeans, shorts, and skirts.",
        None,
        exits={}
        )
        bottoms_section.items = set()
        self.rooms.append(bottoms_section)
        accessories_section = Room(
            "Accessories Section",
            "A stylish corner showcasing scarves, gloves, hats, and other winter accessories.",
            None,
            exits={}
        )
        accessories_section.items = set()
        self.rooms.append(accessories_section)
        tops_section = Room("Tops Section",
        "Explore an array of tops, from button-ups and t-shirts to trendy crop tops.",
        None,
        exits={}
        )
        tops_section.items = set()
        self.rooms.append(tops_section)
        checkout = Room(
            "Checkout",
            "The final stop where customers can review their items and make their purchases.",
            "Cashier",
            exits={}
        )
        checkout.items = set()
        self.rooms.append(checkout)
        self.rooms=[hall_entry,hall_exit,hall_center,
                    coats_section, sweaters_section, tops_section,
                    jewelry, shoes_section, accessories_section,
                    sunglasses_section, bottoms_section, checkout]
        hall_entry.exits={
            "N":hall_center,
            "S": None ,
            "W":checkout,
            "E":coats_section}
        hall_center.exits={
            "N":hall_exit,
            "S": hall_entry ,
            "W":sunglasses_section,
            "E":sweaters_section}
        hall_exit.exits={
            "N":accessories_section,
            "S": hall_center ,
            "W":jewelry,
            "E":bottoms_section}
        coats_section.exits={
            "N":sweaters_section,
            "S": None ,
            "W": hall_entry ,
            "E": None}
        sweaters_section.exits={
            "N":bottoms_section,
            "S": coats_section,
            "W":hall_center ,
            "E":None}
        tops_section.exits={
            "N":None,
            "S": bottoms_section ,
            "W":accessories_section ,
            "E": None}
        bottoms_section.exits={
            "N":tops_section,
            "S": sweaters_section ,
            "W":hall_exit ,
            "E": None}
        sunglasses_section.exits={
            "N":jewelry,
            "S": checkout ,
            "W":shoes_section ,
            "E": tops_section}
        accessories_section.exits={
            "N": None,
            "S": hall_exit ,
            "W":shoes_section,
            "E":tops_section }
        jewelry.exits={
            "N":shoes_section,
            "S": sunglasses_section ,
            "W":None,
            "E":hall_exit }
        shoes_section.exits={
            "N":None,
            "S": jewelry,
            "W":None,
            "E": accessories_section}
        checkout.exits={
            "N":sunglasses_section,
            "S":None,
            "W":None,
            "E":hall_entry}

    def _setup_player(self):
        """Initializes the player character"""
        self.player = Player(
            name=input("\nEnter your name: "),
            hair=input("\nEnter your hair color: "),
            eyes=input("\nEnter your eye color: "),
            height=int(input("\nEnter your height in cm: ")),
            style=input("\nEnter your style: "),
            cart={},
            total=0,
            gift_card=random.randint(50,200),
            current_room=self.rooms[0],
            room_history=[]
        )
        self.player.current_room =self.rooms[0]

    def _setup_items(self):
        """Adds items to rooms"""
        sweaters_items = {
        Item(
            "A pink sweater",
            "A cozy pink sweater, perfect for staying warm on chilly days",
            "15",
            10,
            10),
        Item(
            "A blue turtleneck",
            "A stylish blue turtleneck that adds elegance to your winter wardrobe.",
            "18",
            10,
            10),
        Item(
            "A Christmas jumper",
            "A festive Christmas sweater featuring cheerful holiday patterns",
            "20",
            10,
            10),
        Item(
            "A white sweatshirt",
            "A casual white sweatshirt, ideal for a relaxed and sporty look",
            "12",
            10,
            10)}
        self.rooms[4].items.update(sweaters_items)
        coats_items={
        Item(
            "A black coat", "A classic black coat, perfect for formal and casual winter outings",
            "25",
            5,
            10),
        Item(
            "A green puffer jacket", "A warm green puffer jacket, ideal for chilly weather",
            "30",
            5,
            10),
        Item(
            "A beige trench coat", "A timeless beige trench coat for a sophisticated winter look",
            "35",
            5,
            10),
        Item(
            "A brown fur coat", "A luxurious brown fur coat that combines style and warmth",
            "40",
            5,
            10)}
        self.rooms[3].items.update(coats_items)
        tops_items={
        Item(
            "A blue shirt", "A classic blue shirt,for formal and casual occasions",
            "14",
            5,
            10),
        Item(
            "A mauve round-neck T-shirt", "A comfortable mauve T-shirt with a round neck",
            "10",
            5,
            10),
        Item(
            "A red bandeau", "A vibrant red bandeau",
            "8",
            5,
            10),
        Item(
            "A pastel yellow crop top", "A trendy pastel yellow crop top",
            "12",
            5,
            10)}
        self.rooms[5].items.update(tops_items)
        bottoms_items={
        Item(
            "A blue baggy jean", "A relaxed-fit blue baggy jean for a laid-back look.",
            "20",
            5,
            10),
        Item(
            "A black straight-leg pant", "A sleek black straight-leg pant.",
            "18",
            5,
            10),
        Item(
            "A bottle-green short", "A bottle-green short,for a comfortable summer look",
            "12",
            5,
            10),
        Item(
            "A caramel skirt", "A caramel-colored skirt that exudes elegance",
            "15",
            5,
            10)}
        self.rooms[10].items.update(bottoms_items)
        jewelry={
        Item(
            "A gold watch", "A luxurious gold watch.",
            "40",
            30,
            10),
        Item(
            "A pair of gold earrings", "Elegant gold earrings, perfect for adding sparkle.",
            "25",
            30,
            10),
        Item(
            "A silver necklace", "A delicate silver necklace, a timeless piece for any occasion",
            "20",
            30,
            10),
        Item(
            "A gold ring", "A chic gold ring that adds a subtle but striking detail to your style",
            "18",
            30,
            10)}
        self.rooms[6].items.update(jewelry)
        accessories_items={
        Item(
            "A grey scarf", "A soft grey scarf to keep you cozy and stylish in cold weather",
            "10",
            30,
            10),
        Item(
            "Black gloves", "Classic black gloves that combine warmth and sophistication",
            "8",
            30,
            10),
        Item(
            "A red beanie", "A warm and vibrant red beanie, perfect for chilly winter days",
            "6",
            30,
            10),
        Item(
            "A khaki scarf",
            "A lightweight khaki scarf that adds a touch of elegance to your outfit",
            "9",
            30,
            10)}
        self.rooms[8].items.update(accessories_items)
        sunglasses_items={
        Item(
            "Black square sunglasses",
            "Stylish black square sunglasses that offer both sun protection and flair",
            "12",
            15,
            10),
        Item(
            "Leopard rectangular sunglasses",
            "Trendy leopard-print rectangular sunglasses for a bold statement",
            "15",
            15,
            10),
        Item(
            "Oversized sunglasses",
            "Chic oversized sunglasses that provide full coverage and timeless elegance",
            "18",
            15,
            10)}
        self.rooms[9].items.update(sunglasses_items)
        shoes_items={
        Item(
            "Black heels",
            "Sophisticated black heels, perfect for formal events or nights out",
            "25",
            20,
            10),
        Item(
            "Brown boots",
            "Durable brown boots, ideal for keeping your feet warm and stylish",
            "30",
            20,
            10),
        Item(
            "White sneakers",
            "Comfortable and versatile white sneakers, perfect for any casual outfit",
            "20",
            20,
            10),
        Item(
            "Pink slippers",
            "Cozy pink slippers, designed for ultimate comfort and relaxation at home",
            "10",
            20,
            10)}
        self.rooms[7].items.update(shoes_items)


    def _setup_characters(self):
        """
        Adds characters to rooms.
        """
        cashier = Character(
            "Cashier",
            "Manages payments and checks purchases.",
            self.rooms[2],
            dialogues=["Hello! Ready to check out?"],
        )
        assistant_sales = Character(
            "Assistant Sales",
            "Helps customers find products.",
            self.rooms[1],
            dialogues=["Can I help you find something?"],
        )
        self.rooms[11].character = cashier
        self.rooms[1].character = assistant_sales

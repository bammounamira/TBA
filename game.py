# Description: Game class

# Import modules
from room import Room
from player import Player

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
        help = Command("help", " : Display a list of available commands.", actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : Exit the store.", actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : Move to another section of the store (N, E, S, W).", actions.go, 1)
        self.commands["go"] = go
        back = Command("back", " : Return to the previous section.", actions.back, 0)
        self.commands["back"] = back
        check = Command("check", " : Check the description of the current section.", actions.check, 0)
        self.commands["check"] = check
        look = Command("look", " : View the inventory of items in the current section.", actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " <item> : Pick up an item from the current section.", actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " <item> : Return an item to the current section.", actions.drop, 1)
        self.commands["drop"] = drop
        buy = Command("buy", " <item> : Add an item to your shopping cart.", actions.buy, 1)
        self.commands["buy"] = buy
        checkout = Command("checkout", " : Proceed to the checkout to finalize your purchases.", actions.checkout, 0)
        self.commands["checkout"] = checkout

# Setup direction ensemble

    self.direction_ensemble.add("N")
    self.direction_ensemble.add("S")
    self.direction_ensemble.add("W")
    self.direction_ensemble.add("E")
    self.direction_ensemble.add("U")
    self.direction_ensemble.add("D")


 # Setup player and starting room

    self.player = Player(input("\nEnter your name: "))
    self.player.current_room = hall

# Setup rooms

    hall = Room("hall", "An inviting hall showcasing winter novelties with mannequins and elegant accessories.")
    self.rooms.append(hall)
    section_sweaters = Room("Sweaters Section", "A cozy section filled with winter sweaters and warm cardigans.")
    self.rooms.append(section_sweaters)
    section_coats = Room("Coats Section", "Discover a variety of winter coats, from elegant wool designs to trendy puffer jackets.")
    self.rooms.append(section_coats)
    jewelry = Room("Jewelry", "An elegant section showcasing sparkling jewelry pieces perfect for the winter season.")
    self.rooms.append(jewelry)
    section_sunglasses = Room("Sunglasses Section", "A bright corner featuring sunglasses designed to protect your eyes during snowy days.")
    self.rooms.append(section_sunglasses)
    section_shoes = Room("Shoes Section", "Explore a wide selection of winter boots, stylish heels, and cozy slippers.")
    self.rooms.append(section_shoes)
    section_bottoms = Room("Bottoms Section", "A trendy section featuring a variety of jeans, shorts, and skirts for every winter occasion.")
    self.rooms.append(section_bottoms)
    section_accessories = Room("Accessories Section", "A stylish corner showcasing scarves, gloves, hats, and other winter accessories.")
    self.rooms.append(section_accessories)
    section_tops = Room("Tops Section", "Explore an array of tops, from button-ups and t-shirts to trendy crop tops.")
    self.rooms.append(section_tops)
    checkout = Room("Checkout", "The final stop where customers can review their items and make their purchases.")
    self.rooms.append(checkout)

#Create exits for rooms 
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
    scarf = Item("A grey scarf", "A soft grey scarf to keep you cozy and stylish in cold weather", "10")
    gloves = Item("Black gloves", "Classic black gloves that combine warmth and sophistication", "8")
    beanie = Item("A red beanie", "A warm and vibrant red beanie, perfect for chilly winter days", "6")
    scarf = Item("A khaki scarf", "A lightweight khaki scarf that adds a touch of elegance to your outfit", "9")
    square_sunglasses = Item("Black square sunglasses", "Stylish black square sunglasses that offer both sun protection and flair", "12")
    leopard_sunglasses = Item("Leopard rectangular sunglasses", "Trendy leopard-print rectangular sunglasses for a bold statement", "15")
    oversized_sunglasses = Item("Oversized sunglasses", "Chic oversized sunglasses that provide full coverage and timeless elegance", "18")
    heels = Item("Black heels", "Sophisticated black heels, perfect for formal events or nights out", "25")
    boots = Item("Brown boots", "Durable brown boots, ideal for keeping your feet warm and stylish", "30")
    sneakers = Item("White sneakers", "Comfortable and versatile white sneakers, perfect for any casual outfit", "20")
    slippers = Item("Pink slippers", "Cozy pink slippers, designed for ultimate comfort and relaxation at home", "10")

    # Setup characters
    cashier = Character("Cashier", "The person handling payments at the checkout counter.", checkout )
    Sales_Assistant= Character("Sales Assistant","The person who helps customers find products or provides assistance.", hall)
    # Setup characters by location

    checkout.characters = {cashier}
    hall.characters={Sales_Assistant}
# Play the game

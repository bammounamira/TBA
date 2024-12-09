#from game import game 
class Character():

    def __init__(self, name, description, current_room):
        self.name= name
        self.description= description 
        self.current_room= current_room
        self.dialogues= dialogues
    
    def parler( self):
        for i, dialogue in enumerate(self.dialogues):
            print(f"{i+1}: {dialogue}")

    def interagir (self):
        print(f"{self.nom} dit : 'self.dialogues[0]'")

    pnjs = {
    "hall_entry": [
        PNJ("saleswoman", "a woman who is dressed with elegance"
            ["Welcome, Shopper.", "You can have acces to many articles."]),
       
    "": [
        PNJ("Fée des bois", "Une petite fée lumineuse.", 
            ["Prenez garde aux dangers dans la forêt.", "Les arbres parlent ici, écoutez bien."])
    ]
}

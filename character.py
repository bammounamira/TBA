#from game import game 
class Character():

    def __init__(self, name, description, current_room, dialogues):
        self.name= name
        self.description= description 
        self.current_room= current_room
        self.dialogues= dialogues
    
    def parler (self):
        for i, dialogues in enumerate (self.dialogues):
            print(f"{i+1}: {dialogue}")
    
    def interagir (self):
        print(f"{self.nom} dit: '{self.dialogues[0]}'")

    def afficher_characters(room):
        if room in characters :
            print(f"The characters are present in {self.room} are:")
            for i, characters in enumerate(character [self.room]):
                print(f"{i + 1}. {character.nom} - {character.description}")
        else:
            print("no charaters here")

    def interagir_avec_character(room, choix):
        if room in characters and 0 < choix <= len(characters[room]):
            characters[room][choix - 1].interagir()
        else:
            print("choice not valable.")
        
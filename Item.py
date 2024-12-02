#Description Item class
class Item():

    def __init__(self, name, description, price, discount=0):
        self.name= name
        self.description= description
        self.price= int(price)
        self.discount= discount

    def discounted_price(self):
        return self.price*(1-self.discount/100)
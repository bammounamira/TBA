#Description Item class
class Item():
    def __init__(self, name, description, price, quantity, discount=0):
        self.name = name.strip()
        self.description = description
        self.price = int(price)
        self.discount = discount
        self.quantity = int(quantity)


    def discounted_price(self):
        return self.price*(1-self.discount/100)
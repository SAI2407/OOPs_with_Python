from item import Item


# Subclass for Laptops
class Laptop(Item):
    def __init__(self, name: str, price: float, quantity=0, ram: str = "8GB"):

        

        super().__init__(name, price, quantity)
        self.ram = ram
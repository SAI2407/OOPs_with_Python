from item import Item

# Subclass for Keyboards
class Keyboard(Item):
    def __init__(self, name: str, price: float, quantity=0, layout: str = "QWERTY"):
        super().__init__(name, price, quantity)
        self.layout = layout
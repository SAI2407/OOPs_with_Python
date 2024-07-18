# Inventory class to manage all items
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        
        self.items.append(item)

    def calculate_inventory_value(self):
        total_value = 0
        for item in self.items:
            total_value += item.calculate_total_price()
        return total_value

    def apply_discounts(self):
        for item in self.items:
            item.apply_discount()

    def display_inventory(self):
        for item in self.items:
            print(item)
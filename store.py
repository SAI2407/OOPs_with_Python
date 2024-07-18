from inventory import Inventory

# Shop class to manage the shop operations
class Store:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()

    def add_item_to_inventory(self, item):
        self.inventory.add_item(item)

    def calculate_total_inventory_value(self):
        return self.inventory.calculate_inventory_value()

    def apply_discounts_to_inventory(self):
        self.inventory.apply_discounts()

    def display_shop_inventory(self):
        print(f"Inventory for {self.name}:")
        self.inventory.display_inventory()

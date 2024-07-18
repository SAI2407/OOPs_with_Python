from item import Item
from phone import Phone
from inventory import Inventory
from store import Store
from laptop import Laptop
from keyboard import Keyboard



# Example usage
shop = Store("Tech Store")

# Adding different items to the shop's inventory
phone1 = Phone("iPhone 13", 999.99, 5, "5g")

laptop1 = Laptop("MacBook Pro", 1999.99, 3, "16GB")

keyboard1 = Keyboard("Mechanical Keyboard", 149.99, 10, "QWERTY")


shop.add_item_to_inventory(phone1)
shop.add_item_to_inventory(laptop1)
shop.add_item_to_inventory(keyboard1)

# Displaying the inventory before applying discounts
shop.display_shop_inventory()

# Applying discounts to all items in the inventory
shop.apply_discounts_to_inventory()

# Displaying the inventory after applying discounts
shop.display_shop_inventory()

# Calculating the total value of the inventory
total_value = shop.calculate_total_inventory_value()
print(f"Total inventory value: ${total_value:.2f}")

            
        



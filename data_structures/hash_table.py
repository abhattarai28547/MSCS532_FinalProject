# Dictionary to simulate a hash table for inventory management
inventory = {}

# Function to add items to the inventory
def add_item(product_id, quantity):
    inventory[product_id] = quantity

# Function to retrieve the quantity of a product in the inventory
def get_item(product_id):
    return inventory.get(product_id, None)

# Example usage:
add_item('Product1', 50)
add_item('Product2', 30)

print(get_item('Product1'))  # Output: 50
print(get_item('Product3'))  # Output: None (Product not found)
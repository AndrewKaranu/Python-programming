import json

# Load inventory from file or create an empty dictionary if file does not exist
try:
    with open("inventory.json", "r") as f:
        inventory = json.load(f)
except FileNotFoundError:
    inventory = {}

def save_inventory():
    with open("inventory.json", "w") as f:
        json.dump(inventory, f)

def exit_gracefully():
    print("Saving inventory...")
    save_inventory()
    print("Goodbye!")
    exit()

def checkout(inventory, items, ammount):
    total_cost = 0.0
    for item in items:
        if item in inventory and inventory[item]["quantity"] >= items[item]:
            inventory[item]["quantity"] -= items[item]
            total_cost += inventory[item]["price"] * items[item]
            VAT = 0.16*total_cost
            total_cost_VAT = total_cost+VAT
            change = ammount-total_cost_VAT
            
        elif item in inventory and inventory[item]["quantity"] < items[item]:
            print(f"Sorry, there are not enough {item}(s) in inventory.")
        else:
            print(f"Item {item} not found in inventory.")
    print(f"Total cost: ${total_cost_VAT}")
    print(f"The customers change is {change}")
    

def add_to_inventory(item, quantity, price):
    if item in inventory:
        inventory[item]["quantity"] += quantity
    else:
        inventory[item] = {"quantity": quantity, "price": price}
    print(f"Added {quantity} {item}(s) to inventory.")

def remove_from_inventory(item, quantity):
    if item in inventory and inventory[item]["quantity"] >= quantity:
        inventory[item]["quantity"] -= quantity
        print(f"Removed {quantity} {item}(s) from inventory.")
    elif item in inventory and inventory[item]["quantity"] < quantity:
        print(f"Sorry, there are not enough {item}(s) in inventory.")
    else:
        print(f"Item {item} not found in inventory.")

def print_inventory():
    print("Inventory:")
    for item, details in inventory.items():
        print(f"{item} - Quantity: {details['quantity']}, Price: ${details['price']}")

items = {}
while True:
    print("Please choose an option:")
    print("1. Checkout")
    print("2. Add to inventory")
    print("3. Remove from inventory")
    print("4. Print inventory")
    print("5. Exit")
    choice = input("> ")

    if choice == "1":
        while True:
            item = input("Enter an item (or 'done' to finish): ")
            if item == "done":
                break
            quantity = int(input("Enter the quantity: "))
            items[item] = quantity
            change = int(input("How much did the customer give?"))
        checkout(inventory, items, change)
        items = {}  
    elif choice == "2":
        item = input("Please enter the item name: ")
        quantity = int(input("Please enter the quantity: "))
        price = float(input("Please enter the price: "))
        add_to_inventory(item, quantity, price)
    elif choice == "3":
        item = input("Please enter the item name: ")
        quantity = int(input("Please enter the quantity: "))
        remove_from_inventory(item, quantity)
    elif choice == "4":
        print_inventory()
    elif choice == "5":
        exit_gracefully()
    else:
        print("Invalid choice. Please try again.")

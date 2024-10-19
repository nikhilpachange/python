class Item:
    def __init__(self, item_id, name, quantity, price):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def display_info(self):
        print(f"Item ID: {self.item_id}")
        print(f"Name: {self.name}")
        print(f"Quantity: {self.quantity}")
        print(f"Price: {self.price}")
        print("-" * 30)

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Item {item.name} added successfully.")

    def remove_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                self.items.remove(item)
                print(f"Item ID {item_id} removed successfully.")
                return
        print(f"Item ID {item_id} not found.")

    def view_inventory(self):
        if not self.items:
            print("No items in the inventory.")
        else:
            print("Inventory List:")
            for item in self.items:
                item.display_info()

def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Inventory")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item_id = input("Enter Item ID: ")
            name = input("Enter Item Name: ")
            quantity = int(input("Enter Item Quantity: "))
            price = float(input("Enter Item Price: "))
            item = Item(item_id, name, quantity, price)
            inventory.add_item(item)
        elif choice == '2':
            item_id = input("Enter Item ID to remove: ")
            inventory.remove_item(item_id)
        elif choice == '3':
            inventory.view_inventory()
        elif choice == '4':
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

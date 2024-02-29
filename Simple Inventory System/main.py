# main.py RoboGarden Simple System
# Demian Swindells 2/28/2024
# Create a simple inventory system that manages information about products in a store.
# Each product should have specified attributes like name, price, and quantity.
# Use classes to represent products and include methods for displaying product information, updating quantities, and calculating the total value of the inventory.

class Product:
 
  # Constructor
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Function to display product details
    def display_info(self, prod):
        print("Name : ", prod.name)
        print("Price : ", prod.price)
        print("Quantity : ", prod.quantity)
        print("\n")

    #  Function to create and add a new product item
    def add_product(self, name, price, quantity):
        prod = Product(name, price, quantity)
        lst.append(prod)

    # Function to update Product Quantity for sale
    def sell_product(self, prod, qty):
        if qty < prod.quantity:
            prod.quantity = 0
        else:
            prod.quantity -= qty
        print("Quantity of Product Sale Updated")

    # Function to update Product Quantity for stock
    def stock_product(self, prod, qty):
        prod.quantity += qty
        print("Quantity of Product Restock Updated")

    # Function to calculate total value of products
    def calc_value(self, prod):
        val = prod.price * prod.quantity
        print("val: ", val)
        print("price: ", self.price)
        print("qty: ", self.quantity)
        return val

# Create list to stor books
lst = []

# create objet of the Books Class
obj = Product("", 0, 0)

run = True
while run:
    user_input = input("Please make a choice: stop, view, add, sell, stock, value: ")

    if user_input == "stop":
        run = False
        break
    elif user_input == 'add':
        name = input("Enter Product Name: ")
        price = int(input("Enter Product Price: "))
        quantity = int(input("Enter Product Quantity: "))
        obj.add_product(name, price, quantity)
        continue
    elif user_input == 'view':
        print("\n")
        print("\nList of Products\n")
        for i in range(lst.__len__()):
            obj.display_info(lst[i])
        continue
    elif user_input == 'sell':
        prod = input("Please Enter the name of the product that was sold: ")
        for i in range(lst.__len__()):
            if prod == lst[i].name:
                qty = int(input("Please enter the amount of the product sold: "))
                obj.sell_product(lst[i], qty)
    elif user_input == 'stock':
        prod = input("Please Enter the name of the product that was restocked: ")
        for i in range(lst.__len__()):
            if prod == lst[i].name:
                qty = int(input("Please Enter the quantity of the Product Re-Stocked"))
                obj.stock_product(lst[i])
    elif user_input == 'value':
        total_val = 0
        for i in range(lst.__len__()):
            total_val += obj.calc_value(lst[i])
            print("i: ", i)
            print("TV: ", total_val)
        print("The Total Vlaue of all the Products is: ", total_val)
    else:
        print("Please choose from the list provided")
        continue
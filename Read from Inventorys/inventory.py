import os
from tabulate import tabulate

# Define the Shoe class
class Shoe:
    # Shoe class is the blueprint for creating shoe objects. Each shoe
    # object will have the following attributes.
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        # Returns the cost of the shoe
        return self.cost

    def get_quantity(self):
        # Returns the quantity of the shoe in stock
        return self.quantity

    def __str__(self):
        # Returns a string to represent the shoe object
        return (
            f"{self.country}, "
            f"{self.code}, "
            f"{self.product}, "
            f"{self.cost}, "
            f"{self.quantity} "
        )

# Global variable to store shoe objects from inventory.txt file
shoes_list = []

# Function to read data from inventory.txt
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()[1:]  # Skip the first line (header)
            for line in lines:
                # Split each line by commas to attract the attributes
                country, code, product, cost, quantity = line.strip().split(",")
                shoe = Shoe(country, code, product, cost, quantity)
                shoes_list.append(shoe)
    # Error handling, if the file is not found it prompts the user with
    # a message.
    except FileNotFoundError:
        print("Error: File 'inventory.txt' not found.")

# Allows the user to input new shoe data and adds it to shoes_list.
def capture_shoes():
    # Prompt the user to enter the shoe information.
    # Create a shoe object using the users input.
    # Append the new shoe object to shoes_list.
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product: ")
    cost = float(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))
    shoe = Shoe(country, code, product, cost, quantity)
    shoes_list.append(shoe)
    print("Shoe data captured successfully!")

    # Append the new shoe data to the inventory.txt file
    # Error handling if the writing to file fails.
    # This was not asked in the task and I was unsure if I must ad it.
    try:
        with open("inventory.txt", "a") as file:
            file.write(f"{country},{code},{product},{cost},{quantity}\n")
        print("Shoe data added to inventory.txt successfully!")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def view_all():
    # Displays all shoes in a tabular format using the tabulate module.
    # Checks if the shoe list is empty if it is the message will be prompt.
    # Use the tabulate module to print it into a table.
    if not shoes_list:
        print("No shoes available.")
        return
    table = []
    for shoe in shoes_list:
        table.append([shoe.country, shoe.code, shoe.product, shoe.cost,
                      shoe.quantity])
    print(tabulate(table, headers=["Country", "Code", "Product", "Cost",
                                   "Quantity"], tablefmt="grid"))

def re_stock():
    # Find the shoe with the lowest quantity using the min function and a
    # lambda function as the key.
    # Display the shoe details to the user.
    # Ask the user how many units they want to add.
    # Update the shoe's quantity in shoes_list.
    # Write the updated data back to inventory.txt.
    if not shoes_list:
        print("No shoes available.")
        return
    lowest_quantity_shoe = min(shoes_list, key=lambda x: x.get_quantity())
    print(f"Shoe with the lowest quantity: {lowest_quantity_shoe}")
    choice = input("Do you want to add more quantity? (yes/no): ").lower()
    if choice == "yes":
        try:
            additional_quantity = int(input("Enter the quantity to add: "))
            lowest_quantity_shoe.quantity += additional_quantity
            print("Quantity updated successfully!")
            # Update the file
            with open("inventory.txt", "r") as file:
                lines = file.readlines()
            with open("inventory.txt", "w") as file:
                for line in lines:
                    data = line.strip().split(",")
                    if data[1] == lowest_quantity_shoe.code:
                        data[4] = str(lowest_quantity_shoe.quantity)
                        line = ",".join(data) + "\n"
                    file.write(line)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("No changes made.")


# Function to search for a shoe by code
def search_shoe():
    # Prompt the user to enter a shoe code.
    # Iterate through shoes_list to find a shoe with a matching code.
    # If found, print the shoe's details using the __str__ method.
    # If not found, print a "Shoe not found" message.
    code = input("Enter the shoe code to search: ")
    for shoe in shoes_list:
        if shoe.code == code:
            print(shoe)
            return
    print("Shoe not found.")

# Function to calculate and displays the total value (cost * quantity)
# for each shoe.
def value_per_item():
    # Iterate through shoes_list.
    # For each shoe, calculate the value using the formula value =
    # cost * quantity.
    # Print the shoe's name, code, and total value.
    if not shoes_list:
        print("No shoes available.")
        return
    table = []
    for shoe in shoes_list:
        value = shoe.get_cost() * shoe.get_quantity()
        table.append([shoe.product, shoe.code, value])
    print(tabulate(table, headers=["Product", "Code", "Total Value"],
                   tablefmt="grid"))

# Function to Finds and displays the shoe with the highest quantity.
def highest_qty():
    # Find the shoe with the highest quantity using the max function and
    # a lambda function as the key.
    # Print the shoe's details with a message indicating it is for sale.
    if not shoes_list:
        print("No shoes available.")
        return
    highest_quantity_shoe = max(shoes_list, key=lambda x: x.get_quantity())
    print(f"Shoe with the highest quantity "
          f"is (for sale): {highest_quantity_shoe}")

# Main menu
# A while loop provides a menu-driven interface for the user to interact
# with the program.
def main():
    read_shoes_data()  # Load data at the start
    while True:
        print("\n===== Shoe Inventory Management =====")
        # User chooses a number 1-7
        choice = input('''Select one of the following options:
1. Capture New Shoe
2. View All Shoes
3. Re-stock Shoes
4. Search for a Shoe
5. Calculate Value per Item
6. Find highest quantity shoe
7. Exit
: ''')
    # Based on the number the user entered the functioned will be called.
        if choice == "1":
            capture_shoes()

        elif choice == "2":
            view_all()

        elif choice == "3":
            re_stock()

        elif choice == "4":
            search_shoe()

        elif choice == "5":
            value_per_item()

        elif choice == "6":
            highest_qty()

        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            # If the users input is anything else than 1-7 the user will
            # receive a invalid choice message
            print("Invalid choice. Please try again")

# Run the program
if __name__ == "__main__":
    main()

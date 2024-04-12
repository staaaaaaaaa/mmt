from inventory import *

### creating an initial inventory
inventory = Inventory([ 
    Product("Apple", 100, 5, 8),
    Product("Banana", 50, 10, 12),
    Product("Orange", 75, 6, 78),
    Product("Babyoil", 15, 2, 3),
    Product("Bread", 150, 1.5, 2.5),
    Product("Eggs", 100, 0.5, 0.8),
    Product("Dogfood", 50, 3, 5),
    Product("Shampoo", 300, 4, 6),
    Product("Tomato", 80, 0.5, 0.8),
    Product("Potato", 120, 0.3, 0.5)

])

def get_numeric_input(prompt):
    """
    Get numeric input from the user with input validation.

    Parameters:
    - prompt (str): The prompt message for the user input

    Returns:
    - float: The validated numeric input
    """
    while True:
        user_input = input(prompt)
        if not user_input.replace('.', '', 1).isdigit():
            print("Invalid input. Please enter a numeric value.")
        else:
            return float(user_input)
            break


# Displaying a welcome message
print("""
█▀▀ █▀█ █▀█ █▀▀ █▀▀ █▀█ █▄█ █░█ ▄▀█ █░░ █░░
█▄█ █▀▄ █▄█ █▄▄ ██▄ █▀▄ ░█░ ▀▀█ █▀█ █▄▄ █▄▄
      """)

print("""==============BOOKING SYSTEM==============""")

# Main program loop
while True:
    print('\nChoose a section to continue.')

    # Displaying options for the user to choose from
    print("""1. Inventory management: View, add, restock and sell products.
2. Transactions management: View transactions and financial metrics.
3. Exit.
          """)

    section = input("Enter your choice: ")

    if section == '1':
        print("""1. Show Inventory
2. Add New Product
3. Restock Product
4. Sell Product            
          """)
        choice = input("Enter your choice: ")

        # Handling user choices for inventory management
        if choice == '1':
            inventory.print_list_of_products()
            
        elif choice == '2':
            # Adding a new product to the inventory
            name = input("Enter product name: ")
            quantity = get_numeric_input("Enter product quantity: ")
            price_purchase = get_numeric_input("Enter purchase price: ")
            price_sell = get_numeric_input("Enter selling price: ")

            new_product = Product(name, int(quantity), float(price_purchase), float(price_sell))
            inventory.add_new_product_to_inventory(new_product)

        elif choice == '3':
            # Restocking an existing product
            product_name = input("Enter product name to restock: ")
            added_items = get_numeric_input("Enter quantity to add: ")

            inventory.restock_product(product_name, int(added_items))
            
        elif choice == '4':
            # Selling a product
            product_name = input("Enter product name to sell: ")
            sold_items = get_numeric_input("Enter quantity to sell: ")

            inventory.sell_product_stock(product_name, int(sold_items))

    if section == '2':
        print("""1. Show Last Transactions
2. Show Financial Report (all financial metrics)
3. Show Revenue
4. Show Costs
5. Show Profit 
6. Calculate Inventory Value            
          """)
        choice = input("Enter your choice: ")

        # Handling user choices for transactions management
        if choice == '1':
            inventory.print_transactions_logs()
        elif choice == '2':
            inventory.print_financial_report()
        elif choice == '3':
            print(f"Revenue: {inventory.revenue}")
        elif choice == '4':
            print(f"Costs: {inventory.costs}")
        elif choice == '5':
            print(f"Profit: {inventory.revenue - inventory.costs}")
        elif choice == '6':
            ids = input("Enter ids separated by comma or skip to calculate all: ")
            print(f"Inventory Value: {inventory.calculate_inventory_value(ids)}")

    # Exiting the program
    elif section == '3':
        print("============== Have a nice day! ==============")
        break
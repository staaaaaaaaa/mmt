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


print("""
█▀▀ █▀█ █▀█ █▀▀ █▀▀ █▀█ █▄█ █░█ ▄▀█ █░░ █░░
█▄█ █▀▄ █▄█ █▄▄ ██▄ █▀▄ ░█░ ▀▀█ █▀█ █▄▄ █▄▄
      """)

print("""==============BOOKING SYSTEM==============""")

# Main program loop

while True:
    print('Choose a section to continue.')

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
        if choice == '1':
            inventory.print_list_of_products()
        elif choice == '2':
            name = input("Enter product name: ")

            # Input validation for quantity
            while True:
                quantity = input("Enter product quantity: ")
                if not quantity.isdigit():
                    print("Invalid input. Quantity should be numeric.")
                else:
                    break

            # Input validation for purchase price
            while True:
                price_purchase = input("Enter purchase price: ")
                if not price_purchase.replace('.', '', 1).isdigit():
                    print("Invalid input. Purchase price should be numeric.")
                else:
                    break

            # Input validation for selling price
            while True:
                price_sell = input("Enter selling price: ")
                if not price_sell.replace('.', '', 1).isdigit():
                    print("Invalid input. Selling price should be numeric.")
                else:
                    break

            new_product = Product(name, int(quantity), float(price_purchase), float(price_sell))
            inventory.add_new_product_to_inventory(new_product)
        elif choice == '3':
            product_name = input("Enter product name to restock: ")

            # Input validation for added quantity
            while True:
                added_items = input("Enter quantity to add: ")
                if not added_items.isdigit():
                    print("Invalid input. Quantity should be numeric.")
                else:
                    break

            inventory.restock_product(product_name, int(added_items))
            
        elif choice == '4':
            product_name = input("Enter product name to sell: ")

            # Input validation for sold quantity
            while True:
                sold_items = input("Enter quantity to sell: ")
                if not sold_items.isdigit():
                    print("Invalid input. Quantity should be numeric.")
                else:
                    break

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

    elif section == '3':
        print("============== Have a nice day! ==============")
        break
    else:
        print("Invalid choice. Please try again.")
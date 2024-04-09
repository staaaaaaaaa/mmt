from tabulate import tabulate, SEPARATING_LINE
from datetime import datetime 

class Product:
    last_id = 0  # variable to keep track of the last product ID and regenerate it

    def __init__(self, name, quantity, price_purchase, price_sell):
        """
        Initialize a new Product object with the given attributes.

        Parameters:
        name (str): The name of the product
        quantity (int): The quantity of the product
        price_purchase (float): The purchasing price of the product
        price_sell (float): The selling price of the product
        """
        Product.last_id += 1
        self.id = Product.last_id
        self.name = name
        self.quantity = quantity
        self.price_purchase = price_purchase
        self.price_sell = price_sell

class Inventory:
    def __init__(self, inventory):
        """
        Initialize the Inventory object with the given inventory list.

        Parameters:
        inventory (list): The list of Product objects
        """
        self.inventory = inventory
        self.inventory_logs = []  # list to store transaction logs for selling, restocking and adding

        self.revenue = 0  # initialize revenue to 0
        self.costs = 0  # initialize costs to 0

    def add_new_product_to_inventory(self, product_new):
        """
        Add a new product to the inventory.

        Parameters:
        product_new (Product): The new product to be added
        """
        log = f'Unsuccessful transaction. Could not add product {product_new}. Try again.'
        for product in self.inventory:
            if product.name == product.name: # catching attempts to add existing product 
                log = 'Product with the same name exists. Try again.'
        if product_new.name != "": 
            self.inventory.append(product_new) # adding Product to the list of product inventory
            log = f"Added new product {product_new.name}: {product_new.quantity}"
            self.costs += product_new.quantity * product_new.price_purchase # updating costs
        self.inventory_logs.append({'date': datetime.now(), 'transaction': log}) # saving adding trasaction  
        print(log)

    def restock_product(self, product_name, added_items):
        """
        Restock a product in the inventory.

        Parameters:
        product_name (str): The name of the product to restock
        added_items (int): The quantity to add to the stock
        """
        log = f'Unsuccessful transaction. {product_name} not found in the inventory. Try again or add product.'
        for product in self.inventory: 
            if product.name == product_name: # going through the list of products and finding needed one for updating
                product.quantity += added_items
                log = f"Added new stock for {product_name}: {product.quantity - added_items} -> {product.quantity}"
                self.costs += product.quantity * product.price_purchase # updating costs
        self.inventory_logs.append({'date': datetime.now(), 'transaction': log}) # saving restocking trasaction  
        print(log)

    def sell_product_stock(self, product_name, sold_items):
        """
        Sell a product from the inventory.

        Parameters:
        product_name (str): The name of the product to be sold
        sold_items (int): The quantity to be sold
        """
        log = f'Unsuccessful transaction. {product_name} not found in the inventory. Try again or add product.'
        for product in self.inventory:
            if product.name == product_name and product.quantity >= sold_items: # checking whenever the product can be sold or not
                product.quantity -= sold_items
                log = f"Sold {product_name}: {product.quantity + sold_items} -> {product.quantity}" 
                self.revenue += product.quantity * product.price_sell # updating revenue
            elif product.name == product_name and product.quantity < sold_items:
                log = f"Unsuccessful transaction. Not enough stock to sell {sold_items} of {product_name}: {product.quantity}" 
        self.inventory_logs.append({'date': datetime.now(), 'transaction': log}) # saving selling trasaction  
        print(log)



    def calculate_inventory_value(self, user_ids=''):
        """
        Calculate the total value of the inventory.

        Parameters:
        user_ids (str): Commaseparated string of product IDs to calculate specific inventory value

        Returns:
        float: Total value of the inventory
        """
        if len(user_ids) == 0: # if user didn't specify the ids the whole inventory's value will be printed
            ids = [product.id for product in self.inventory]
        else:
            ids = [int(id) for id in user_ids.replace(' ','').split(',')]
        return (sum([product.quantity * product.price_purchase  for product in self.inventory if product.id in ids]))


    def print_list_of_products(self):
        """Print a table of all products in the inventory."""
        inventory_table = []
        for product in self.inventory:
            inventory_table.append({k: v for i, (k, v) in enumerate(vars(product).items())}) 
        print(tabulate(inventory_table, headers='keys'))
    

    def print_transactions_logs(self):
        """Print a table of all transaction logs."""
        print(tabulate(self.inventory_logs, headers='keys'))

    def print_financial_report(self):
        """
        Print a financial report including inventory value, revenue, costs, and profit.
        """

        print(tabulate([['inventory value', self.calculate_inventory_value()], 
                        ['revenue', self.revenue], ['cost', self.costs],
                          SEPARATING_LINE, 
                        ['profit', self.revenue - self.costs]]))


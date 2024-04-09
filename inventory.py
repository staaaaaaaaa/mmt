from tabulate import tabulate, SEPARATING_LINE
from datetime import datetime

class Product:
    last_id = 0
    def __init__(self,  name, quantity, price_purchase, price_sell):
        Product.last_id += 1
        self.id = Product.last_id
        self.name = name
        self.quantity = quantity
        self.price_purchase = price_purchase
        self.price_sell = price_sell
    

class Inventory:
    def __init__(self, inventory):
        self.inventory = inventory
        self.inventory_logs = []

        self.revenue = 0
        self.costs = 0

    


    def print_list_of_products(self):
        inventory_table = []
        for product in self.inventory:
            inventory_table.append({k: v for i, (k, v) in enumerate(vars(product).items())})
        print(tabulate(inventory_table, headers='keys'))
    
    def print_product_info(self, product_name):
        product_info = f'{product_name} not found in the inventory. Try again or add product.'
        for product in self.inventory:
            if product.name == product_name:
                product_info = tabulate(vars(product).items(), headers=[product_name,''])
        print(product_info)

    def print_transactions_logs(self):
        print(tabulate(self.inventory_logs, headers='keys'))

    def print_financial_report(self):
        print(tabulate([['inventory value', self.revenue - self.costs], ['revenue', self.revenue], ['cost', self.costs], SEPARATING_LINE, ['profit', self.revenue - self.costs]]))


                
    def add_new_product_to_inventory(self, product_new):
        log = f'Error while adding product. Try again.' 
        for product in self.inventory:
            if product.name == product.name:
                log = f'Error while adding product. Try again.'
        if product_new.name != "":
            self.inventory.append(product_new)
            log = f"Added new product {product_new.name}: {product_new.quantity}"
            self.costs = self.costs + product_new.quantity * product_new.price_purchase
        self.inventory_logs.append({'date': datetime.now(), 
                                    'transaction': log})
        print(log)
    
    def restock_product(self, product_name, added_items):
        log = f'{product_name} not found in the inventory. Try again or add product.'
        for product in self.inventory:
            if product.name == product_name:
                product.quantity = product.quantity + added_items
                log = f"Added new stock for {product_name}: {product.quantity - added_items} -> {product.quantity}"
                self.costs = self.costs + product.quantity * product.price_purchase
        self.inventory_logs.append({'date': datetime.now(), 
                                'transaction': log})
        print(log)
        
    
    def sell_product_stock(self, product_name, sold_items):
        log = f'{product_name} not found in the inventory. Try again or add product.'
        for product in self.inventory:
            if product.name == product_name and product.quantity >= sold_items:
                product.quantity = product.quantity - sold_items
                log = f"Sold {product_name}: {product.quantity + sold_items} -> {product.quantity}"
                self.revenue = self.revenue + product.quantity * product.price_sell
            elif product.name == product_name and product.quantity < sold_items:
                log = f"Unsuccessful transaction. Not enough stock for sell {sold_items} of {product_name}: {product.quantity}"
        self.inventory_logs.append({'date': datetime.now(), 
                                'transaction': log})
        print(log)

    def calculate_inventory_value(self,user_ids=''):
        if len(user_ids) == 0:
            ids = [product.id for product in self.inventory]
        else:
            ids = [int(id) for id in user_ids.replace(' ','').split(',')]
        print(sum([product.quantity * product.price_purchase  for product in self.inventory if product.id in ids]))

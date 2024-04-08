class Product:
    def __init__(self, id, name, quantity, price_purchase, price_sell):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price_purchase = price_purchase
        self.price_sell = price_sell
    

class Inventory:
    def __init__(self, stock_inventory):
        self.stock_inventory = stock_inventory
        self.inventory_logs = []

    def print_list_of_products(self):
        for product in self.stock_inventory:
            print(f"""Product: {product.name} ID: {product.id} Quantity: {product.quantity}""")
    
    def print_product_info(self, product_name):
        for product in self.stock_inventory:
            if product.name == product_name:
                print(f"""
Product: {product.name} 
ID: {product.id} 
Quantity: {product.quantity}
Purchasing price: {product.price_purchase}
Selling price: {product.price_sell}
""")
                
    def add_new_product_to_inventory(self, product):
        if product.name != "":
            self.stock_inventory.append(product)
    
    def restock_product(self, product_name, added_items):
        for product in self.stock_inventory:
            if product.name == product_name:
                product.quantity = product.quantity + added_items
                log = f"Added new stock for {product_name}. New value: {product.quantity}"
                self.inventory_logs.append(log)
                print(log)
    
    def sell_product_stock(self, product_name, sold_items):
        for product in self.stock_inventory:
            if product.name == product_name and sold_items < product.quantity:
                product.quantity = product.quantity - sold_items
                log = f"{product_name}: {product.quantity + sold_items} -> {product.quantity}"
                self.inventory_logs.append(log)
                print(log)

    

stock_inventory = [Product(1, "Chair", 10, 10, 50), Product(2, "Lipstick", 20, 20, 15)]
store = Inventory(stock_inventory)

store.add_new_product_to_inventory(Product(3, "Babyoil", 1, 1, 50))
store.print_list_of_products()
store.restock_product('Chair', 3)
store.print_list_of_products()
store.sell_product_stock('Babyoil', 3)
store.print_list_of_products()
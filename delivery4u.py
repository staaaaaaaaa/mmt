from inventory import *
initial_inventory = [Product(1, "Chair", 10, 10, 50), Product(2, "Lipstick", 20, 20, 15)]
store = Inventory(initial_inventory)

store.add_new_product_to_inventory(Product(3, "Babyoil", 1, 10, 50))
store.sell_product_stock('Babyoil', 1)
store.restock_product('Babyoil', 15)
store.sell_product_stock('Babyoil', 5)
store.print_transactions_logs()
store.print_financial_report()
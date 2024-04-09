from inventory import *
initial_inventory = [Product("Chair", 10, 10, 50), Product( "Lipstick", 20, 20, 15),Product( "Babyoil", 5, 10, 50)]
store = Inventory(initial_inventory)

store.add_new_product_to_inventory(Product("Corgi", 4, 6, 12))
store.add_new_product_to_inventory(Product("Border", 4, 6, 12))
store.sell_product_stock('Babyoil', 1)
store.restock_product('Babyoil', 15)
store.print_list_of_products()
store.print_financial_report()
store.print_transactions_logs()
store.print_list_of_products()

store.calculate_inventory_value('')

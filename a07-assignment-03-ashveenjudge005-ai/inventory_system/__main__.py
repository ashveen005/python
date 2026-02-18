from pathlib import Path

current_path = Path.cwd()


# YOUR CODE HERE
############################
# import the Classes from the orders and inventory
from .utils.inventory import Inventory, StockItem
from .utils.orders import Order, OrdersList
############################

# Part 1 stock and Inventory Do not remove
test_stock_item_id = "9709AA"
test_stock_current_units = "9001"
test_stock_unit_price = "32.1"
# Testing StockItem class
# YOUR CODE HERE
############################
print("Stock testing")
test_stock_item = StockItem(
    test_stock_item_id,
    test_stock_current_units,
    test_stock_unit_price,
)
print(f"{test_stock_item} has a value of{test_stock_item.get_stock_value()}")



###########################

INVENTORY_CSV_FILE = current_path / "inventory_stock.csv"
ORDERS_CSV_FILE = current_path / "customer_orders.csv"

print("Inventory system testing")
test_stock_id = "1308BA"

# YOUR CODE HERE
############################
inventory = Inventory()
inventory.import_stock(INVENTORY_CSV_FILE)
print(f"Number of items in inventory {len(inventory.stock)}")
total_inventory_price = 0.0
for item in inventory.stock:
    total_inventory_price += item.get_stock_value()
print(f"Total price of inventory {round(total_inventory_price, 2)}")

sample_item = inventory.get_stock_by_id(test_stock_id)
if sample_item:
    print(f"Sample stock found {sample_item}, price:{sample_item.unit_price}")
    








###########################

# Part 2: Order testing Do not remove
test_order_date = "12/13/2022"
test_order_stock_id ="2847BA"
test_order_quantity = "582"
# Order class testing
# YOUR CODE HERE
############################

test_order = Order(
    test_order_date, test_order_stock_id, test_order_quantity
)
print(f"Order:{test_order}")








#############################

print("Order system testing")
test_order_testing_stock_item_id = "1695CA"
# OrdersList testing
# YOUR CODE HERE
############################

orders_list = OrdersList(inventory)
orders_list.import_orders(ORDERS_CSV_FILE)
num_orders = orders_list.get_number_of_orders_by_sku(test_order_testing_stock_item_id)
print(f"Number of orders with the stock item id {test_order_testing_stock_item_id}: {num_orders}")
total_price = orders_list.get_number_of_orders_by_sku(test_order_testing_stock_item_id)
print(f"Total price of orders with stock item id {test_order_testing_stock_item_id}: {total_price}")






############################

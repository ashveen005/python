from inventory_system.utils.orders import OrdersList

def get_orders_list_and_inventory():
    from pathlib import Path
    from inventory_system.utils.inventory import Inventory

    current_path = Path.cwd()
    INVENTORY_CSV_FILE = current_path / "automated-tests-do-not-touch" /  "testing_inventory.csv"
    ORDERS_CSV_FILE = current_path / "automated-tests-do-not-touch" /  "testing_customer_orders.csv"

    inventory = Inventory()
    inventory.import_stock(INVENTORY_CSV_FILE)

    orders_list = OrdersList(inventory)
    orders_list.import_orders(ORDERS_CSV_FILE)

    return orders_list, inventory

def test_part_2_orders_list_import_orders():
    orders_list, _ = get_orders_list_and_inventory()

    EXPECTED_LENGTH = 189

    assert len(orders_list.orders) == EXPECTED_LENGTH, F"OrdersList length should be {EXPECTED_LENGTH}"

def test_get_orders_by_sku():
    orders_list, _ = get_orders_list_and_inventory()
    TEST_SKU = '3084CA'
    EXPECTED_NUMBER_OF_ORDERS = 4
    number_of_orders = orders_list.get_number_of_orders_by_sku(TEST_SKU)
    assert number_of_orders == EXPECTED_NUMBER_OF_ORDERS, F"Number of orders for SKU {TEST_SKU} should be {EXPECTED_NUMBER_OF_ORDERS}"

def test_get_orders_price_by_sku():
    orders_list, _ = get_orders_list_and_inventory()
    TEST_SKU = '3084CA'
    EXPECTED_ORDERS_PRICE = 11079.24
    orders_price = orders_list.get_orders_price_by_sku(TEST_SKU)
    assert orders_price == EXPECTED_ORDERS_PRICE, F"Total orders price for SKU {TEST_SKU} should be {EXPECTED_ORDERS_PRICE}"

if __name__ == "__main__":
    test_part_2_orders_list_import_orders()
    test_get_orders_by_sku()
    test_get_orders_price_by_sku()
    print("successful output")

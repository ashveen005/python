from inventory_system.utils.inventory import  Inventory, StockItem

from pathlib import Path

current_path = Path.cwd()

INVENTORY_CSV_FILE = current_path / "automated-tests-do-not-touch" /  "testing_inventory.csv"


def test_part_1_inventory_works():
    inventory = Inventory()
    assert isinstance(inventory.stock, list), "Inventory stock should be a list"

def test_inventory_import_stock():
    inventory = Inventory()
    inventory.import_stock(INVENTORY_CSV_FILE)
    EXPECTED_LENGTH = 81
    assert len(inventory.stock) == EXPECTED_LENGTH, F"Inventory stock length should be {EXPECTED_LENGTH}"

def test_total_stock_value():
    inventory = Inventory()
    inventory.import_stock(INVENTORY_CSV_FILE)
    total_value = inventory.get_total_stock_value()
    EXPECTED_TOTAL_VALUE = 9405278.34
    assert total_value == EXPECTED_TOTAL_VALUE, F"Inventory total stock value should be {EXPECTED_TOTAL_VALUE}"

def test_get_stock_by_id():
    inventory = Inventory()
    inventory.import_stock(INVENTORY_CSV_FILE)
    # first value in the testing file.
    EXPECTED_STOCK_ITEM = "2925CA"
    EXPECTED_STOCK_QUANTITY = 131.0
    EXPECTED_PRICE = 48
    stock_item = inventory.get_stock_by_id(EXPECTED_STOCK_ITEM)
    assert isinstance(stock_item, StockItem), "get_stock_by_id should return a StockItem instance"
    assert stock_item.id == EXPECTED_STOCK_ITEM, F"StockItem id should be '{EXPECTED_STOCK_ITEM}'"
    assert stock_item.current_units == EXPECTED_STOCK_QUANTITY, F"StockItem current_units should be {EXPECTED_STOCK_QUANTITY}"
    assert stock_item.unit_price == EXPECTED_PRICE, F"StockItem unit_price should be {EXPECTED_PRICE}"

def test_get_stock_by_id_not_found():
    inventory = Inventory()
    inventory.import_stock(INVENTORY_CSV_FILE)
    stock_item = inventory.get_stock_by_id("NOTFOUND")
    assert stock_item is None, "get_stock_by_id should return None if not found"

def test_inventory_str():
    inventory = Inventory()
    inventory.import_stock(INVENTORY_CSV_FILE)
    EXPECTED_LENGTH = 81
    assert str(inventory) == F"Inventory(stock: {EXPECTED_LENGTH})", "Inventory __str__ output is incorrect"

if __name__ == "__main__":
    test_part_1_inventory_works()
    test_inventory_import_stock()
    test_total_stock_value()
    test_get_stock_by_id()
    test_get_stock_by_id_not_found()
    test_inventory_str()
    print("successful output")
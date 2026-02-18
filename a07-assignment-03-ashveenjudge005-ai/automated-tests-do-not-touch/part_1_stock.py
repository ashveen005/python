from inventory_system.utils.inventory import  StockItem

def test_part_1_stock_item_works():
    test_stock_item_id = "9709AA"
    test_stock_current_units = "1000"
    test_stock_unit_price = "30.2"
    stock_item = StockItem(test_stock_item_id, test_stock_current_units, test_stock_unit_price)
    assert stock_item.id == test_stock_item_id, "StockItem id is incorrect"
    assert stock_item.current_units == float(test_stock_current_units), "StockItem current_units is incorrect"
    assert stock_item.unit_price == float(test_stock_unit_price), "StockItem unit_price is incorrect"

def test_stock_item_get_stock_item():
    test_stock_item_id = "9709AA"
    test_stock_current_units = "1000"
    test_stock_unit_price = "30.2"
    stock_item = StockItem(test_stock_item_id, test_stock_current_units, test_stock_unit_price)
    assert stock_item.get_stock_value() == 30200.0, "Stock value calculation is incorrect "

def test_stock_item_str():
    test_stock_item_id = "9709AA"
    test_stock_current_units = "1000"
    test_stock_unit_price = "30.2"
    stock_item = StockItem(test_stock_item_id, test_stock_current_units, test_stock_unit_price)

    assert str(stock_item) == "StockItem(9709AA)", "StockItem __str__ is incorrect"

if __name__ == "__main__":
    test_part_1_stock_item_works()
    test_stock_item_get_stock_item()
    test_stock_item_str()
    print("successful output")
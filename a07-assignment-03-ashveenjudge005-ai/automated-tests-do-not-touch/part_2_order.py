from inventory_system.utils.orders import Order

def test_part_2_order_works():
    test_order_date = "12/13/2022"
    test_order_stock_id ="2847BA"
    test_order_quantity = "582"
    order = Order(test_order_date, test_order_stock_id, test_order_quantity)
    assert order.order_date.strftime("%m/%d/%Y") == test_order_date, "Order date is incorrect"
    assert order.stock_item_id == test_order_stock_id, "Order stock_item_id is incorrect"
    assert order.quantity == float(test_order_quantity), "Order quantity is incorrect"

def test_order_str():
    test_order_date = "12/13/2022"
    test_order_stock_id ="2847BA"
    test_order_quantity = "582"
    order = Order(test_order_date, test_order_stock_id, test_order_quantity)
    expected_str = "Order(stock item id: 2847BA, date: 2022-12-13)"
    assert str(order) == expected_str, "Order __str__ is incorrect"

def test_order_repr():
    test_order_date = "12/13/2022"
    test_order_stock_id ="2847BA"
    test_order_quantity = "582"
    order = Order(test_order_date, test_order_stock_id, test_order_quantity)
    expected_repr = "Order(stock item id: 2847BA, date: 2022-12-13)"
    assert repr(order) == expected_repr, "Order __repr__ is incorrect"

if __name__ == "__main__":
    test_part_2_order_works()
    test_order_str()
    test_order_repr()
    print("successful output")
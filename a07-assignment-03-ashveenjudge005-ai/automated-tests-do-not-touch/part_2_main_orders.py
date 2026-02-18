from .helpers import (
    run_module_with_patches,
    get_line_that_includes,
    assert_line_includes)

def test_part_2_main_orders_testing():
    output = run_module_with_patches(
        "inventory_system"
    )
    line = get_line_that_includes(output, "Order:")
    assert_line_includes(line, "2847BA")
    assert_line_includes(line, "2022-12-13", "order date not correct")

def test_part_2_orders_list_testing():
    output = run_module_with_patches(
        "inventory_system"
    )
    line = get_line_that_includes(output, "Number of orders")
    assert_line_includes(line, "177", "number of orders not completely correct")

def test_part_2_orders_list_total_price_testing():
    output = run_module_with_patches(
        "inventory_system"
    )
    line = get_line_that_includes(output, "Total Price of orders")
    assert_line_includes(line, "413974.3", "price not completely correct")

if __name__ == "__main__":
    test_part_2_main_orders_testing()
    test_part_2_orders_list_testing()
    test_part_2_orders_list_total_price_testing()
    print("successful output")
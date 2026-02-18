from .helpers import (
    run_module_with_patches,
    get_line_that_includes,
    assert_line_includes)


def test_part_2_main_stock_testing():
    output = run_module_with_patches(
        "inventory_system"
    )
    line = get_line_that_includes(output, "StockItem")
    assert_line_includes(line, "9709AA")
    assert_line_includes(line, "288932.1", "stock item value not correct")

def test_part_2_main_inventory_testing():
    output = run_module_with_patches(
        "inventory_system"
    )
    line = get_line_that_includes(output, "Number of items")
    assert_line_includes(line, "303", "number of orders not completely correct")
    line = get_line_that_includes(output, "Total price of inventory")
    assert_line_includes(line, "77329254.77", "number of orders not completely correct")

def test_part_2_stock_found_in_inventory():
    output = run_module_with_patches(
        "inventory_system"
    )
    line = get_line_that_includes(output, "Sample stock found")
    assert_line_includes(line, "1308BA")
    assert_line_includes(line, " 240.0", "stock item value not correct")

if __name__ == "__main__":
    test_part_2_main_stock_testing()
    test_part_2_main_inventory_testing()
    test_part_2_stock_found_in_inventory()
    print("successful output")
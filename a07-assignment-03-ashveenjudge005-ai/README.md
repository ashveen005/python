[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/j0qttKO2)
# SDEV 1001 - Assignment 3

This assignment covers everything up to and including Classes and Objects

Note on completing this `breakpoint()` will be very useful.

## Instructions

### Part 1: Stock and Inventory

1. Make the inventory folder a module so you can run it with the command `python -m inventory_system` by adding an `__init__.py` in the folder, ensure for every folder you create inside of the `inventory_system` folder you add an `__init__.py`

2. In inside the module in a folder named `utils` create a file named `inventory.py`

3. Create the `StockItem` class:
  - with the following attributes:
    - `id` a string
    - `current_units` a float
    - `unit_price` a float
  - and with the following methods
    - a constructor (take a look at the `__main__.py`) which will take in **"id", "units", and "price" as parameters** and set to the to the attributes above.
    - method `get_stock_value` which takes **no parameters**
      - this returns multiplication result of the `current_units` and `unit_price` rounded to 2 places.
    - the double underscore methods of `__str__` and `__repr__` so a sample output would yield `StockItem(9709AA)` if the `id` provided was `9709AA`
      - Note you can just call this variable or print it and it should show this output.

4. Create the `Inventory` class
  - with the following attributes
    - `stock` as an array
  - with the following methods
    - a constructor (**no parameters**) that assigns the `stock` attribute to an empty array
    - method `import_stock` **which takes a string of the csv file name as a paramter.**
      - loop through the rows of the csv and append a `StockItem` with the correct values of the of csv provided (please read the csv)
        - Note: `id` of a stock is a `SKU ID` in the csv
      - returns the attribute `stock`
    - method `get_stock_by_id` which takes a **single string of a stock_item_id as a parameter**
      - this should search for the stock in the `stock` attribute
        - returns `None` if no stock found
        - returns an instance of `StockItem`
  - the double underscore methods of `__str__` and `__repr__` so a sample output would yield `Inventory(stock: 12)` if the length of the `stock` after an import was provided was `12`.


### Part 2: Orders and OrdersList
Note: only proceed to this if the above step is fully completed.

1. In inside the module in a folder named `utils` create a file named `orders.py`
2. Create the class `Order`
  - with the following attributes
    - `order_date` a `datetime.date` object
      - [reference](https://docs.python.org/3/library/datetime.html)
      - [converting dates from strings](https://www.digitalocean.com/community/tutorials/python-string-to-datetime-strptime#converting-a-string-to-a-datetime-object-using-datetime-strptime)
        - you'll use the format "%m/%d/%Y"
    - `stock_item_id` a string
    - `quantity` a float

  - with the following methods
    - a contructor which takes in the **following parameters (that will set the above attributes) listed below**
      - `date_string` string
      - `stock_item_id` string
      - `quantity` number
    - the double underscore methods of `__str__` and `__repr__` so a sample output would yield `Order(stock item id: 2847BA, date: 2022-12-13)` with inputs of `"12/13/2022"` for order_date and `"2847BA"` for the stock ids.

2. Create the class `OrdersList`
  - with the following attributes:
    - `inventory` which will be an instance of `Inventory`
    - `orders` initialized with an empty array, but will be a list of `Order` instances.
  - with following methods
    - `import_orders` which takes **a single parameter `csv_file` (a string)**
      - this will loop through the rows of the csv and create `Order` objects with the information from the csv.
    - `get_number_of_orders_by_sku` which **will take the parameter `stock_item_id` as a string**. This is going to count the number of orders with the stock item id specified.
      - returns the count of orders (as an `int`) with the `stock_item_id` equal to the `stock_item_id` on the `Order` instances.

    - `get_orders_price_by_sku` which will take the **parameter `stock_item_id` as a string**. This will calculate total price of all orders with that `stock_item_id`, the price of a single order is the quantity of an order multiplied by unit price of a stock item.
      - returns the price of all orders (as a `float` rounded to max 2 decimals)
    - the double underscore methods of `__str__` and `__repr__` so a sample output would yield `OrdersList(orders: 9001)` being the number of `Order` instances in the `orders` list attribute

5. Finish the code in the `inventory/__main__.py` file so the output looks like the sample output.
    - use the methods defined in the above classes to achieve the output.
    - also don't hardcode values and use the existing values with `test_` prefixes in `__main__.py` file.

## Sample Output

- the following output has different numbers but should provide the values in the same format.
```
Stock testing
StockItem(929AA) has a value of 321548.1
Inventory system testing
Number of items in inventory 452
Total price of inventory 45663218.77
Sample stock found StockItem(1308BA), price: 110.0
Order: Order(stock item id: 284RBA, date: 2024-12-1)
Order system testing
Number of orders with the stock item id 1435CA: 197
Total Price of orders with the stock item id 1435CA: 563242.3
```

## Rubric

### 4 Points - Part 1: StockItem class implementation
| Level                | Feedback Description                                   |
| -------------------- | ------------------------------------------------------ |
| Excellent            | All Tests pass, formatted correctly                    |
| Satisfactory         | Tests pass but code formatted incorrectly.             |
| Incomplete/Incorrect | Tests don't pass but Still somewhat functional         |
| Poor                 | Tests don't pass, program does not use best practices. |
| Missing              | Broken/Missing/Way Off                                 |

### 8 points - Part 1: Inventory class implementation
| Level                | Feedback Description                                                    |
| -------------------- | ----------------------------------------------------------------------- |
| Excellent            | All Tests pass, formatted correctly                                     |
| Satisfactory         | Tests pass but code formatted incorrectly.                              |
| Good                 | Some tests dont pass, still functional, but code formatted incorrectly. |
| Incomplete/Incorrect | Tests don't pass but Still somewhat functional                          |
| Poor                 | Tests don't pass, program does not use best practices.                  |
| Missing              | Broken/Missing/Way Off                                                  |

### 3 Points - Part 2: Order class implementation
| Level                | Feedback Description                                   |
| -------------------- | ------------------------------------------------------ |
| Excellent            | All Tests pass, formatted correctly                    |
| Satisfactory         | Tests pass but code formatted incorrectly.             |
| Incomplete/Incorrect | Tests don't pass but Still somewhat functional         |
| Poor                 | Tests don't pass, program does not use best practices. |
| Missing              | Broken/Missing/Way Off                                 |

### 10 Points - Part 2: OrdersList class implementation
| Level                | Feedback Description                                                    |
| -------------------- | ----------------------------------------------------------------------- |
| Excellent            | All Tests pass, formatted correctly                                     |
| Satisfactory         | Tests pass but code formatted incorrectly.                              |
| Good                 | Some tests dont pass, still functional, but code formatted incorrectly. |
| Incomplete/Incorrect | Tests don't pass but Still somewhat functional                          |
| Poor                 | Tests don't pass, program does not use best practices.                  |
| Missing              | Broken/Missing/Way Off                                                  |


### 8 Points - Part 2: Main Script runs and gives correct output
| Level                | Feedback Description                                                    |
| -------------------- | ----------------------------------------------------------------------- |
| Excellent            | All Tests pass, formatted correctly                                     |
| Satisfactory         | Tests pass but code formatted incorrectly.                              |
| Incomplete/Incorrect | Tests don't pass but Still somewhat functional                          |
| Poor                 | Tests don't pass, program does not use best practices.                  |
| Missing              | Broken/Missing/Way Off                                                  |
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/ULylLGZW)
# SDEV 1001 - Assignment 2

This assignment covers Arrays and Loops, Debugging with Breakpoints and More Loops and Exceptions.

## Instructions

### Part 1: List Methods and Loops

1. In the the file `cursed_antiques_part_one.py` create a list named `cursed_antiques` with the following items
    - Talisman
    - Monkeys Paw
    - Cursed Mirror
    - Haunted Painting
    - Voodoo Doll
    - Crystal Ball
    - Cursed Locket
    - Ancient Amulet
    - Phantom Clock
    - Dorian Gray's Portrait
    - Cursed Ring

add the following items to this list using list methods only:
- Demon Key
- Horcrux

2. Sort the array alphabetically, after sorting it remove the items at index 4 and 8, using list methods

3. Using for loops display the items and the index of the item in that array using a for loop.

4. If you try to remove an item called `Shrunken Head` using the `index` and/or `remove` list method, what kind of exception or error is thrown?

- ENTER ANSWER FOR PART 4 HERE: value error is thrown because when we executed the code it tried to find the item name shrunken head but it was not able to find that item in list so it raised an error. shrunken head is not item of list so python was not able to remove it and raised an error.

5. If you try to remove item with index of `17` using the `pop` method what Exception/Error is thrown?

- ENTER ANSWER FOR PART 5 HERE: index error is thrown because the list is not having item at index number 17. when we use pop with index it checks if that index number exists and if it didnt as in our case so it shows an error as index is not in range .

Hint for part 4 and 5: `breakpoint()` is handy here.

#### Desired output
- All of Part 1
```
The Cursed Antique Shop Part 1
After adding cursed antiques (part 1.1)
['Talisman', ...redacted output...]
After sorting and removing (part 1.2)
['Ancient Amulet', ...redacted output...]
All cursed antiques and their index in point form (part 1.3)
- 1: Ancient Amulet
- 2: Crystal Ball
# ... redacted output ...
```

### Part 2: While Loops and List methods
Here you'll be using the knowledge of part one to create an application that will give you the ability to:
- list the antiques
- list the shopping cart
- sort the antiques
- add antique to shopping cart
- and remove antique from shopping cart (if it's in the list.)

based on user input.

1. Use the file called `cursed_antiques_part_2.py`. In the while loop that will check if the user has entered quit and exit the loop if they do.
```python
"""\nWhat would you like to do?
    - Buy an item (enter 'buy')
    - Remove antique from shopping cart (enter 'remove')
    - Sort antiques (enter 'sort')
    - List items (enter 'list')
    - Quit (enter 'quit'
    Option: """
```
Hint: if you run this for testing and you just have an infinite loop you can use `Ctrl + C` to cancel it.

2. In the while loop that will check if the user has entered `quit` and exit the loop if they do (you can do this a few different ways that will be accepted.)
3. Check if the user has entered `buy`.
   1. get a new input from the user to get the item they'd like to buy an item by its name or its index. Use the following string for your input `"Would you like to buy the antique by name or by index? (Enter 'name' or 'index') "`
   2. By Name:
      1. Ask the user which item they want to by using the string `Which item would you like to buy? `
      2. If the item (for example `Haunted Cheese`) is not in the list of available antiques for purchase, display `That item is not available.`
      3. If the item (for example `Crystal Ball`) is available for purchase, remove it from the available antiques and add it to the shopping cart and print `Crystal Ball was removed from the inventory and added to the shopping cart.`
   3. By index:
      1. Ask the user which item they want to by using the string `Which item would you like to buy? `
      2. If the user enters an invalid value, print the message `That item is not available.`
      3. If the item (for example `Crystal Ball`) is available for purchase, remove it from the available antiques and add it to the shopping cart and print `Crystal Ball was removed from the inventory and added to the shopping cart.`
   4. If the user enters an invalid choice, display `Sorry I didn't understand that.`
4. Check if the user has entered `sort` to sort the cursed antiques list
   1. Give the user the option to sort the antiques in reversed order if they want using the input `Would you like to sort the antiques in reverse alphabetical order (y/n)? `
   2. If the user chooses y, the antiques list should be sorted in reverse alphabetical order.
   3. If the user chooses n, the antiques list should be sorted in alphabetical order.
   4. If the user chooses neither, display `Sorry I didn't understand that.`
5. Check if the user has entered `list` to list the items in the shopping cart or in the antiques list using the input `Would you like to view your shopping cart or available antiques (s/a)? `
   1. The numerical list should be displayed with the appropriate items based on the user's choice starting at `1`
   2. If the user does not choose s or a then show the string `Sorry I didn't understand that.`
6. Check if the user has entered `remove` to remove items from their shopping cart.
   1. Receive input from the user for the item they want to remove using the prompt `Which item would you like to remove from your shopping cart? `
   2. if the item is in the shopping cart (for example `Phantom Clock`) remove the item and display `"Phantom Clock removed from the shopping cart."` The item should then go back into the available antiques.
   3. if the item is not in the shopping cart (for example `"Phantom Clock"`), if it is not in the list then display
      1. do this using the `try ... except ...` syntax with the correct error (do this with the step above.) display `"Phantom Clock is not in the shopping cart"`
7. Handle if the user has entered anything unexpected and display `"Sorry I didn't understand that try again."`


#### Desired output
- Part 2.1 and 2.2 - Quit
```
Welcome to The Cursed Antique Shop!

    - Buy an item (enter 'buy')
    - Remove antique from shopping cart (enter 'remove')
    - Sort antiques (enter 'sort')
    - List items (enter 'list')
    - Quit (enter 'quit')
    Option: quit


Thank you for visiting the Cursed Antiques Shop! Happy Halloween!
```

- Part 2.3.2 - Buy - By Name - Item Available
```
Welcome to The Cursed Antique Shop!

    - Buy an item (enter 'buy')
    - Remove antique from shopping cart (enter 'remove')
    - Sort antiques (enter 'sort')
    - List items (enter 'list')
    - Quit (enter 'quit')
    Option: buy


Would you like to buy the antique by name or by index? (Enter 'name' or 'index') name
Which item would you like to buy? Crystal Ball
Crystal Ball was removed from the inventory and added to the shopping cart.
```

- Part 2.3.2 - Buy - By Name - Item Unavailable
```
Welcome to The Cursed Antique Shop!

    - Buy an item (enter 'buy')
    - Remove antique from shopping cart (enter 'remove')
    - Sort antiques (enter 'sort')
    - List items (enter 'list')
    - Quit (enter 'quit')
    Option: buy


Would you like to buy the antique by name or by index? (Enter 'name' or 'index') name
Which item would you like to buy? Haunted Cheese
That item is not available.
```

- Part 2.3.3 - Buy - By Index - Item Available
```
Welcome to The Cursed Antique Shop!

    - Buy an item (enter 'buy')
    - Remove antique from shopping cart (enter 'remove')
    - Sort antiques (enter 'sort')
    - List items (enter 'list')
    - Quit (enter 'quit')
    Option: buy


Would you like to buy the antique by name or by index? (Enter 'name' or 'index') index
Which item would you like to buy? 3
Cursed Mirror was removed from the inventory and added to the shopping cart.
```

- Part 2.3.3 - Buy - By Index - Out of Range Index
```
Welcome to The Cursed Antique Shop!

    - Buy an item (enter 'buy')
    - Remove antique from shopping cart (enter 'remove')
    - Sort antiques (enter 'sort')
    - List items (enter 'list')
    - Quit (enter 'quit')
    Option: buy


Would you like to buy the antique by name or by index? (Enter 'name' or 'index') index
Which item would you like to buy? 500
That item is not available.
```

- Part 2.3.3 - Buy - By Index - Invalid Index
```
Welcome to The Cursed Antique Shop!

    - Buy an item (enter 'buy')
    - Remove antique from shopping cart (enter 'remove')
    - Sort antiques (enter 'sort')
    - List items (enter 'list')
    - Quit (enter 'quit')
    Option: buy


Would you like to buy the antique by name or by index? (Enter 'name' or 'index') index
Which item would you like to buy? fdsf
That item is not available.
```

- Part 2.3.4 - Buy - Invalid Selection
```
Welcome to The Cursed Antique Shop!

    - Buy an item (enter 'buy')
    - Remove antique from shopping cart (enter 'remove')
    - Sort antiques (enter 'sort')
    - List items (enter 'list')
    - Quit (enter 'quit')
    Option: buy


Would you like to buy the antique by name or by index? (Enter 'name' or 'index') fdsfas
Sorry I didn't understand that.
```

- Part 2.4.2 - Sort - Reverse Alphabetical Order
```
Welcome to The Cursed Antique Shop!

    - Buy an item (enter 'buy')
    - Remove antique from shopping cart (enter 'remove')
    - Sort antiques (enter 'sort')
    - List items (enter 'list')
    - Quit (enter 'quit')
    Option: sort


Would you like to sort the antiques in reverse alphabetical order (y/n)? y
Antiques sorted in reverse alphabetical order.
```

- Part 2.4.3 - Sort - Alphabetical Order
```
Welcome to The Cursed Antique Shop!

    - Buy an item (enter 'buy')
    - Remove antique from shopping cart (enter 'remove')
    - Sort antiques (enter 'sort')
    - List items (enter 'list')
    - Quit (enter 'quit')
    Option: sort


Would you like to sort the antiques in reverse alphabetical order (y/n)? y
Antiques sorted in alphabetical order.
```

- Part 2.4.4 - Sort - Invalid Option
```
Welcome to The Cursed Antique Shop!

    - Buy an item (enter 'buy')
    - Remove antique from shopping cart (enter 'remove')
    - Sort antiques (enter 'sort')
    - List items (enter 'list')
    - Quit (enter 'quit')
    Option: sort


Would you like to sort the antiques in reverse alphabetical order (y/n)? fsdf
Sorry I didn't understand that.
```

- Part 2.5.1 - List - List Antiques or Shopping Cart
```
Welcome to The Cursed Antique Shop!

    - Buy an item (enter 'buy')
    - Remove antique from shopping cart (enter 'remove')
    - Sort antiques (enter 'sort')
    - List items (enter 'list')
    - Quit (enter 'quit')
    Option: list


Would you like to view your shopping cart or available antiques (s/a)? a
1. Ancient Amulet
2. Crystal Ball
3. Cursed Locket
# ... redacted output ...
```

- Part 2.5.2 - List - Invalid Input
```
Welcome to The Cursed Antique Shop!

    - Buy an item (enter 'buy')
    - Remove antique from shopping cart (enter 'remove')
    - Sort antiques (enter 'sort')
    - List items (enter 'list')
    - Quit (enter 'quit')
    Option: list


Would you like to view your shopping cart or available antiques (s/a)? fdsfs
Sorry I didn't understand that.
```

- Part 2.6.2 - Remove - Remove From Shopping Cart Success
```
Welcome to The Cursed Antique Shop!

    - Buy an item (enter 'buy')
    - Remove antique from shopping cart (enter 'remove')
    - Sort antiques (enter 'sort')
    - List items (enter 'list')
    - Quit (enter 'quit')
    Option: remove

Which item would you like to remove from your shopping cart? Monkeys Paw
Monkeys Paw was removed from the shopping cart.
```

- Part 2.6.3 - Remove - Item not in Shopping Cart
```
Welcome to The Cursed Antique Shop!

    - Buy an item (enter 'buy')
    - Remove antique from shopping cart (enter 'remove')
    - Sort antiques (enter 'sort')
    - List items (enter 'list')
    - Quit (enter 'quit')
    Option: remove

Which item would you like to remove from your shopping cart? Ghost Cat
Ghost Cat is not in the shopping cart.
```

- Part 2.7 - Invalid Choice
```
Welcome to The Cursed Antique Shop!

    - Buy an item (enter 'buy')
    - Remove antique from shopping cart (enter 'remove')
    - Sort antiques (enter 'sort')
    - List items (enter 'list')
    - Quit (enter 'quit')
    Option: gggg

Sorry I didn't understand that try again.
```
### Part 1: Array Methods and Loops

#### 5 points - Parts 1.1, 1.2, and 1.3

| Level                | Feedback Description                                   |
| -------------------- | ------------------------------------------------------ |
| Excellent            | Code executed maches desired output, code is formatted correctly.               |
| Satisfactory         | Code executed maches desired output but code formatted incorrectly.             |
| Incomplete/Incorrect | Code executed does not match desired output but the program works somewhat.       |
| Poor                 | Code executed does not match desired output, program does not use best practices. |
| Missing              | Broken/Missing/Way Off                                 |

#### 2 points - Parts 1.4, 1.5

| Level   | Feedback Description |
| ------- | -------------------- |
| Correct | Values are correct.  |
| Missing | Not Correct          |


### Part 2: While Loops

#### 2 points - Part 2.1 and 2.2
| Level   | Feedback Description                     |
| ------- | ---------------------------------------- |
| Correct | Code executed maches desired output, code is formatted correctly. |
| Missing | Broken/Missing/Way Off                   |


#### 5 points - Part 2.3
| Level                | Feedback Description                                   |
| -------------------- | ------------------------------------------------------ |
| Excellent            | Code executed maches desired output, code is formatted correctly.               |
| Satisfactory         | Code executed maches desired output but code formatted incorrectly.             |
| Incomplete/Incorrect | Code executed does not match desired output but the program works somewhat.       |
| Poor                 | Code executed does not match desired output, program does not use best practices. |
| Missing              | Broken/Missing/Way Off                                 |

#### 3 points - Part 2.4 and 2.5
| Level   | Feedback Description                     |
| ------- | ---------------------------------------- |
| Correct | Code executed maches desired output, code is formatted correctly. |
| Incomplete/Incorrect | Code executed maches desired output but code formatted incorrectly.      |
| Missing | Broken/Missing/Way Off                   |

#### 6 points - Part 2.6
| Level                | Feedback Description                                   |
| -------------------- | ------------------------------------------------------ |
| Excellent            | Code executed maches desired output, code is formatted correctly.               |
| Satisfactory         | Code executed maches desired output but code formatted incorrectly.             |
| Incomplete/Incorrect | Code executed does not match desired output but the program works somewhat.       |
| Poor                 | Code executed does not match desired output, program does not use best practices. |
| Missing              | Broken/Missing/Way Off                                 |

#### 1 point - Part 2.7
| Level   | Feedback Description                     |
| ------- | ---------------------------------------- |
| Correct | Code executed maches desired output, code is formatted correctly. |
| Missing | Broken/Missing/Way Off                   |
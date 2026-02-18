print("Welcome to The Cursed Antique Shop!")

cursed_antiques = [
    "Talisman", "Monkeys Paw", "Cursed Mirror", "Haunted Painting", "Voodoo Doll", "Crystal Ball", "Cursed Ball", "Cursed Locket", "Ancient Amulet", "Phantom Clock ", "Dorian Gray's Portrait" , "Cursed Ring "
]

shopping_cart = [
    "Phantom Clock",
]

user_quit = False

# DO NOT CHANGE THE CODE ABOVE HERE
# YOUR CODE BELOW HERE
while not user_quit:
    option = input("what would you like to do?\n"
    "-Buy an item (enter 'buy')\n"
    "-Remove antique from shopping cart(enter'remove')\n"
    "-Sort antiques (enter'sort')\n"
    "-List items (enter 'list')\n"
    "Quit (enter'quit')\n"
    "option:")
    
    if option == "quit":
        print("Thankyou for visiting the cursed antiques shop! Happy Halloween!")
        user_quit = True
   
   
    elif option == "buy":
        choose = input("Would you like to buy the antique by name or by index? (Enter 'name' or 'index') ")
       
       
        if choose == "name":
            item_name= input("Which item would you like to buy?")
            if item_name in cursed_antiques:
                
                shopping_cart.append(item_name)
                print(f"{item_name} was removed from the inventory and added to the shopping cart. ")
            else:
                print("This item is not available.")

        elif choose == "index":
            index_choice = input("which item would you like to buy?")
            if index_choice.isdigit():
                index = int(index_choice)
                if 1 <= index <= len(cursed_antiques):
                    item_name = cursed_antiques.pop(index - 1)
                    shopping_cart.append(item_name)
                    print(f"{item_name} was removed from the inventory and added to the shopping cart.")
                else:
                 print("That item is not available") 
            else:
                print("That item is not available")    
            
        else:
             print ("Sorry I didn't understand that.")

          
    elif option == "sort":
        alpbh_order =  input("Would you like to sort the antiques in reverse alphabetical order(y/n)?")
        if alpbh_order == "y":
            cursed_antiques.sort(reverse=True)
            print("Antiques sorted in reverse alphabetical order.")
            for i, item in enumerate(cursed_antiques,1):
                print(f"{i}.{item}")
           
        elif alpbh_order == "n":
            cursed_antiques.sort()
            print("Antiques sorted in alphabetical order.")
            for i, item in enumerate(cursed_antiques,1):
                print(f"{i}.{item}")
        else:
            print("Sorry I didn't understand that.")
            
    elif option == "list":
        list_item = input("Would you like to view your shopping cart or available antiques (s/a)?")
        if list_item == "a":
                cursed_antiques.sort()
                for i, item in enumerate(cursed_antiques,1):
                    print(f"{i}. {item}")
        elif list_item == "s":
                for i, item in enumerate(shopping_cart,1):
                    print(f"{i}.{item}")
        else:
            print ( " Sorry i didn't understand.")
    

    elif option == "remove":
        remove_name = input("Which item would you like to remove from your shopping cart?")
        try:
            shopping_cart.remove(remove_name)
            cursed_antiques.append(remove_name)
            print(f"{remove_name} was removed from your shopping cart.")
        except ValueError:
            print(f"{remove_name} is not in the shopping cart.")            
        
    else:
        print("Sorry I didn't understand that. try again")

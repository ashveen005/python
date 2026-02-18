import random

# first dice roll is an int
first_dice_roll = random.randint(1,6)

# DO NOT COPY ABOVE THIS LINE FOR PART 2

# YOUR CODE BELOW
print('Welcome to the Dice Game')
play=input('Would you like to play?(yes/no)')
if play == "yes" :
 
 wager= int(input("How much do you like to wager?(enter an integer less than or equal 100)"))

 guess= int(input("What is your guess number guess? (1-6) "))

 first_dice_roll = random.randint(1,6)
 print(f"the first dice rolled:{first_dice_roll}")
 print(f"If you guess it correctly, you win {wager * 2}")


 if guess == first_dice_roll:
  if wager <= 100:
   print(f"Congratulations, you win {wager * 2}" )
 elif wager > 100:
   print("Thats too much, sorry")
 else:
  print(f"you lost your wager {wager}")  
  
elif play == "no":
 print("Thanks, see you soon!")
else:
 print("Invalid input, Please try again")
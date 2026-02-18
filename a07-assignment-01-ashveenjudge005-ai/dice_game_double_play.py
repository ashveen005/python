import random

# first dice roll is an int
first_dice_roll = random.randint(1,6)

# second dice roll is an int
second_dice_roll = random.randint(1,6)

# YOUR CODE BELOW
print('Welcome to the Dice Game, if you win you win double!')
play=input('Would you like to play?(yes/no)')

if play == "yes" :
 pass

elif play == "no":
 print("Thanks, see you soon!")
 exit()
else:
 print("Invalid input, Please try again")
 exit()

wager= int(input("How much do you like to wager?(enter an integer less than or equal 100)"))
guess= int(input("What is your guess number guess? (1-6) "))

total = 0


if guess== first_dice_roll:
 print(f"Congratulations, you win {wager*2}" )
 current_total = total + wager*2
elif wager > 100:
  print(f"Thats too much sorry")
else:
  print(f"you lost your wager { abs(total - wager ) }")
  current_total= total - wager

double_play_amount = abs(current_total * 2)

double_play= input(f"Would you like to double play for {double_play_amount}(yes/no)")
if double_play == "yes":
 
 second_guess= int(input("What is your guess number guess? (1-6)"))
 
 if second_dice_roll== second_guess:
  current_total+= double_play_amount
  print(f"Wow! you won all { current_total} in total ")
  

 else:
  print(f"you lose all{current_total-double_play_amount} in total")
else:
 print(f"Thank you, your current total is {current_total}")
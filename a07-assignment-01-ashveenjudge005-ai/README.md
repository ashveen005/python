[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/7V59bL7h)
# SDEV 1001 - Assignment 1

This assignment covers introduction to programming, version control and making decisions.

## Instructions

### Part 1: Simple Dice Game

You will create a simple dice game where you prompt the user for the betting amount and and we will check to see if they guessed the correct roll.

1. First you will ask if the user wants to play based on a `"yes"` or `"no"` input.
    - If the user enters `"yes"` then go on to play the game (described in the next steps)
    - If the user enters `"no"` display `"Thanks, see you soon"`
    - If the user enters anything else please enter `"Invalid input, Please try again"`

2. If the user plays the game then you will prompt them for two inputs and immediately convert them to integers.
    - the betting amount, you can use the following string in your code: `"How much would you like to wager? (enter an integer less than or equal 100) "`
    - the guess of the user `"What is your guess number guess? (1-6) "`
    - Note: the dice roll guess is given to you as the variable `first_dice_roll` in the file.
Note: take a look at the `Analysis` part of this section.

3. To play the game the user will have to bet **less than 100**, if they **guess the dice roll then they will win two times the amount**. If they lose they will lose it all. Use the following strings in your conditional appropriately. (these use a bet of 50)
    - "That's too much sorry"
    - "Congratulations, you win 100"
    - "You lost your wager 50"

Note: Refer to the `Desired output` section

#### Analysis
What error occurs if you put the string `"five"` when you prompt the user the wager and guess in Part two (Remove "Your Answer Here")

Error Type that occurs: ValueError # error line Error Type that occurs: "Your Answer Here"
Why Does it occur? You can't convert a string to an integer. # Why Does it occur? "Your Answer Here"

#### Desired Output

- user doesn't want to play the game.
```
$ python simple_dice_game.py
Welcome to the Dice Game
Would you like to play? (yes/no) no
Thanks, see you soon
```
- invalid input
```
$ python simple_dice_game.py
Welcome to the Dice Game
Would you like to play? (yes/no) potato
Invalid input, Please try again
```
- valid wager and incorrect guess
```
Welcome to the Dice Game
Would you like to play? (yes/no) yes
How much would you like to wager? (enter an integer less than or equal 100) 50
What is your guess number guess? (1-6) 2
If you guess correctly you win 100
You lost your wager 50
```
- valid wager, and correct guess
```
$ python simple_dice_game.py
Welcome to the Dice Game
Would you like to play? (yes/no) yes
How much would you like to wager? (enter an integer less than or equal 100) 50
What is your guess number guess? (1-6) 1
If you guess correctly you win 100
Congratulations, you win 100
```
- invalid wager
```
$ python simple_dice_game.py
Welcome to the Dice Game
Would you like to play? (yes/no) yes
How much would you like to wager? (enter an integer less than or equal 100) 9001
What is your guess number guess? (1-6) 1
If you guess correctly you win 18002
That's too much sorry
```

### Part 2: Dice Game Double play

Here you'll be prompting the user whether or not they want to double their bet and guess again.

1. Copy all of your working code from part 1 to create the first part of the double play dice game in the file the `dice_game_double_play.py` file after the line `# YOUR CODE BELOW`

2. Keep track of the winnings or what you lost from the Part 1. Note this should be positive if the user has won and negative if they have lost.

3. Only prompt the user for the double play if they have a valid betting amount.
    - The amount at stake will will be twice the previous winning (whether they won or not) amount (or 4 times the original bet).
    - use the following string (displayed for a bet of 50 originally) `"\nWould you like to go double play for 200? (yes/no) "`
    - if they don't want to play please display `"Thank you, your current total is CURRENT_AMOUNT_HERE"`

4. If they want to play prompt them for a guess and immediately convert it to an integer.
    - use the following string `"What is your guess number guess? (1-6) "`
    - Note: the dice roll guess is given to you as the variable `second_dice_roll` in the file.

5. Handle the winning conditions
   - if they guess correctly then add up the winnings from the first play and the double play and display it to ther user use the string `"Wow! you won all CURRENT_AMOUNT_HERE in total"`
   - if they don't guess correctly `"You lose all {current_amount} in total"`

#### Desired Output
- won original bet, won second bet
```
Welcome to the Dice Game, if you win you win double!
Would you like to play? (yes/no) yes
How much would you like to wager? (enter an integer less than or equal 100) 50
What is your guess number guess? (1-6) 1
Congratulations, you win 100

Would you like to go double play for 200? (yes/no) yes
What is your guess number guess? (1-6) 1
Wow! you won all 300 in total
```
- lost first, won second
```
Welcome to the Dice Game, if you win you win double!
Would you like to play? (yes/no) yes
How much would you like to wager? (enter an integer less than or equal 100) 100
What is your guess number guess? (1-6) 2
You lost your wager 100

Would you like to go double play for 400? (yes/no) yes
What is your guess number guess? (1-6) 1
Wow! you won all 300 in total
```
- lost both bets
```
Welcome to the Dice Game, if you win you win double!
Would you like to play? (yes/no) yes
How much would you like to wager? (enter an integer less than or equal 100) 50
What is your guess number guess? (1-6) 2
You lost your wager 50

Would you like to go double play for 100? (yes/no) yes
What is your guess number guess? (1-6) 2
You lose all -150 in total
```
- won first, lost second
```
Welcome to the Dice Game, if you win you win double!
Would you like to play? (yes/no) yes
How much would you like to wager? (enter an integer less than or equal 100) 50
What is your guess number guess? (1-6) 1
Congratulations, you win 100

Would you like to go double play for 200? (yes/no) yes
What is your guess number guess? (1-6) 2
You lose all -100 in total
```
- won first, didn't want to play the double
```
Welcome to the Dice Game, if you win you win double!
Would you like to play? (yes/no) yes
How much would you like to wager? (enter an integer less than or equal 100) 50
What is your guess number guess? (1-6) 1
Congratulations, you win 100

Would you like to go double play for 100? (yes/no) no
Thank you, your current total is 100
```

#### Desired Output

## Marking Key

#### 2 points - Parts 1 - Analysis

| Level             | Feedback Description                         |
| ----------------- | -------------------------------------------- |
| Correct           | Values are correct. Explanation Makes sense. |
| Partially Correct | One of the two answers makes sense.          |
| Missing/Incorrect | Not Correct, no marks                        |

#### 6 points - Part 1 - Code

| Level                | Feedback Description                                                                   |
| -------------------- | -------------------------------------------------------------------------------------- |
| Excellent            | Code looks like desirable output, code is formatted correctly.                         |
| Satisfactory         | Code looks like desirable output but code formatted incorrectly.                       |
| Incomplete/Incorrect | Code does not behave like desirable output but the program works somewhat.             |
| Poor                 | Code does not behave like desirable output don't, program does not use best practices. |
| Missing              | Broken/Missing/Way Off                                                                 |

#### 8 Points - Part 2 - Code

| Level                | Feedback Description                                                                               |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| Excellent            | Code looks like desirable output, code is formatted correctly.                                     |
| Satisfactory         | Code looks like desirable output but code formatted incorrectly one test may not for this section. |
| Incomplete/Incorrect | Code does not behave like desirable output but the program works somewhat.                         |
| Poor                 | Code does not behave like desirable output don't, program does not use best practices.             |
| Missing              | Broken/Missing/Way Off                                                                             |

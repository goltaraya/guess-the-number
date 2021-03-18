# Guess the number
# Author >>> Yago Goltara

import random               # Imports random module
from logo import logo       # Imports logo from logo.py
from os import system       # Imports system() function
from time import sleep      # Imports sleep() function

number = random.randint(1,100)      # The computer chooses a number randomly

def level(difficulty):              # Defines the number of lives due difficulty choosen
    if difficulty == 'easy':
        live = 10
        return live
    elif difficulty == 'hard':
        live = 5
        return live

difficulty = input("Choose a difficulty: 'easy' or 'hard'\n").lower()

lives = level(difficulty)

sleep(0.3)
system('cls')
print(logo)

while lives != 0:
    guess = int(input("Type a number between 1 and 100: "))     # The user inserts a number between 1 and 100
    
    if guess == number:                                         # If the user's guess is equal to the number choosen,
        print("You win!")                                       # then, it wins
        lives = 0
        break
    elif guess > number:                                        # If it's higher, prints that is too high 
        print("Your guess is too high!")
        lives -= 1
    elif guess < number:                                        # If it's lower, prints that is too low
        print("Your guess is too low.")
        lives -= 1 
    print(f"You still have {lives} lives.\n")                   # Indicates how many lives the user has yet
    if lives == 0:                                              # If the lives be equal to 0, the user loses
        print("Oh oh... You lose!")

sleep(5)
# Python Project 6
# Guess the number
import random
import os
easy=10
hard=3
choice=False
print("      GUESS THE NUMBER GAME         ")
print("Let me think of a number between 1 to 50.")
number=random.randint(1,50)
level=(input("Choose level of the difficulty...Type 'easy' or 'hard': ")).lower()
if level not in ('easy','hard'):
    print("Type 'easy' or 'hard' ")
    level=(input("Choose level of the difficulty...Type 'easy' or 'hard': ")).lower()
if(level=='easy'):
    print(f"You have {easy} attempts remaining to guess the answer!")
    attempts=easy
elif(level=='hard'):
    print(f"You have {hard} attempts remaining to guess the answer!")
    attempts=hard

while not choice:
    if(attempts>0):
        guess=int(input("Make a Guess: "))
        if(number>guess):
            print("Your Guess is too low")
            print("Guess again")
            attempts=attempts-1
            print(f"You have {attempts} remaining to guess the number!")
        elif(number<guess):
            print("your Guess is too high")
            print("Guess again")
            attempts=attempts-1
            print(f"You have {attempts} attempts remaining to guess the number!")
        elif(number==guess):
            print("Your Guess is right.")
            print(f"Your number is {number}.")
            choice=True
if(attempts<=0):
    print("you lose")
    os.system('cls')

#python project-1
# Rock Paper Scissors Game
import random
print("WELCOME TO THE GAME ROCK PAPER SCISSORS")
userchoice=input("Enter your choice(rock,paper,scissors):")
clist=["rock","paper","scissors"]
computerchoice=random.choice(clist)
print(f"computerchoice: {computerchoice}")
if(userchoice==computerchoice):
    print("Match Draw")
elif((userchoice=="rock" and computerchoice=="scissors") or (userchoice=="scissors" and computerchoice=="paper") or (userchoice=="paper" and computerchoice=="rock")):
    print("Congratulations You are the Winner🎉🎊🎉")
elif((userchoice!="rock") or (userchoice!="paper") or (userchoice!="scissors")):
    print(f"ERROR!!!!!!!!!!")
else:
    print("Computer Wins😢😢")

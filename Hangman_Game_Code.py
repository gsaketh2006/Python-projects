#Python Project 3
#  Hangman Game
import random
import hangman_stages
print("Welcome To Hangman Game")
words=["apple","mango","beautiful","papaya","guava","handsome","potato"]
lives=6
word=random.choice(words)
w=list(word)          #apple
blanks=[]
for i in range(1,len(w)+1):
    blanks.append("_")
print(blanks)
gameover=False
count=0
while not gameover:
    letter=input("Guess a letter: ").lower()
    if letter in w:
        for i in range(len(w)):
            if(w[i]==letter):
                blanks[i]=letter
        print(blanks)
        if "_" not in blanks:
            gameover=True
    else:
        lives=lives-1
        print(hangman_stages.stages[lives])
    if(lives==0):
        gameover=True
        
if(lives==0):
    print("You lose")  
    print(f"The word is '{word}'")
else:
    print("You won🎉🎉🎉")

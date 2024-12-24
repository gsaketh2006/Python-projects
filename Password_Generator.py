#python project 2
#Password generator
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']
print("WELCOME TO PASSWORD GENERATOR")
l=int(input("How many letters you want in your password?\n"))
n=int(input("How many symbols you want in your password?\n"))
s=int(input("How many numbers you want in your password?\n"))
password=[]
for i in range(1,l+1):
    char=random.choice(letters)
    password+=char
for i in range(1,n+1):
    char=random.choice(symbols)
    password+=char
for i in range(1,s+1):
    char=random.choice(numbers)
    password+=char
random.shuffle(password)
p=""
for i in password:
    p=p+str(i)
print(f"Password: {p}")

# Python Project 5
# Silent Auction Program
import os
def winner(bidden_details):
    max=0
    winner=""
    for i in bidden_details:
        price=bidden_details[i]
        if(price>max):
            max=price
            winner=i
    print(f"Congratulations {winner} 👏👏🎉🎉🎉🥳🥳🥳")
    print(f" You are the winner and with a bid {max}💲")
print("        WELCOME TO SILENT AUCTION PROGRAM        ")
bidden_data={}
end_auction=False
while not end_auction:
    name=input("What is your name: ")
    bid=int(input("What is your bid: "))
    bidden_data[name]=bid
    check=input("Are there any more bidders if there type 'yes' if not there type 'no': ").lower()
    if check not in ('yes','no'):
        print("\nType correctly 'yes' or 'no'\n")
        check=input("Are there any more bidders if there type 'yes' if not there type 'no': ").lower()
    elif(check=='no'):
        end_auction=True
        os.system('cls')
        winner(bidden_data)
    elif(check=='yes'):
        os.system('cls')
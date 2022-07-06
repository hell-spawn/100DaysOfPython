import os
from art import logo
#HINT: You can call clear() to clear the output in the console

clear = lambda: os.system('cls||clear')

print(logo)
print("Welcome to the secret auction program.")

more = True

bidders = []
bidder_won = {"name": "unkhown", "bid": 0}

while more:
    
    name = input("What's your name?: ")
    bid = input("What's your bid?: $")
    other_bidders = input("Are there any other_bidders? Type 'yes' or 'no'.\n")

    bidders.append({"name": name, "bid": int(bid)})

    if other_bidders.lower() == 'no':
        more = False
    clear()

for bidder in bidders:
     
    if bidder_won['bid'] <  bidder['bid']:
        bidder_won = bidder


print(f"The winner is {bidder_won['name']} with a bid of ${bidder_won['bid']}")

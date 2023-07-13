import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

from art import logo

print(logo)
print("Welcome to the secret auction program. \n")

continue_auction = True
bids = {}

while continue_auction:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    # fill the dictionary with name and bid
    bids[name] = bid

    max_bid = max(bids.values())
    any_other_bidders = input(
        "Are there any other bidders? Type 'yes' or 'no'. \n")
    if any_other_bidders == 'yes':
        #clear the screen
        cls()
        print(logo)
        print("Welcome to the secret auction program. \n")
    elif any_other_bidders == 'no':
        winner = name
        print(f"The winner is {winner} with a bid of ${max_bid}. ")
        continue_auction = False
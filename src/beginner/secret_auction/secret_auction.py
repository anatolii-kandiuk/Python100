import os

user_bid = {}
stop_bidding = False

while stop_bidding == False:
    username = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))

    user_bid[username] = bid_amount

    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    
    if continue_bidding == "no":
        stop_bidding = True

    os.system('cls' if os.name == 'nt' else 'clear')

winner = max(user_bid, key=user_bid.get)
print(f"\nThe winner is {winner} with a bid of ${user_bid[winner]}.\n")
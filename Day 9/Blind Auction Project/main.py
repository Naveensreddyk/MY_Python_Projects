import art
print(art.logo)
print("*********************************WELCOME TO THE SECRET AUCTION****************************")
def highest_bidding(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of $ {highest_bid}")

bids = {}
continue_bidding = True
while continue_bidding:
    Name = input("What is your name?")
    price = float(input("What is your bid amount? $"))
    bids[Name] = price
    extra_bidders = input("Are there any bidders Type YES or NO\n").lower()
    if extra_bidders == "no":
        continue_bidding = False
        highest_bidding(bids)
    elif extra_bidders == "yes":
        print("\n" * 100)







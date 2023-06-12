import day9_art

# HINT: You can call clear() to clear the output in the console.
# Name is the key, value is the bid
bids = {}
name = ''
bid = ''


def new_bid(input_name, input_bid):
    bids[input_name] = input_bid


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} and the highest bid is {highest_bid}")


print(day9_art.logo)
more_bids = "y"

while more_bids == "y":
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    new_bid(name, bid)
    more_bids = input("Does anyone else want to bid? Enter 'y' for yes, or 'n' for no: ")

find_highest_bidder(bids)


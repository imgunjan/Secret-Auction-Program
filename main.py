from click import clear
from art import logo
print(logo)
print("Welcome to secret auction Program")
# Creating a empty Dictionary
bidding_price = {}
checking_bidding = False


def highest_number_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # lets see how our dictionary look like
    # bidding_record={"Gunjan": 125,"Anish":130}
    for bidder in bidding_record:
        bid_amt = bidding_record[bidder]
        if bid_amt > highest_bid:
            highest_bid = bid_amt
            winner = bidder
    print(f"the winner is {winner} with the bid of RS{highest_bid}")


while not checking_bidding:
    name = input("Enter your name :")
    initial_bid = int(input("what is your bidding price? Rs"))
    # Adding a new entry to bidding price dictionary
    bidding_price[name] = initial_bid
    Exit = input("Are there any bidder left? Type 'yes' or 'no'.\n")
    if Exit == "no":
        checking_bidding = True
        highest_number_bidder(bidding_price)
    elif Exit == "yes":
        clear()

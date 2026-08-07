# TODO-1: Ask the user for input
from art import logo
print(logo)
name = input("What is your name? : ")
price = int(input("What is your bid ? : "))

bid_dict ={}

# TODO-2: Save data into dictionary {name: price}

bid_dict[name] = price

# TODO-3: Whether if new bids need to be added

cond = input("Are there any other bidders? type yes or no : ")
print("\n"*20)

def compare_bids(bid_dict):
    winner = ""
    the_highest_bid = 0
    for key in bid_dict :
        bid_value = bid_dict[key]
        if bid_value > the_highest_bid :
            the_highest_bid = bid_dict[key]
            winner = key
    print(f"the winner is {winner} with highest a bid of {the_highest_bid}$")

continue_bid = True

while continue_bid :
    name = input("What is your name? : ")
    price = int(input("What is your bid ? : "))
    bid_dict[name] = price
    cond = input("Are there any other bidders? type yes or no : ").lower()
    if cond == "yes":
        print("\n"*20)
        name = input("What is your name? : ")
        price = int(input("What is your bid ? : "))
        bid_dict[name] = price
        cond = input("Are there any other bidders? type yes or no : ").lower()
    elif cond == "no":
        continue_bid = False
        compare_bids(bid_dict)

# TODO-4: Compare bids in dictionary

    # def compare_bids(bid_dict):
    #     winner = ""
    #     the_highest_bid = 0
    #     for key in bid_dict:
    #         bid_value = bid_dict[key]
    #         if bid_value > the_highest_bid:
    #             the_highest_bid = bid_dict[key]
    #             winner = key
    #     print(f"the winner is {winner} with highest a bid of {the_highest_bid}")
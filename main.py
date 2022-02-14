import os
from art import logo
print(logo)

def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        total = bidding_record[bidder]
        if total > highest_bid:
            highest_bid = total
            winner = bidder
    print(f'The Winner Is {winner} With A Bid Of £{highest_bid}')

users_left = True
bids = {}

while users_left:
    name = input('What is your name ? \n')
    price = int(input('What is your bid ? \n'))
    bids[name] = price 
    any_left = input("Anyone else wants to bid ? ('Yes'or'No') \n")
    if any_left.lower() == 'no':
        users_left = False
        find_highest_bid(bids)
    elif users_left == True:
        os.system('clear')


 
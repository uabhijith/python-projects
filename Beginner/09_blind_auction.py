#import os
bids={}
bid_finished= False
def highest_bidder(record):
    #a=10,b=20,c=30,d=40,e=10
    #a=0
    highest=0
    winner=""
    for item in record:
        amount=record[item]
        if amount>highest:
            highest=amount
            winner=item
    print(f"the winner is {winner} with a bid of ${highest}")




while  not bid_finished:
    name = input("What is your name: ")
    price = int(input("your bid: $"))
    bids = {name: price}
    should_continue = input("Are there any other bidders? 'yes' or 'no' :").lower()
    if should_continue=="no":
        bid_finished= True
    #else: os.system('cls')

#print(bids)
highest_bidder(bids)
 #for item in auction:
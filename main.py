from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)



def find_highest_bidded(bidding_record):
    highest_bidder = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount>highest_bidder:
            highest_bidder=bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bidder}")

condition = True
dicionary = {}

while condition:
    name = input("What is your name ? \n")
    price = int(input("What is your bid ? \n$"))  
    
    dicionary[name] = price 

    continue_yes_or_no = input("Are there any other bidders? Type 'yes' or 'no'\n")

    if continue_yes_or_no=="yes":
        clear()
        condition = True

    else:
         condition=False
         find_highest_bidded(dicionary)

# print(f"The winner is {} with a bid of {}")
# print(dicionary)
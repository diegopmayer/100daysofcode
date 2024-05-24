import clear

def blind_auction():
    print("Welcome to the secret auction program.")

    other_bidder = "yes"
    bidder = dict()
    bidder_max = dict()
    while other_bidder == "yes":
        name = input("What is your name?: ")
        bid = float(input("What's your bid?: $"))
        bidder[name] = bid
        other_bidder = input("Are there any other bidders? Type 'yes' ro 'no'.\n")
        if other_bidder == "yes":
            clear.clear()

    for key, value in bidder.items():
        if value == max(bidder.values()):
            print(f"The winner is {key} with a of ${value}")

blind_auction()
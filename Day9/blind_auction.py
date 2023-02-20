
bids = []


def highest_bidder():
    max = 0
    winner_name = ""
    winner_bid = 0
    for key in bids:
        # print(key)
        print(key, key['bid'], bids, len(bids))
        if key['bid'] > max:
            max = key['bid']
            winner_name = key['name']
            winner_bid = key['bid']

    print(f"Winner is {winner_name} with a bid of {winner_bid}")


def auction(name, bid):
    bids.append({'name': name, 'bid': bid})
    if input("Other bidders? (y)") == "y":
        auction(input('Name?'), int(input("Bid?")))


auction(input('Name?'), int(input("Bid?")))
highest_bidder()

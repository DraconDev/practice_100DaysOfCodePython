import random


def ace_lower(hand):
    if sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw(hand):
    print(f"Your hand value {hand}")
    if sum(hand) < 21:
        print("Draw a card? y or n")
        if input() == 'y':
            hand.append(random.choice(cards))
            ace_lower(hand)
            draw(hand)
    return hand


def opponent_hand():
    hand = [random.choice(cards), random.choice(cards)]
    while sum(hand) < 17:
        hand.append(random.choice(cards))
        # print(hand)
        ace_lower(hand)
    print(f"Opp hand {hand}")
    return sum(hand)


def player_hand():
    hand = [random.choice(cards), random.choice(cards)]
    draw(hand)
    print(f"Your hand {hand}")
    return sum(hand)


def winner(player_hand, opponent_hand):
    if player_hand > 21:
        return "Lose"
    elif opponent_hand > 21:
        return "Win"
    elif player_hand > opponent_hand:
        return "Win"
    elif player_hand == opponent_hand:
        return "Tie"
    else:
        return "Lose"


# print("Your hand", player_hand())
# print("Opp hand", opponent_hand())
print(winner(player_hand(), opponent_hand()))

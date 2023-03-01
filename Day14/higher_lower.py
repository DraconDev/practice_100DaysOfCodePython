import random

import game_data


def guess():
    pick()


def pick():
    score = 0
    while True:
        if score > 0:
            pick1 = pick2
            print(pick1)
            pick2 = random.choice(game_data.data)
        else:
            pick1 = random.choice(game_data.data)
            pick2 = random.choice(game_data.data)
        if pick1 == pick2:
            pick2 = random.choice(game_data.data)
        print(
            f"Who has more followers? {pick1['description']} {pick1['name']} from {pick1['country']}\n")
        print('or\n')
        print(
            f"Who has more followers? {pick2['description']} {pick2['name']} from {pick2['country']}\n")
        guess_which = int(input("1 or 2\n"))
        if (guess_which == 1 and pick1['follower_count'] > pick2['follower_count']):
            score += 1
            pick2 = pick1
        elif (guess_which == 2 and pick1['follower_count'] < pick2['follower_count']):
            score += 1
        else:
            print(f"Game over your score {score}")
            return


guess()

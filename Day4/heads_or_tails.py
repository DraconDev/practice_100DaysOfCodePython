import random

random_number = random.randint(1, 2)


def heads_or_tails(random):
    if random == 2:
        print("heads")
    else:
        print("tails")


heads_or_tails(random_number)

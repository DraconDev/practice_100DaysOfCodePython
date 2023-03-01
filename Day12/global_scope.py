enemies = ['zombie']


def test():
    # enemies = 1
    # The return keyword is to exit a function and return a value.
    # return has access to outer scope !!
    return enemies.append("cake")


cake = test()

print(cake, enemies)

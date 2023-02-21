from main import MENU, resources


def order():
    print("What would you like?\n")
    return input()


def menu():
    for item in MENU:
        print(f"{item}: ${MENU[item]['cost']}")


def update_ingredients(ordered_item):
    resources['water'] -= MENU[ordered_item]['ingredients']['water']
    resources['coffee'] -= MENU[ordered_item]['ingredients']['coffee']
    if "milk" in MENU[ordered_item]["ingredients"]:
        resources['milk'] -= MENU[ordered_item]['ingredients']['milk']


def coffee_machine():
    menu()
    ordered_item = order()
    check_availability(ordered_item)
    paid_coins = pay()
    # print(MEordered_item['cost'])
    if paid_coins > MENU[ordered_item]['cost']:
        update_ingredients(ordered_item)
        print(
            f"Enjoy your coffee, your change ${paid_coins - MENU[ordered_item]['cost']}")
    else:
        print("not enough money returning coins")


def pay():
    coins = {"quarter": 0.25, "dime": 0.10, 'nickel': 0.05, 'penny': 0.01}
    print("Add number of quarters, dimes, nickels, pennies")
    sum = 0
    sum += float(input()) * coins['quarter']
    sum += float(input()) * coins['dime']
    sum += float(input()) * coins['nickel']
    sum += float(input()) * coins['penny']
    return sum


def check_availability(order):
    if resources['water'] > MENU[order]["ingredients"]['water'] and resources['milk'] > MENU[order]["ingredients"]['milk'] if "milk" in MENU[order]["ingredients"] else True and resources['coffee'] > MENU[order]["ingredients"]['coffee']:
        print('available')
    else:
        print('not available')


coffee_machine()



from start.coffee_maker import CoffeeMaker
from start.menu import Menu, MenuItem
from start.money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()


def drink_machine():
    while True:
        money_machine.report()
        coffee_maker.report()
        print("What would you like?", menu.get_items())
        choice = input("Which drink?")
        order = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
            coffee_maker.make_coffee(order)
        else:
            return


drink_machine()

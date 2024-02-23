from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def make_coffee():
    is_on = True
    menu = Menu()
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    options = menu.get_items()
    while is_on:
        # user_choice = input("Hello, which drink would you like " + menu.get_items() + "?: ") // without making var options
        user_choice = input(f"What would you like? {options}: ")
        if user_choice == 'report':
            coffee_maker.report()
            money_machine.report()
        elif user_choice == 'off':
            is_on = False
        elif menu.find_drink(user_choice):
            drink = menu.find_drink(user_choice)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)



make_coffee()

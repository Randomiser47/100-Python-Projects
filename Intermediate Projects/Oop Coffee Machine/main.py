from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

options = menu.get_items()

is_on = True
while is_on:
    what_drink = input(f"What drink would you like? {options}\n")
    if what_drink == "off":
        is_on = False
    elif what_drink == "report":
       coffee_maker.report()
       money_machine.report()
    else:
        drink = menu.find_drink(what_drink)
        if drink is None:
            print("❌ Sorry, that item is not available.")
            continue  # Go back to the start of the loop
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
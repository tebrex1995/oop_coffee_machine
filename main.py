from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money = MoneyMachine()
coffee = CoffeeMaker()
# drink = menu.find_drink(service)

is_on = True

while is_on:
    service = input(f"What would you like to order? ({menu.get_items()}): ").lower()
    if service == "off":
        is_on = False
    elif service == "report":
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(service)
        if money.make_payment(drink.cost) and coffee.is_resource_sufficient(drink):
            coffee.make_coffee(drink)


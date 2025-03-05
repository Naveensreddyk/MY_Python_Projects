from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#we created an object coffe_maker to access Coffee Maker class. And same for the money machine.
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu_items = Menu()
is_on = True

while is_on:
    options = menu_items.get_items()
    choice = input(f"What would you like to have ({options})\n")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu_items.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)




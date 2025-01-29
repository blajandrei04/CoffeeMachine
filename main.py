from menu import Menu, MenuItem
from coffeeMaker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
cofee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}) ")
    if choice == "off":
        is_on = False
    elif choice == "report":                                #daca vrei sa printezi raportul
        cofee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if cofee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):   #verifica daca avem resurse si cafeau a fost platita
            cofee_maker.make_coffee(drink)
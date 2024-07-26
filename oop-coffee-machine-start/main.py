from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
s=input("What would you like? (espresso/latte/cappuccino/):")

def coffee():
    cfmake=CoffeeMaker()
    mnmachien=MoneyMachine()
    men=Menu()
    if s=="report":
        cfmake.report()
        mnmachien.report()
        return
    else:
        drink=men.find_drink(s)
        if cfmake.is_resource_sufficient(drink) and mnmachien.make_payment(drink.cost):
            cfmake.make_coffee(drink)
while not s=="off":
    coffee()
    s=input("What would you like? (espresso/latte/cappuccino/):")



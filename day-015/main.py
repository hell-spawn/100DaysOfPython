# Coffee Machine

from typing import Dict


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

ESPRESSO = "espresso"
LATTE = "latte"
CAPPUCCINO = "cappuccino"
REPORT = "report"
OFF = "off"

QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01

def get_money(value):
    """TODO: Docstring for get_money.

    :arg1: TODO
    :returns: TODO

    """
    print(f"Cost drink $ { value }, insert coins")
    cant_quarters = int(input("how many quarters: ")) 
    cant_dimes = int(input("how many dimes: ")) 
    cant_nickles = int(input("how many nickles: ")) 
    cant_pennies = int(input("how many pennies: ")) 
    total = (QUARTERS * cant_quarters)
    total += (DIMES * cant_dimes)
    total += (NICKLES *  cant_nickles)
    total += (PENNIES * cant_pennies)

    if value > total:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif value <= total:
        global money
        money += total
        print(f"Here is ${ total - value } in change.")
        return True
    else:
        return False


def prepare_drink(kind_of_drink):
    global resources
    drink = MENU[kind_of_drink]
    if not (resources["water"] - drink["ingredients"]["water"]) >= 0:
        print("Sorry there is not enough water.")
        return 
    if not (resources["milk"] - drink["ingredients"]["milk"]) >= 0:
        print("Sorry there is not enough milk.")
        return 
    if not (resources["coffee"] - drink["ingredients"]["coffee"]) >= 0:
        print("Sorry there is not enough milk.")
        return 

    if get_money(drink["cost"]):
        resources["water"] = (resources["water"] - drink["ingredients"]["water"])
        resources["milk"] = (resources["milk"] - drink["ingredients"]["milk"])
        resources["coffee"] = (resources["coffee"] - drink["ingredients"]["coffee"])
        print("Take your drink")

def report():
    """TODO: Docstring for report.
    """
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money:$ {money}")

def on_machine():
    run = True
    while run: 
        answer = input("What would you like? (espresso/latte/cappuccino): ")
        if answer == ESPRESSO:
            prepare_drink(ESPRESSO)
        elif answer == LATTE:
            prepare_drink(LATTE)
        elif answer == CAPPUCCINO:
            prepare_drink(CAPPUCCINO)
        elif answer == REPORT:
            report()
        elif answer == OFF:
            print("Turnning off")
            run = False
        else:
            print("Error: selection invalid")

on_machine()

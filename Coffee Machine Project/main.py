MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def calculating_money(money_received, drink_cost):
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    print(total)

    change = round(money_received - drink_cost, 2)

    if money_received < drink_cost:
        return "Not enough money to make the drink"
    elif money_received > drink_cost:
        global profit
        profit += drink_cost
        return f"Here is your remaining change: ${change}"


def is_resources_available(drink_name):
    if drink_name in MENU:
        drink = MENU[drink_name]["ingredients"]
        enough_resources = True
        for item in drink:
            if drink[item] > resources[item]:
                print("we don't have enough")
                enough_resources = False
        else:
            print("Please insert coins:")

def money_sufficient(money_received, drink_cost):
    change = round(money_received - drink_cost, 2)
    if money_received < drink_cost:
        return "Not enough money to make the drink"
    elif money_received > drink_cost:
        global profit
        profit += drink_cost
        return f"Here is your remaining change: ${change}"

user_choice = input("What would you like to have? (espresso, latte, cappuccino)\n").lower()
is_resources_available(user_choice)


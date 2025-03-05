import sys  # Used for controlling output behavior like smooth text display
import time  # Used for adding a slight delay to create a typing effect

# Coffee Machine Menu containing available drinks, their required ingredients, and costs
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

# Tracks the total profit earned by the coffee machine
profit = 0

# Stores the available resources in the machine (water, milk, coffee)
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def fancy_print(message, delay=0.05):
    """
    Displays text with a smooth typing effect for better user experience.
    :param message: The text to be printed with animation.
    :param delay: The time delay (in seconds) between each character being printed.
    """
    for char in message:
        sys.stdout.write(char)  # Prints one character at a time
        sys.stdout.flush()  # Ensures immediate output display
        time.sleep(delay)  # Adds delay between character printing for smooth effect
    print()  # Moves to a new line after printing the message


def is_resource_sufficient(order_ingredients):
    """
    Checks if there are enough ingredients in the machine to make the requested drink.
    If any ingredient is insufficient, it notifies the user and returns False.
    :param order_ingredients: Dictionary of ingredients required for the chosen drink.
    :return: True if all ingredients are available, False otherwise.
    """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            fancy_print(f"\033[1;31m❌ Sorry, there is not enough {item}.\033[0m")  # Red colored error message
            return False
    return True


def process_coins():
    """
    Handles coin input from the user and calculates the total amount inserted.
    Prompts user for each type of coin (quarters, dimes, nickels, pennies) and sums up the value.
    :return: The total amount of money inserted by the user.
    """
    fancy_print("💰 Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """
    Validates if the user has inserted enough money for the selected drink.
    If payment is sufficient, calculates change and updates profit.
    :param money_received: The total amount of money inserted.
    :param drink_cost: The cost of the selected drink.
    :return: True if the transaction is successful, False otherwise.
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        fancy_print(f"\033[1;32m✅ Here is ${change} in change.\033[0m")  # Green colored success message
        global profit
        profit += drink_cost  # Update total profit with drink cost
        return True
    else:
        fancy_print("\033[1;31m❌ Sorry, that's not enough money. Money refunded.\033[0m")
        return False


def make_coffee(drink_name, order_ingredients):
    """
    Deducts the required ingredients from the machine's resources after a successful purchase.
    :param drink_name: The name of the selected drink.
    :param order_ingredients: Dictionary of ingredients required for the selected drink.
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]  # Deducts used ingredients from available resources
    fancy_print(f"\033[1;33m☕ Here is your {drink_name}. Enjoy!\033[0m")  # Yellow colored message for serving coffee


# Machine is initially set to ON state
is_on = True

while is_on:
    # Ask user for their drink choice with a styled message
    fancy_print("\033[1;36mWhat would you like? (espresso/latte/cappuccino):\033[0m", delay=0.02)
    choice = input().lower()  # Convert input to lowercase to handle case variations

    if choice == "off":
        # If user types 'off', turn off the machine
        is_on = False  # Exits the loop, effectively stopping the program
        fancy_print("\033[1;31m🚪 Turning off the coffee machine... Goodbye!\033[0m")
    elif choice == "report":
        # If user requests a report, display the current resource levels and profit earned
        fancy_print(f"\033[1;34m📋 Resource Report:\033[0m")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice in MENU:
        # If the user selects a valid drink, proceed with checking resources and payment
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        # If user enters an invalid choice, display an error message
        fancy_print("\033[1;31m❌ Invalid choice. Please try again.\033[0m")

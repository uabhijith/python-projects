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


def is_resource_sufficient(order_ingredient):
    """Returns True when order can be made, false if resources are insufficient"""
    for item in order_ingredient:
        if order_ingredient[item] > resources[item]:
            print(f"sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """returns total calculated coins inserted"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕ .Enjoy!\n\n")


def report():
    print("---------------Report---------------")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}gm")
    print(f"Money: ${profit}")


def refill():
    print("--------------REFILL---------------")
    resources['water'] += int(input(" How much ml water do you want to add?:"))
    resources['milk'] += int(input(" How much ml milk do you want to add?:"))
    resources['coffee'] += int(input(" How much gm coffee do you want to add?:"))
    report()


# todo 1
check_on = True
print("----------------------COFFEE MACHINE----------------------")
while check_on:
    choice = input("What would you like?:"
                   "\n1.Espresso 2.Latte 3.Cappuccino :\n").lower()

    if choice == "report":
        report()
    elif choice == "off":
        check_on = False
    elif choice == "refill":
        """refill resources"""
        refill()
    else:
        #if choice == 1:
        #    choice = "espresso"
        #elif choice == 2:
        #    choice = "latte"
        #elif choice == 3:
        #    choice = "cappuccino"
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

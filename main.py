import machineData

TURN_OFF = False


def print_report():
    print(f"Current resource values: \n Water: {machineData.resources['water']}ml \n Milk: {machineData.resources['milk']}ml \n"
          f" Coffee: {machineData.resources['coffee']}g \n Money: ${machineData.resources['money']}")


def check_resources(user_option):
    for resource in machineData.MENU[user_option]["ingredients"]:
        if machineData.resources[resource] <= machineData.MENU[user_option]["ingredients"][resource]:
            print(f"Sorry there is not enough {resource}.")
            return False
    return True


def validate_option(user_option):
    if user_option in machineData.valid_options:
        return True
    else:
        print(f"{user_option} is not a valid option.")
        return False


def create_coffee(user_option):
    if user_option == "espresso":
        print("Here is your espresso ☕. Enjoy!")
    elif user_option == "latte":
        print("Here is your latte ☕. Enjoy!")
    elif user_option == "cappuccino":
        print("Here is your cappuccino ☕. Enjoy!")


def process_coins():
    print("Please insert coins.")
    quarters_amount = int(input("How many quarters?: "))
    dimes_amount = int(input("How many dimes?: "))
    nickles_amount = int(input("How many nickles?: "))
    pennies_amount = int(input("How many pennies?: "))
    total_amount = quarters_amount * machineData.coins_values["quarters"] \
                   + dimes_amount * machineData.coins_values["dimes"] \
                   + nickles_amount * machineData.coins_values["nickles"] \
                   + pennies_amount * machineData.coins_values["pennies"]
    return total_amount


def validate_transaction(user_option):
    money_inserted = process_coins()
    coffee_cost = machineData.MENU[user_option]["cost"]
    if money_inserted < coffee_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        machineData.resources["money"] += coffee_cost
        for resource in machineData.MENU[user_option]["ingredients"]:
            machineData.resources[resource] -= machineData.MENU[user_option]["ingredients"][resource]
        if money_inserted > coffee_cost:
            change = round(money_inserted - coffee_cost, 2)
            print(f"Here is ${change} dollars in change.")
        return True


while not TURN_OFF:
    option = input("What would you like? (espresso/latte/cappuccino): ")
    if validate_option(option):
        if option == "report":
            print_report()
        elif option == "off":
            TURN_OFF = True
        else:
            if check_resources(option):
                if validate_transaction(option):
                    create_coffee(option)

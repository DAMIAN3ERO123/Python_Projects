from dictionaries import MENU, resources
from art import logo


# TODO Revisar si el dinero ingresado es suficiente
def pay(coffe_type):
    print("Please insert coins.")
    quarters = float(input("how many quarters?: ")) * .25
    dimes = float(input("how many dimes?: ")) * .10
    nickles = float(input("how many nickles?:")) * .05
    pennies = float(input("how many pennies?:")) * .01
    total = quarters + dimes + nickles + pennies
    if total == MENU[coffe_type]["cost"]:
        print("Here is your espresso ☕️.Enjoy!")
        return True
    # TODO Dar cambio si el monto fue mayor
    elif total > MENU[coffe_type]["cost"]:
        change = round(total - MENU[coffe_type]["cost"], 2)
        print(f"Here is ${change} dollars in change.")
        print("Here is your espresso ☕️.Enjoy!")
        update_report(total, coffe_type)
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def update_report(total, coffe_type):
    if coffe_type == "espresso":
        discount = resources["water"] - MENU[coffe_type]["ingredients"]["water"]
        resources["water"] = discount
        discount = resources["coffee"] - MENU[coffe_type]["ingredients"]["coffee"]
        resources["coffee"] = discount
    else:
        discount = resources["water"] - MENU[coffe_type]["ingredients"]["water"]
        resources["water"] = discount
        discount = resources["coffee"] - MENU[coffe_type]["ingredients"]["coffee"]
        resources["coffee"] = discount
        discount = resources["milk"] - MENU[coffe_type]["ingredients"]["milk"]
        resources["milk"] = discount


machine_is_running = True

while machine_is_running:

    print(logo)

    user_choice = input("What would you like? (espresso 'cost:1.5' / latte 'cost: 2.5' / cappuccino 'cost: 3.0'): ")

    # TODO Revisar si la maquina tiene suficientes recursos para preparar el producto
    if user_choice == "espresso":
        if MENU["espresso"]["ingredients"]["water"] < resources["water"]:
            if MENU["espresso"]["ingredients"]["coffee"] < resources["coffee"]:
                if pay("espresso"):
                    resources["Money"] += 1.5
            else:
                print("Sorry there is not enough coffe.")
        else:
            print("Sorry there is not enough water.")
    elif user_choice == "latte":
        if MENU["latte"]["ingredients"]["water"] < resources["water"]:
            if MENU["latte"]["ingredients"]["coffee"] < resources["coffee"]:
                if MENU["latte"]["ingredients"]["milk"] < resources["milk"]:
                    if pay("latte"):
                        resources["Money"] += 2.5
                else:
                    print("Sorry there is not enough milk.")
            else:
                print("Sorry there is not enough coffe.")
        else:
            print("Sorry there is not enough water.")
    elif user_choice == "cappuccino":
        if MENU["cappuccino"]["ingredients"]["water"] < resources["water"]:
            if MENU["cappuccino"]["ingredients"]["coffee"] < resources["coffee"]:
                if MENU["cappuccino"]["ingredients"]["milk"] < resources["milk"]:
                    if pay("cappuccino"):
                        resources["Money"] += 3.0
                else:
                    print("Sorry there is not enough milk.")
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough water.")
    elif user_choice == "report":
        for resource in resources:
            if resource == "Money":
                print(f"{resource}: ${resources[resource]}")
            elif resource == "coffee":
                print(f"{resource.capitalize()}: {resources[resource]}g")
            else:
                print(f"{resource.capitalize()}: {resources[resource]}ml")
    elif user_choice == "off":
        machine_is_running = False

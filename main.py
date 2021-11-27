

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
gain = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def sufficient_resources(other_ingredients):
    for item in other_ingredients:
        if other_ingredients[item] >= resources[item]:
            print('Sorry there is no sufficient resources')
            return False
        return True

def coins():
    print("Please insert coins")
    total = int(input("How many Quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total
def transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received-drink_cost, 2)
        print(f"Here is ${change} change")
        global gain
        gain += drink_cost
        return True
    else:
        print("sorry there is no enough money")
        return False

def make_coffee(other_ingredients, drink_name):
    for item in other_ingredients:
        resources[item] -= other_ingredients[item]
    print(f"Here is your {drink_name}, Enjoy!")


machine_on = True
while machine_on:
    choose = input('Please Choose: espresso/latte/cappuccino: ')
    if choose == 'off':
        machine_on = False
    elif choose == 'report':
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${gain}")
    else:
        drink = MENU[choose]
        if sufficient_resources(drink['ingredients']):
            payment = coins()
            if transaction_successful(payment, drink['cost']):
                make_coffee(drink['ingredients'], choose)



machine_on = False

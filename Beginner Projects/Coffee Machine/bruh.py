import art
print(art.logo)

def coin_box(coffee_type,pennies,nickles,dimes,quarters):
    pennies = 0.01 * pennies
    nickles = 0.05 * nickles
    dimes = 0.10 * dimes
    quarters = 0.25 * quarters
    all_cash = pennies + nickles + dimes + quarters
    if all_cash < 1.50:
        print(f"Here is your money back, you can't afford anything")
        return False
    elif coffee_type == 'latte' and all_cash < 2.50:
        return print("You DONT HAVE ENOUGH MONEY BOZO, you can only afford an espresso")
    elif coffee_type == 'cappuccino' and all_cash < 3.00:
        return print("You DONT HAVE ENOUGH MONEY BOZO, you can only afford an espresso and latte")
    if coffee_type == 'espresso' and all_cash > 1.50:
        all_cash = all_cash - 1.50
    elif coffee_type == 'latte' and all_cash > 2.50:
        all_cash = all_cash - 2.50
    elif coffee_type == 'cappuccino' and all_cash > 3.00:
        all_cash = all_cash - 3.00
    return print(f"Here is your change ${all_cash}")

def machine_resource(coffee_type,material):
    if coffee_type == 'espresso' and material['water'] >=50 and material['coffee']>=18:
        water= material['water']-50
        coffee = material['coffee']-18
        milk = material['milk']
    elif coffee_type == 'latte' and material['water'] >=200 and material['coffee']>=24 and material['milk']>=150:
        water= material['water']-200
        coffee = material['coffee']-24
        milk = material['milk']-150
    elif coffee_type == 'capuccino' and material['water'] >=250 and material['coffee']>=24 and material['milk']>100:
        water= material['water']-250
        coffee = material['coffee']-24 
        milk = material['milk']-100
    leftover_resource = {
        'water' : water,
        'coffee' : coffee,
        'milk' : milk,
    }
    return leftover_resource


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
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

what_want = input("What would you like?\n 1.Espresso \n 2.Latte \n 3.Cappuccino\n").lower()
coin_pennies = float(input("How many pennies?: "))
coin_nickles = float(input("How many nickles?: "))
coin_dimes = float(input("How many dimes?: "))
coin_quarters = float(input("How many quarters?: "))
coinless = coin_box(coffee_type=what_want,pennies=coin_pennies,nickles=coin_nickles,dimes=coin_dimes,quarters=coin_quarters)
if coinless == False:
    print("i'm a horse")
    #break
if coinless != False:
    print(machine_resource(coffee_type=what_want, material=resources))
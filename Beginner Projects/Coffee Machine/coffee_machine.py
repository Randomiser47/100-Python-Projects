import art
print(art.logo)



MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0,
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

ORDER = True

def coin_box(coffee_type,coin,menu):
    profit = 0
    all_cash = coin
    if all_cash >= 3.00:
        if coffee_type in ['espresso','latte','cappuccino']:
            all_cash = all_cash - menu[coffee_type]['cost']
            profit += menu[coffee_type]['cost']
    return all_cash,profit

def check_money(coffee_type,coin,menu):
    check_coin = coin
    if check_coin < 1.5:
        False
    elif check_coin <2.50 and coffee_type == 'latte':
        return False
    elif check_coin <=2.50 and coffee_type == 'cappuccino':
        return False
    else:
        return True
            
def resource_mgmt(coffee_type,materials,menu):
    if coffee_type in ['espresso','latte','cappuccino']:
        water_cal = materials['water'] - menu[coffee_type]['ingredients']['water']
        coffee_cal = materials['coffee'] - menu[coffee_type]['ingredients']['coffee']
        milk_cal = materials['milk'] - menu[coffee_type]['ingredients']['milk']
    leftover_resource = {'water':water_cal,'coffee':coffee_cal,'milk':milk_cal}
    return leftover_resource

def check_resource(coffee_type,materials,menu):
    if coffee_type in ['espresso','latte','cappuccino'] and materials['water']>menu[coffee_type]['ingredients']['water']and materials['coffee']>menu[coffee_type]['ingredients']['coffee']:
        return True
    if materials['water']< menu[coffee_type]['ingredients']['water']:
        print("Water Resource has delpleted cannot make your drink")
        return False
    if materials['coffee']< menu[coffee_type]['ingredients']['coffee']:
        print("Coffee Resource has delpleted cannot make your drink")
        return False
    if materials['milk']< menu[coffee_type]['ingredients']['milk']:
        print("Milk Resource has delpleted cannot make your drink")
        return False
    return True

total_profit = 0
while ORDER == True:
    report = True
    while report == True:
        what_want = input("What would you like?\n 1.Espresso \n 2.Latte \n 3.Cappuccino\n").lower()
        if what_want == "report":
            print(resources)
            print(f"the money is ${round(total_profit,2)} ")
            report = True
        else:
            report = False
    if what_want =="off":
            break
    enough_resource = check_resource(coffee_type=what_want,materials=resources,menu=MENU)
    if not enough_resource:
        break
    coin_pennies = float(input("How many pennies?: ")) * 0.01
    coin_nickles = float(input("How many nickles?: ")) * 0.05
    coin_dimes = float(input("How many dimes?: ")) *0.10
    coin_quarters = float(input("How many quarters?: ")) *0.25
    total_coin = coin_pennies + coin_nickles + coin_dimes + coin_quarters
    coin_valid = check_money(coffee_type=what_want,coin=total_coin,menu=MENU)
    if not coin_valid:
        print("Sorry You don't have enough money for the order, Money Refunded")
        break
    return_coin,profit_coin = coin_box(coffee_type=what_want,coin=total_coin,menu=MENU)
    total_profit+=profit_coin
    
    resources = resource_mgmt(coffee_type=what_want,materials=resources,menu=MENU)
    print(f"Here is your {what_want}\nand here is your change ${round(return_coin,2)} ENJOY!!")
        
   
    

from art import logo
print(logo)

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations  = {
     "+":add,
     "-":subtract,
     "*":multiply,
     "/":divide,}
continue_calculation = True
no1 = float(input("Please input number 1:\n"))
while continue_calculation is True:
    no2 = float(input("Please input number 2:\n"))
    for symbol in operations:
        print(symbol)
    operator = input("Please select the operation \n")
    result =operations[operator](no1,no2)
    print(f"Your calculated value is {result}")
    cont = input("would you like to make another calculation?\n")
    if cont == "yes":
        no1=result
    elif cont == "no":
         continue_calculation = False

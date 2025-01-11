print("Welcome to python pizza delivery:")
size = input("What size pizza do you want? S, M or L\n")
add_pepperoni = input("Do you want Pepperoni? Y or N\n")
extra_cheese = input("Do you want extra Cheese? hmmmmmmmmmmmm Y or N\n")

if size=="S":
    bill=15
    if add_pepperoni=="Y":
        bill+=2
elif size=="M":
    bill=20
    if add_pepperoni=="Y":
        bill+=3
elif size == "L":
    bill=25
    if add_pepperoni=="Y":
        bill+=3
else:
    print("Please enter a correct choice:")

if extra_cheese=="Y":
    bill+=1
elif extra_cheese=="N":
    bill=bill
else:
    print("Please use a correct choice.")

print(f"Your bill is {bill}")
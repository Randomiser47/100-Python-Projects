#Conditional Operators

print("WELCOME TO THE ROLLERCOASTER BRRRRRRRRRR!!!!")
height = int(input("Please enter your height: \n"))
if height>=120:
    print("Yay!! your height is appropriate go buy your ticket")
    age = int(input("Please enter your age: \n"))
    if age>=45 and age<=55:
        print("100'%' off for this age group Enjoy")
        bill=0
    elif age>=18:
        bill=12
        print("The ticket costs 12$")
    elif age<12:
        bill=5
        print("The ticket costs 5$")
    else:
        bill=7
        print("The ticket costs 7$")
    want_photo = input("Do you want to take a photo? Press Y for Yes N for No:\n")
    if want_photo== "Y":
        bill=bill+3
        print(f"Your bill is {bill}, Don't forget to smile for the photo")    
    else:
        bill=bill
        print(f"Your bill is {bill} Enjoy!")
else:    
    print("Your height is inadquate!!! NOT ALLOWED~")


print("Welcome to the tip calculator:")
bill = float(input("What was the total bill \n"))
tip = float(input("What Percentage of tip would you like to give 10,12 or 15?\n"))
tip = tip/100  #percentage for tip
tip = tip*bill #Calculation for tip on the bill
final_bill = tip + bill #addition of tip in the bill
people = int(input("How many people will split the bill?: \n"))
bill_per_person= final_bill/people #calculating the split of bill among people
final_bill=(round(bill_per_person,2)) #rounding off
final_bill="{:.2f}".format(bill_per_person) #formatting
print(f"Each person should pay: ${final_bill}")

print("Welcome to the love calculator")
name_1=input("Please Enter the first name: \n")
name_2=input("Please enter the second name: \n")
combined_name = name_1+name_2
lc_name = combined_name.lower()
t=lc_name.count("t")
r=lc_name.count("r")
u=lc_name.count("u")
e=lc_name.count("e")
l=lc_name.count("l")
o=lc_name.count("o")
v=lc_name.count("v")
add_1=t+r+u+e
add_2=l+o+v+e
final_score=str(add_1)+str(add_2)
final_score=int(final_score)
print(f"The love percentage is {final_score}%")

if final_score<10 or final_score>90:
    print(f"Your score is {final_score}, you go together like coke and mentos")
elif 40<final_score<50:
    print(f"your score is {final_score}, you're alright together")
else:
    print(f"your score is {final_score}")    
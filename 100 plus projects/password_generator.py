#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# i = 0
# password_letters = ""
# for i in range (nr_letters):
#     password_letters= password_letters +random.choice(letters)

# i = 0
# password_numbers = ""
# for i in range (nr_letters):
#     password_numbers= password_numbers +random.choice(numbers)

# i = 0
# password_symbols = ""
# for i in range (nr_letters):
#     password_symbols= password_symbols +random.choice(symbols)

# print(password_letters + password_numbers + password_symbols)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P



i = 0
password_letters = ""
for i in range (nr_letters):
    password_letters= password_letters +random.choice(letters)

i = 0
password_numbers = ""
for i in range (nr_numbers):
    password_numbers= password_numbers +random.choice(numbers)

i = 0
password_symbols = ""
for i in range (nr_symbols):
    password_symbols= password_symbols +random.choice(symbols)

password = password_letters + password_numbers + password_symbols
password = list(password)
#password = random.shuffle(password)
random.shuffle(password)

password = ''.join(password)
print(f"The hard mode password is {password}")
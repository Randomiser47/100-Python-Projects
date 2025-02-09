import random

names_string = input("Give me everyones name but separate them with a comma.\n")

names = names_string.split(", ")

x = len(names)

n = random.randint(0, x-1)

print(f"TODAY {names[n]} IS PAYING FOR THE MEALLLL")


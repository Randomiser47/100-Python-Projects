from art import logo
import random
print(logo)
numbers = []
for i in range (1,101):
    numbers.append(i)
selected_number = random.choice(numbers)
easy_or_hard = input("Would you like to play the easy mode or hard mode?").lower()
if easy_or_hard == "easy":
    life = 10
elif easy_or_hard == "hard":
    life = 5
while life >= 0:
        guess = int(input(f"You have {life} lives, make your first guess"))
        if guess >= selected_number:
            print("Too high")
            life -= 1
        elif guess <= selected_number:
            print("Too low")
            life -= 1
        elif guess == selected_number:
            print("You chose the correct number congratulations")
            break
        if life <= 0:
            print(f"You have run out of Lives, Remaining lives {life}")
            print(f"The numbers you had to guess was {selected_number}")
            break 
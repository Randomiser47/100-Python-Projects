from art import logo
import random
replay = True
def number_dealer():
    numbers = [11, 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,10 ,10 ,10]
    randed = random.choice(numbers)
    return randed

def list_addition(list_numbers):
    total = 0
    for num in list_numbers:
        total += num
    return total

def compare_scores(player_score, computer_score):
    if player_score > 21:
        return "You busted! Computer wins. 😢"
    elif computer_score > 21:
        return "Computer busted! You win! 🎉"
    elif player_score > computer_score:
        return "You win! 🎉"
    elif player_score < computer_score:
        return "Computer wins! 😢"
    else:
        return "It's a draw! 😐"


while replay == True:
    print(logo)
    computer_numbers = []
    player_numbers = []
    for i in range (0,2):
        player_numbers.append(number_dealer())
    print(f"Your current numbers: {player_numbers} current score: {list_addition(player_numbers)}")
    computer_numbers.append(number_dealer())
    print(f"The computer's first number: {computer_numbers}")
    recieve_another_number = input("Would you like to recieve another number?").lower()
    if(recieve_another_number == "y"):
        player_numbers.append(number_dealer())  
        print(f"Your score is {list_addition(player_numbers)}")
        print(f"The computer's first number: {computer_numbers}")
    elif recieve_another_number == "n":
        while list_addition(computer_numbers) < 17:
            computer_numbers.append(number_dealer())
            if list_addition(computer_numbers) > 21:
                print("The computer has busted!")
                break
    print(f"The computer's number: {computer_numbers}")
    player_score = list_addition(player_numbers)
    computer_score = list_addition(computer_numbers)

    print(compare_scores(player_score, computer_score))

    play_again = input("Would you like to play the game again?")
    if play_again == "y":
        replay = True
        print("\n"*20)
    elif play_again == "n":
        replay = False
print(computer_numbers)
print(player_numbers)
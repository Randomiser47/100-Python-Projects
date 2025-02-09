import random
import hangman_art #Using the art from hangman_art.py
import hangman_words #Updating the word list to use the 'word_list' from hangman_words.py

lives = 6
print(hangman_art.logo) #Import the logo from hangman_art.py
chosen_word = random.choice(hangman_words.word_list) # running a randomiser to pick a random word from the list

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"****************************You have {lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    display = ""

    for letter in chosen_word:
       if letter == guess:
            display += letter
            correct_letters.append(guess)
       elif letter in correct_letters:
            display += letter
       else:
            display += "_"
    if guess in correct_letters:
        print("You have already pressed this button")
    print("Word to guess: " + display)

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not in the word. You have lost a life. Please try again")

        if lives == 0:
            game_over = True
            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************YOU LOSE**********************")
            print(f"The correct word was {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    print(hangman_art.stages[lives])

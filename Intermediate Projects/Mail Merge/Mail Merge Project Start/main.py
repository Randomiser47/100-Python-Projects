#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp




with open("Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()



with open("Input/Names/invited_names.txt") as name_file:
    i = 0 
    names = name_file.read().splitlines()
    print(names)
    for name in names:
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", "x") as file:
           with open(f"Output/ReadyToSend/letter_for_{name}.txt","a") as final_file:
               final_file.write(letter.replace("[name]",name))






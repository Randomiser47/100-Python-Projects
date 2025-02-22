# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


#PHONETIC PROGRAM

#TODO 1. Create a dictionary in this format:
npa = pandas.read_csv("nato_phonetic_alphabet.csv")

nato = {row["letter"]: row["code"] for index,row in npa.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
entered_word = list(input("Enter a word: ").upper())
phonetic = {char:nato[char] for (char) in entered_word if char in nato}

print(phonetic)


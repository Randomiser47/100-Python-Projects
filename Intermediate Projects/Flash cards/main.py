from tkinter import *
import pandas
import random
#constants
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv('data/words_to_learn.csv')
    
except (FileNotFoundError, ValueError ,IndexError):
    data = pandas.read_csv('data/french_words.csv')

data_dict = data.to_dict(orient='records')
current_card = {}
to_learn_later = []
#------------------------------Data Manipulation-----------------------------------------#
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(title,text="French",fill='black')
    canvas.itemconfig(word,text=current_card["French"],fill='black')
    canvas.itemconfig(canvas_image,image = card_front)
    flip_timer = window.after(3000,func=flip_card)

def right():
    data_dict.remove(current_card)
    next_card()
    pandas.DataFrame(data_dict).to_csv('data/words_to_learn.csv',index=False)
    

# def wrong():
#     to_learn_later.append(current_card)
#     print(to_learn_later)
#     pandas.DataFrame(to_learn_later).to_csv('learn_words.csv')
#     next_card()



def flip_card():
    canvas.itemconfig(title,text="English",fill='white')
    canvas.itemconfig(word,text=current_card['English'],fill='white')
    canvas.itemconfig(canvas_image,image = card_back)

#-----------------------------------UI---------------------------------#
window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0,bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file='images/card_back.png')
canvas_image=canvas.create_image(400,263,image = card_front)
title = canvas.create_text(400,150,text="Title",fill="black",font=('ariel',40,'italic'))
word = canvas.create_text(400,263,text="Word",fill='black',font=('ariel',60,'bold'))
canvas.grid(row=1,column=0,columnspan=2,sticky="EW")

# Cross Button
x_image=PhotoImage(file='images/wrong.png')
x_button = Button(image=x_image,highlightthickness=0,command=next_card)
x_button.grid(row=2,column=0)

# Tick Button
y_image = PhotoImage(file='images/right.png')
y_button = Button(image=y_image,highlightthickness=0,command=right)
y_button.grid(row=2,column=1)

next_card()

window.mainloop()





from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] 
    password_list = []
    pass_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    pass_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    pass_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = pass_letters + pass_numbers + pass_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    pass_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():

    website = website_entry.get()
    eu = eu_entry.get()
    pswd = pass_entry.get()
    new_data = {
        website: {
        "email" : eu,
        "password": pswd,
    }

    }
    if website == "" or pswd == "":
        messagebox.showinfo(title="Bad Input",message="Please try again!")
    else:        
        try:
            with open('file_save.json',mode='r')as file:
                #reading old data
                data = json.load(file)
                #updating data
                data.update(new_data) 
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open('file_save.json',mode= 'w') as file:
                #saving new data
                json.dump(new_data,file,indent=4) 
        else:
            with open('file_save.json',mode= 'w') as file:
                #saving updated data
                json.dump(data,file,indent=4) 
        website_entry.delete(0,END)
        pass_entry.delete(0,END)
# --------------------------- FIND PASSWORD ------------------------------ #
def find_password():
    web_search = website_entry.get()
    try:
        with open('file_save.json', mode = 'r') as file:
            search_data = json.load(file)
            if web_search in search_data:
                messagebox.showinfo(title='Details',message=f"Email: {search_data['email']}\nPassword: {search_data['password']}")
            else:
                messagebox.showinfo(title='Details',message="The data for this email doesn't exist.")
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR!!!",message="THERE IS NO DATA IN YOUR FILE PLEASE TRY AGAIN.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
img_display = canvas.create_image(100,100,image = logo)
canvas.grid(row=0,column=1,sticky="EW")
#------Labels------#
# WEBSITE entry label
website_label = Label(text="Website")
website_label.grid(row=1,column=0)

# Email/username Label
eu_label = Label(text="Email/Username")
eu_label.grid(row=2,column=0)

# Password label
pass_label = Label(text="Password")
pass_label.grid(row=3,column=0)

#----Entry Fields----#
website_entry = Entry(width=21)
website_entry.grid(row=1,column=1,sticky="EW")
website_entry.focus()

eu_entry = Entry(width=35)
eu_entry.grid(row=2,column=1,columnspan=2,sticky="EW")
eu_entry.insert(0,"hassaanalvi47@gmail.com")

pass_entry = Entry(width=21,)
pass_entry.grid(row=3,column=1,sticky="EW")


#-------buttons-------#
pass_button = Button(text="Generate Password",command=gen_pass)
pass_button.grid(row=3,column=2,sticky="EW")
print(pass_button)

add_button = Button(text="Add",width=36,command=save_to_file)
add_button.grid(row=4,column=1,columnspan=2,sticky="EW")

search_button = Button(text="Search",command=find_password)
search_button.grid(row=1,column=2,sticky="EW")

window.mainloop()
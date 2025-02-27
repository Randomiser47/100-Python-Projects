from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
IS_NIGHT = False
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    window.after_cancel(timer)
    work_label.config(text="Timer",fg = PINK)
    canvas.itemconfig(timer_text,text="00:00")
    tick_label.config(text="")
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps

    if reps % 2 == 0 and reps<7: 
        work_sec = count_down(WORK_MIN * 60)
        work_label.config(text = "WORK", fg = GREEN)     
        window.attributes("-topmost",0) 
    elif reps % 2 !=0 and reps <= 5:
        short_break = count_down( SHORT_BREAK_MIN * 60)
        work_label.config(text = "BREAK", fg = PINK)
        window.attributes("-topmost",1)
    elif reps == 7:
        long_break  = count_down(LONG_BREAK_MIN * 60)
        work_label.config(text = "BREAK", fg = RED)
        window.attributes("-topmost",1)
        

    reps +=1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60 
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
       global timer 
       timer = window.after(1000,count_down,count - 1)
    else:
        start_timer()
        tick = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            tick += "✔️"
        tick_label.config(text=tick)
# ---------------------------- Night Mode ------------------------------- # 
def toggle():
    global moon_img
    global tomato_img
    global timer_text
    global img_display
    global IS_NIGHT
    if IS_NIGHT:
        window.config(bg=YELLOW)
        canvas.config(bg = YELLOW)
        work_label.config(bg=YELLOW)
        tick_label.config(bg=YELLOW)
        night_button.config(text="Dark Mode")
        canvas.delete(img_display,timer_text)
        tomato_img = PhotoImage(file="tomato.png")
        img_display =canvas.create_image(100,112,image = tomato_img)
        timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,30,'bold'))
        IS_NIGHT= False
    else:
        window.config(bg='grey')
        canvas.config(bg = "grey")
        work_label.config(bg='grey')
        tick_label.config(bg='grey')
        canvas.delete(img_display,timer_text)
        moon_img = PhotoImage(file="moon-phases.png")
        img_display = canvas.create_image(100,112,image = moon_img)
        timer_text = canvas.create_text(100,120,text="00:00",fill="pink",font=(FONT_NAME,30,'bold'))
        night_button.config(text="Light Mode")
        IS_NIGHT = True


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")

window.config(padx=100,pady=50,bg=YELLOW)
canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
img_display =canvas.create_image(100,112,image = tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,30,'bold'))
canvas.grid(row=1,column=1)

# Label Work
work_label = Label(text="Timer",fg=GREEN,font=(FONT_NAME,30,'bold'),bg=YELLOW)
work_label.grid(row=0,column=1)

# Start button 
start_button = Button(text="Start",bg="#222",fg="#0ff",activebackground="#0ff",highlightthickness=0,activeforeground="#000",relief="raised",command=start_timer)
start_button.grid(row=2,column=0)

# Tick icon
tick_label = Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,'bold'))
tick_label.grid(row=3,column=1)

# Reset button
reset_button = Button(text="Reset",bg="#222",fg="#0ff",activebackground="#0ff",highlightthickness=0,activeforeground="#000",relief="raised",command=reset_timer)
reset_button.grid(row=2,column=2)

# Night Mode button
night_button = Button(text="Dark Mode", bg="#222",fg="#0ff",activebackground="#0ff",highlightthickness=0,activeforeground="#000",relief="raised",command=toggle)
night_button.place(x=300,y=-30)



window.mainloop()


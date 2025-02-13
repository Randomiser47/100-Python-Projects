from turtle import *

class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-10,370)
        self.color('white')
        self.write("Score: 0", align="center",font=('Arial', 20, 'normal'))



    def track_score(self):
        self.clear()
        self.score +=1
        self.write(f"Score: {self.score}", align="center",font=('Arial', 20, 'normal'))


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align="center",font=('Arial', 20, 'normal'))
        
        



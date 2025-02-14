from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,placement):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(placement)
        self.write("0", align="center",font=('OCR A Extended', 40, 'normal'))

    def score_increase(self):
        self.clear()
        self.score +=1
        self.write(f"{self.score}", align="center",font=('OCR A Extended', 40, 'normal'))

from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(-210,260)
        self.write("score: 0", align="center",font=FONT)

    def increase(self):
        self.clear()
        self.score +=1
        self.write(f"score: {self.score}", align="center",font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center",font=FONT)

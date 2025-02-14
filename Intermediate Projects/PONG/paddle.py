from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,placement):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.goto(placement)
        self.setheading(90)

    
    def paddle_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(),new_y)

    def paddle_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(),new_y)

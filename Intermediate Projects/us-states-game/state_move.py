from turtle import Turtle

class State_m(Turtle):
        def __init__(self,state_name,x_coord,y_coord):
            super().__init__()
            self.hideturtle()
            self.penup()
            self.color('black')
            self.goto(x=x_coord,y=y_coord)
            self.write(f"{state_name}")

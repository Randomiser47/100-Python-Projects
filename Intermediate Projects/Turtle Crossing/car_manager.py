from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

Y = [-200,-150,-120,-90,-60,-20,10,40,70,100,130,160,190,220]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.move_delay = random.randint(0, 10)  # Each car gets a random delay
        self.shape('square')
        self.setheading(180)
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=3)
        self.goto(350,random.choice(Y))
        self.move_speed = 0.1

    def move(self): 
        self.forward(MOVE_INCREMENT)

    def increase_speed(self):
        self.move_speed *=0.9

    def game_over(self):
        self.backward(MOVE_INCREMENT)
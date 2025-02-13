from turtle import *


MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITION = [(0, 0), (-20, 0), (-40,0)]
class Snake:
    def __init__(self):
        self.all_turtles = []
        self.increase_turtle = 3
        self.create_snake()
        self.head = self.all_turtles[0]

    def create_snake(self):
      for i in STARTING_POSITION:
          self.add_segment(i)
        
    def add_segment(self,position):
            three_turtles = Turtle(shape='square')
            three_turtles.color('white')
            three_turtles.penup()
            three_turtles.goto(position)
            self.all_turtles.append(three_turtles)
           

    def extend(self):
       self.add_segment(self.all_turtles[-1].position())

    def move(self):
        for turtle_num in range(len(self.all_turtles)-1,0,-1):
            x_pos = self.all_turtles[turtle_num - 1].xcor()
            y_pos = self.all_turtles[turtle_num - 1].ycor()
            self.all_turtles[turtle_num].goto(x_pos,y_pos)
        self.all_turtles[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)  

    def left(self):
        if self.head.heading() !=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT)
        
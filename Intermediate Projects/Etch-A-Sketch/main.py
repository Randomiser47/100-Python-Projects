from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.back(10)

def turn_left():
    tim.left(5)

def turn_right():
    tim.right(5)

def pen_up():
    tim.penup()

def pen_down():
    tim.pendown()

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=turn_left)
screen.onkey(key="d",fun=turn_right)
screen.onkey(key="c",fun=clear)
screen.onkey(key='p',fun=pen_up)
screen.onkey(key='o', fun=pen_down)
screen.exitonclick()
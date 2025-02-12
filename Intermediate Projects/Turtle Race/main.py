from turtle import Turtle,Screen
import random
screen = Screen()
screen.setup(width=1000,height=500)


color_list = ['red','blue','yellow','green','purple','orange']
y = [-150,-100,-50,0,50,100,150]
all_turtle = []
for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_list[i])
    new_turtle.penup()
    new_turtle.goto(x=-490,y=y[i])
    all_turtle.append(new_turtle)
#user input
user_guess = screen.textinput(title="Make Your Guess!", prompt="Which turtle will win the race? Enter a color:")
is_on = True

while is_on:
    for turtle in all_turtle:
        rand_speed = random.randint(0,10)
        turtle.forward(rand_speed)
        
        if turtle.xcor() >= 460:
            winning_color = turtle.pencolor()
            is_on = False
            if winning_color == user_guess:
                print(f"You made the right choice, the turtle {winning_color} has won")
            else:
                print(f"You made the wrong choice, the turtle {winning_color} has won")    





screen.exitonclick()

# #Turtle no 1. TIM
# tim = Turtle(shape="turtle")
# tim.color('red')
# tim.penup()
# tim.goto(x=-490,y=-100)

# #Turtle no 2. JIM
# jim = Turtle(shape="turtle")
# jim.color('blue')
# jim.penup()
# jim.goto(x=-490,y=-50)


# #Turtle no 3. PIM
# pim = Turtle(shape="turtle")
# pim.color('green')
# pim.penup()
# pim.goto(x=-490,y=-0)


# #Turtle no 4. DIM
# dim = Turtle(shape="turtle")
# dim.color('yellow')
# dim.penup()
# dim.goto(x=-490,y=50)

# #Turtle no 5. BIM 
# bim = Turtle(shape="turtle")
# bim.color('orange')
# bim.penup()
# bim.goto(x=-490,y=100)

# #Turtle no 5. SIM 
# sim = Turtle(shape="turtle")
# sim.color('purple')
# sim.penup()
# sim.goto(x=-490,y=150)

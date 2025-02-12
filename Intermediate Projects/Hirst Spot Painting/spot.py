import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
screen.colormode(255)
tim.color("Blue")
tim.penup()
tim.speed(0)
color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]
counter = 0
y = -150
tim.teleport(x=-200,y=-200)
for i in range(100): 
    if counter == 10:
        tim.teleport(x=-200.00,y=y) 
        y +=50  
        counter =0
    random_colors = random.choice(color_list)
    tim.dot(20,random_colors)
    tim.forward(50)
    counter += 1
    

tim.hideturtle()
screen.exitonclick()
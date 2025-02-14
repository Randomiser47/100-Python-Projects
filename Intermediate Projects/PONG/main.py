from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time





#Screen shenanigans
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800,height=600)
screen.tracer(0)

#Mid Wall
wall = Turtle()
wall.goto(0,290)
wall.penup
wall.hideturtle()
wall.color("white")
wall.setheading(270)
for i in range(15):
    wall.pendown()
    wall.forward(20)
    wall.penup()
    wall.forward(20)

#Scorebored
score_p1 = Scoreboard((-200,240))
score_p2 = Scoreboard((200,240))

#Ball
ball = Ball()

#Right Paddle
paddle_r = Paddle((350,0))
screen.onkey(key="Up",fun=paddle_r.paddle_up)
screen.onkey(key="Down",fun=paddle_r.paddle_down)

#Left Paddle
paddle_l = Paddle((-350,0))
screen.onkey(key="w",fun=paddle_l.paddle_up)
screen.onkey(key="s",fun=paddle_l.paddle_down)


screen.listen()
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or  ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #Scorce Track and Ball Reset    
    if ball.xcor() > 380:
        score_p1.score_increase()#this is the score
        ball.reset_ball()
    if ball.xcor() < -380:
        score_p2.score_increase()
        ball.reset_ball()




screen.exitonclick()

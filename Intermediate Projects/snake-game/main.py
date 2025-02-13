from turtle import Screen
import time
from snake import *
from food import *
from scoreboard import *

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detect COllision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.track_score()
        snake.extend()

    #Detect Collision with wall
    if snake.head.xcor() > 470 or snake.head.xcor() <-470 or snake.head.ycor() >400 or snake.head.ycor() < -400:
        game_is_on = False
        score.game_over()

    #Detect COllision with tail
    for segments in snake.all_turtles[1:]:
        if snake.head.distance(segments) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()

# ALTERNATIVE PATH
# length = 3
# tim = Turtle(shape=("square"))
# tim.penup()
# tim.color("white")
# tim.shapesize(stretch_wid=1,stretch_len=length,outline=0)
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random




screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
screen.onkey(fun=player.move_forward,key="w")
cars = []
increase_game_speed = 0.1

def game_speed():
    increase_game_speed *= 0.9


score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(player.game_speed)
    if random.randint(0,10)==1:
        car = CarManager()
        cars.append(car)
    for car in cars:
        car.move()
        if player.distance(car) < 20:
            score.game_over()
            game_is_on =False

        

    if player.ycor() >= 280:
        score.increase()
        player.reset_player()
   

    screen.update()

screen.exitonclick()
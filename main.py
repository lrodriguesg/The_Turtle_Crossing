import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

screen.listen()
screen.onkeypress(player.move, 'Up')
car_manager = CarManager()
score = Scoreboard()



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car.
    for car in car_manager.all_cars:   
        if player.distance(car) < 25:
            game_is_on = False
            score.game_over()


    #Detect when the player go to next level.
    if player.is_at_finish_line():
        score.increse_level()
        car_manager.car_speed_increment()
        player.start_line()






screen.exitonclick()
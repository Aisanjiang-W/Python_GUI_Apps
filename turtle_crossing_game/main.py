import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.crate_car()
    car_manager.car_move()

    # detect collision with the cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    # detect collision with the top wall
    if player.is_at_finish_line():
        score_board.increase_level()
        player.back_to_start_position()
        car_manager.speed_up()

screen.exitonclick()

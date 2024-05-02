import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car = CarManager()
score = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    if player.finish():
        player.go_to_start()
        car.next_level()
        score.level_up()
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            score.game_over()
            game_is_on = False



screen.exitonclick()
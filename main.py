import _tkinter
import time as t
from turtle import Screen
from player import Player
from car_mnger import CarManager
from scoreboard import Scoreboard


def flash_effect():
    """Screen fash animation with delay"""
    for _ in range(3):
        scr.bgpic("assets/bgalt.gif")
        scr.update()
        t.sleep(.1)
        scr.bgpic("assets/bg.gif")
        scr.update()
        t.sleep(.1)


def exit_game():
    global game_is_on
    game_is_on = False
    scr.ontimer(scr.bye, 300)


scr = Screen()
root = Screen()._root
scr.setup(600, 600)
scr.title("Turtle Crossing")
root.iconbitmap("assets/logo.ico")
scr.bgpic("assets/bg.gif")
scr.tracer(0)

player = Player()
car_manager = CarManager()

score = Scoreboard()

scr.listen()
scr.onkeypress(player.move_player_up, "Up")
scr.onkeypress(player.move_player_down, "Down")
scr.onkeypress(exit_game, "Escape")


for _ in range(70):
    car_manager.create_car()
    car_manager.move_cars()

game_is_on = True
while game_is_on:
    scr.update()
    t.sleep(0.1)

    car_manager.create_car()

    # Terminate game in case of unexpected error
    try:
        car_manager.move_cars()
    except _tkinter.TclError:
        exit()

    # Detect player collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            flash_effect()
            if score.hp_left():
                player.goto_starting_pos()
                scr.update()
            else:
                score.game_over_prompt()
                game_is_on = False

    # Level Completion
    if player.at_finish_line():
        score.update_score()
        player.goto_starting_pos()
        car_manager.increase_car_speed()

scr.update()
scr.exitonclick()

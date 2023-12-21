from turtle import Turtle, Screen

STARTING_POS = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 275
STARTING_LINE = -270
SHAPE = Screen()
SHAPE.addshape("assets/player.gif")


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("assets/player.gif")
        self.penup()
        self.goto_starting_pos()
        self.setheading(90)

    def move_player_up(self):
        if self.ycor() < FINISH_LINE:
            self.forward(MOVE_DISTANCE)

    def move_player_down(self):
        if self.ycor() > STARTING_LINE:
            self.backward(MOVE_DISTANCE)

    def at_finish_line(self):
        if self.ycor() >= FINISH_LINE:
            return True
        return False

    def goto_starting_pos(self):
        self.goto(STARTING_POS)

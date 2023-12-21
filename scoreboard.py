from turtle import Turtle, Screen

FONT = ("unispace", 12, "bold")
HP_POS = [(0, 1000), (220, 270), (245, 270), (270, 270)]
SHAPE = Screen()
SHAPE.addshape("assets/heart.gif")
SHAPE.addshape("assets/empty_heart.gif")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("highscore.txt") as datafile:
            self.highscore = int(datafile.read())
        self.hp = []
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_score()
        self.create_hp()

    def update_score(self):
        self.clear()
        self.level += 1
        self.goto(-285, 257)
        self.write(f"Level:{self.level}", align="left", font=FONT)
        if self.level > self.highscore:
            with open("highscore.txt", mode="w") as datafile:
                datafile.write(str(self.level))
        self.goto(-285, 278)
        self.write(f"High Score:{self.highscore}", align="left", font=FONT)

    def game_over_prompt(self):
        self.goto(0, -23)
        self.write("GAME OVER", align="center", font=("unispace", 26, "bold"))

    def create_hp(self):
        for pos in HP_POS:
            heart = Turtle("assets/heart.gif")
            heart.penup()
            heart.goto(pos)
            self.hp.append(heart)

    def hp_left(self):
        self.hp[-1].shape("assets/empty_heart.gif")
        self.hp.remove(self.hp[-1])
        if len(self.hp) > 1:
            return True
        return False

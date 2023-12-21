from turtle import Turtle, Screen
import random as r

CARS = ["assets/left cars/blackcar.gif", "assets/left cars/bluecar.gif", "assets/left cars/graycar.gif",
        "assets/left cars/pinkcar.gif", "assets/left cars/purplecar.gif", "assets/left cars/redcar.gif",
        "assets/left cars/whitecar.gif", "assets/left cars/bluesport.gif", "assets/left cars/redsport.gif",
        "assets/left cars/yellowsport.gif", "assets/left cars/greensport.gif", "assets/left cars/purpletruck.gif",
        "assets/left cars/redtruck.gif", "assets/left cars/greentruck.gif", "assets/left cars/graytruck.gif",
        "assets/left cars/orangesuv.gif", "assets/left cars/greensuv.gif",
        "assets/right cars/blackcar.gif", "assets/right cars/bluecar.gif", "assets/right cars/graycar.gif",
        "assets/right cars/pinkcar.gif", "assets/right cars/purplecar.gif", "assets/right cars/redcar.gif",
        "assets/right cars/whitecar.gif", "assets/right cars/bluesport.gif", "assets/right cars/redsport.gif",
        "assets/right cars/yellowsport.gif", "assets/right cars/greensport.gif", "assets/right cars/purpletruck.gif",
        "assets/right cars/redtruck.gif", "assets/right cars/greentruck.gif", "assets/right cars/graytruck.gif",
        "assets/right cars/orangesuv.gif", "assets/right cars/greensuv.gif"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2
SHAPE = Screen()
for shape in CARS:
    SHAPE.addshape(shape)


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_flag = 0
        self.car_frequency = 14
        self.rand_y_left = [238, 158, 78, -44, -124, -204]
        self.rand_y_right = [206, 126, 46, -76, -156, -236]

    def create_car(self):
        for repeat_car in self.all_cars:
            if repeat_car.xcor() < -320 or repeat_car.xcor() > 320:
                self.all_cars.remove(repeat_car)
                repeat_car.clear()
                repeat_car.ht()
        if self.car_flag > self.car_frequency:
            self.left_cars()
            self.right_cars()
            self.left_cars()
            self.right_cars()
            self.car_flag = 0
        self.car_flag += 1

    def left_cars(self):
        car = Turtle()
        car.shape(r.choice(CARS[:17]))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.goto(-300, r.choice(self.rand_y_left))
        self.all_cars.append(car)

    def right_cars(self):
        car = Turtle()
        car.shape(r.choice(CARS[17:]))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.setheading(180)
        car.goto(300, r.choice(self.rand_y_right))
        self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def increase_car_speed(self):
        if self.car_frequency > 2:
            self.car_speed += MOVE_INCREMENT
            self.car_frequency -= 2

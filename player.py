from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.pu()
        self.refresh()

    def move_turtle(self):
        self.forward(MOVE_DISTANCE)

    def refresh(self):
        self.setheading(90)
        self.goto(STARTING_POSITION)




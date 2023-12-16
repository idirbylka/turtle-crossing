from turtle import Turtle, Screen
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.starting_level = 1
        self.pu()
        self.goto(-200, 260)
        self.ht()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.starting_level}", align="center", font=FONT)

    def score_update(self):
        self.clear()
        self.starting_level += 1
        self.update_scoreboard()


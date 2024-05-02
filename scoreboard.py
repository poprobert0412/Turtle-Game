from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.shape(None)
        self.penup()
        self.hideturtle()
        self.goto(-210, 260)
        self.write(f"Level: {self.level}", False, align="center", font=FONT)


    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", False, align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align="center", font=("Courier", 30, "bold"))
        self.goto(0, -40)
        self.write(f"Level: {self.level}", False, align="center", font=("Courier", 30, "bold"))

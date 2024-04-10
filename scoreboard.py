from turtle import Turtle

X_POS = 0
Y_POS = 270

ALIGNMENT = 'center'
FONT = ('Arial', 15, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=X_POS, y=Y_POS)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Your Score: {self.score}  High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as hscore:
                hscore.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()
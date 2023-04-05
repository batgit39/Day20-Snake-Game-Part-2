from turtle import Turtle, Screen


FONT = ('Arial', 24, 'normal')
ALIGNMENT = "center"

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.total_score = 0
        self.penup()
        self.goto(0,260)
        self.color("white")
        self.hideturtle()
        self.show_scoreboard()

    def show_scoreboard(self):
        self.write(f"Score = {self.total_score}", True,  align = ALIGNMENT, font = FONT)

    def score_increased(self):
        self.total_score += 1
        self.clear()
        self.goto(0,260)
        self.show_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", True,  align = ALIGNMENT, font = FONT)


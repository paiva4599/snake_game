from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 16, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(x=0, y=270)
        self.pendown()
        self.score_writing(self.score)

    def score_writing(self, score):
        self.write(arg=f"Score: {score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_writing(self.score)

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.pendown()
        self.write(arg=f"Game Over", align=ALIGNMENT, font=FONT)
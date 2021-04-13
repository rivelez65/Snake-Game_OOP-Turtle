from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 22, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode='r') as file:
            self.high_score = int(file.read())
        self.color('blue')
        self.hideturtle()
        self.penup()
        self.goto(-100, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"SCORE: {self.score}       HIGH SCORE:{self.high_score} ", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.score))
            self.score = 0
            self.update_score()

    def draw_walls(self):
        t = Turtle()
        t.penup()
        t.color("white")
        t.pensize(2)
        t.goto(280, 0)
        t.pendown()
        t.goto(280, 290)
        t.goto(-290, 290)
        t.goto(-290, -280)
        t.goto(280, -280)
        t.goto(280, 290)
        t.hideturtle()

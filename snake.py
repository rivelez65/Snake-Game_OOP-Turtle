from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_sections = []
        self.snake_body()
        self.head = self.snake_sections[0]

    def snake_body(self):
        for square in STARTING_POSITIONS:
            t = Turtle()
            t.color('black')
            t.speed('fastest')
            t.penup()
            t.shape('square')
            t.goto(square)
            t.color('white')
            t.seth(0)
            self.snake_sections.append(t)

    def extend(self):
        new = Turtle()
        new.penup()
        new.shape('square')
        new.color('white')
        new.goto(self.snake_sections[-1].position())
        self.snake_sections.append(new)

    def move(self):
        for seg in range(len(self.snake_sections) - 1, 0, -1):
            new_x = self.snake_sections[seg - 1].xcor()
            new_y = self.snake_sections[seg - 1].ycor()
            self.snake_sections[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for section in self.snake_sections:
            section.goto(1000, 1000)
        self.snake_sections.clear()
        self.snake_body()
        self.head = self.snake_sections[0]





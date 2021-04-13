from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score_board import Score

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')
game_is_on = True

# SET SCREEN PARAMETES
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("SNAKE GAME!")
screen.tracer(0)

screen.listen()
snake = Snake()
food = Food()
scoreboard = Score()
speed = 0.25
scoreboard.draw_walls()

screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Right', fun=snake.right)
screen.onkey(key='Left', fun=snake.left)


# RESET SCREEN PARAMETERS TO DEFAULT
def initiate():
    global snake, food, scoreboard, speed
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title("SNAKE GAME!")
    screen.tracer(2)

    screen.listen()
    snake = Snake()
    food = Food()
    scoreboard = Score()
    speed = 0.25

    screen.onkey(key='Up', fun=snake.up)
    screen.onkey(key='Down', fun=snake.down)
    screen.onkey(key='Right', fun=snake.right)
    screen.onkey(key='Left', fun=snake.left)


# GAME LOGIC
while game_is_on:

    screen.update()
    time.sleep(speed)
    snake.move()

    if snake.head.distance(food) < 19:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        speed /= 1.2

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        speed = 0.25

    for square in snake.snake_sections[1:]:
        if snake.head.distance(square) < 10:
            scoreboard.reset()
            snake.reset()
            speed = 0.25

screen.exitonclick()
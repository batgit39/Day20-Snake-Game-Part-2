from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

x = 0.1
game = True
while game:
    screen.update()
    time.sleep(x)
    snake.move()

    # detectiong food collision
    if snake.head.distance(food) < 15:
        x *= 0.9
        food.find_new_location()
        snake.extend_snake()
        score.score_increased()

    # detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        x = 0.1
        game = False
        score.game_over()

    # detecting tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            x = 0.1
            game = False
            score.game_over()

screen.exitonclick()

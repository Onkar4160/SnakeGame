import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game.")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision of snake to food
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() <-290 or snake.head.ycor() >290 or snake.head.ycor() <-290 :
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segment:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()
    # if head collides with any segment in the tail:


screen.exitonclick()
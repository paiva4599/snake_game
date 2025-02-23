from turtle import Screen
from snake_class import Snake
from food_class import Food
from scoreboard_class import ScoreBoard
import time

game_is_on = True

display = Screen()
display.setup(width=600, height=600)
display.tracer(0)
display.bgcolor("black")
display.title("Snake Game")

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
score = 0

display.listen()
display.onkey(snake.up,"Up")
display.onkey(snake.left, "Left")
display.onkey(snake.down, "Down")
display.onkey(snake.right, "Right")

while game_is_on:
    display.update()
    time.sleep(0.1)

    snake.move_forward()

    #Colision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    #Colision with wall
    if (snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280
            or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280):
        game_is_on = False
        scoreboard.game_over()

    #Colision with tail
    for segments in snake.segments[1:-1]:
        if snake.segments[0].distance(segments) < 10:
            game_is_on = False
            scoreboard.game_over()

display.exitonclick()

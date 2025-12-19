from turtle import Screen
from score_board import Scoreboard
from food import Food
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
snake = Snake()
scoreboard = Scoreboard()
food = Food()
game_is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
food_counter = 0
delay = 0.1

while game_is_on:
    screen.update()
    time.sleep(delay)
    snake.move()

    # Normal food collision
    if not food.special_active and snake.head.distance(food.normal) < 15:
        food_counter += 1
        snake.extend()
        scoreboard.increase_score()

        if food_counter % 5 == 0:
            food.show_special()
        else:
            food.refresh_normal()

    # Special food collision
    elif food.special_active and snake.head.distance(food.special) < 15:
        snake.extend()
        scoreboard.score += 10
        scoreboard.update_scoreboard()
        food.refresh_normal()

    # Wall collision
    if (
        snake.head.xcor() > 285 or
        snake.head.xcor() < -285 or
        snake.head.ycor() > 285 or
        snake.head.ycor() < -285
    ):
        game_is_on = False
        scoreboard.game_over()

    # Tail collision
    for segment in snake.snakes[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
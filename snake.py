from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        body = Turtle("square")
        body.color("white")
        body.penup()
        body.goto(position)
        self.snakes.append(body)

    def move(self):
        # Move body segments from tail to head
        for idx in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[idx - 1].xcor()
            new_y = self.snakes[idx - 1].ycor()
            self.snakes[idx].goto(new_x, new_y)
        # Move the head forward
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        self.add_segment(self.snakes[-1].position())
    # Direction methods
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

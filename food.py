from turtle import Turtle
import random

class Food:
    def __init__(self):
        # Normal food
        self.normal = Turtle("circle")
        self.normal.penup()
        self.normal.shapesize(0.5,0.5)
        self.normal.color("white")
        self.normal.speed("fastest")
        self.refresh_normal()

        # Special food (hidden at start)
        self.special = Turtle("triangle")
        self.special.penup()
        self.special.shapesize(1,1)
        self.special.color("red")
        self.special.speed("fastest")
        self.special.hideturtle()

        self.special_active = False

    def refresh_normal(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.normal.goto(x, y)
        self.normal.showturtle()
        self.special_active = False

    def show_special(self):
        self.normal.hideturtle()  # hide normal food temporarily
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.special.goto(x, y)
        self.special.showturtle()
        self.special_active = True

        # Hide special and return to normal after 4 seconds
        self.special.getscreen().ontimer(self.refresh_normal, 4000)

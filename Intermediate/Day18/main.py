from turtle import Screen
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

tim.shape("circle")
tim.pensize(15)
tim.speed("fastest")
directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_c = (r, g, b)
    return random_c


for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()

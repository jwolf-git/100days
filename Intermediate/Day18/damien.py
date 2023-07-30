import colorgram
from turtle import Screen
import turtle as turtle_module
import random

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

rgb_colors = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71)]

tim = turtle_module.Turtle()
tim.penup()
turtle_module.colormode(255)
tim.speed("fastest")
ycoord = -200
tim.setpos(-200, ycoord)
num_dots = 100
tim.hideturtle()


for point in range(1, num_dots+1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)
    if point % 10 == 0:
        ycoord += 50
        tim.setpos(-200, ycoord)


screen = turtle_module.Screen()
screen.exitonclick()

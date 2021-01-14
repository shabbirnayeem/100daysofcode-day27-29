import colorgram
from turtle import Turtle, Screen
import random
import turtle
# generating rgb colors from painting
# colors = colorgram.extract("image.jpg", 540)
#
# rgb_color = []
# for c in colors:
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b
#     rgb_color.append((r, g, b))
#
# print(rgb_color)

rgb_color_list = [(247, 244, 235), (250, 240, 247), (239, 250, 245), (233, 240, 247), (134, 167, 191), (211, 156, 106), (197, 143, 166), (29, 110, 168), (234, 214, 86), (127, 74, 92), (187, 178, 19), (26, 136, 66), (55, 18, 26), (142, 20, 40), (38, 175, 113), (225, 170, 196), (116, 188, 144), (231, 77, 50), (172, 70, 46), (238, 218, 5), (37, 17, 16), (186, 91, 110), (9, 102, 52), (34, 167, 189), (20, 20, 28), (183, 185, 213), (234, 171, 159), (154, 215, 172), (142, 20, 16), (89, 124, 182), (160, 206, 213), (13, 91, 97), (7, 73, 26), (52, 61, 102)]

ron = Turtle()
screen = Screen()
turtle.colormode(255)

# My Code

ron.hideturtle()
ron.penup()
ron.speed(0)
screen.title("Welcome to Hirst million dollars patining.")

y = 50
for _ in range(10):

    for _ in range(10):
        #ron.color(random.choice(rgb_color_list))
        ron.dot(20, random.choice(rgb_color_list))
        ron.forward(50)

    ron.setposition(0, y)
    y += 50

#
# # Teachers Code
#
# ron.hideturtle()
# ron.penup()
# ron.speed(0)
# #ron.penup()
# # set heading to south (set turtle to  turn left)
# ron.setheading(180)
# ron.forward(600)
# # set heading to south (set turtle to  turn down)
# ron.setheading(270)
# ron.forward(300)
# # set heading to south (set turtle to turn right)
# ron.setheading(0)
# number_of_dots = 101
#
# for dot_count in range(1, number_of_dots):
#     ron.dot(20, random.choice(rgb_color_list))
#     ron.forward(50)
#
#     # make the dot count to 10,20,30,....
#     if dot_count % 10 == 0:
#         # set turtle to turn left
#         ron.setheading(90)
#         # go up 50
#         ron.forward(50)
#         # turn right
#         ron.setheading(180)
#         # move back to the starting point
#         ron.forward(500)
#         # turn right
#         ron.setheading(0)



















#print(screen.screensize())
# print(screen.window_width())
# print(screen.window_height())





screen.exitonclick()

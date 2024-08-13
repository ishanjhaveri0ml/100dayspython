###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.g
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
#
# color_list = [(245, 243, 243), (247, 242, 242), (240, 245, 245), (202, 164, 164), (238, 240, 240), (150, 75, 75), (223, 201, 201), (52, 93, 93), (172, 154, 154), (140, 30, 30), (133, 163, 163), (198, 91, 91), (46, 122, 122), (72, 43, 43), (145, 178, 178), (13, 99, 99), (233, 175, 175), (161, 142, 142), (105, 74, 74), (55, 46, 46), (183, 205, 205), (36, 60, 60), (18, 86, 86), (81, 148, 148), (148, 17, 17), (14, 70, 70), (30, 68, 68), (107, 127, 127), (174, 94, 94), (176, 192, 192)]

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)









screen = turtle_module.Screen()
screen.exitonclick()

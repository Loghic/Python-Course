import colorgram
import os

ROWS = 10
COLS = 10
NUM_OF_COLORS = ROWS * COLS

path = os.getcwd()
colors = colorgram.extract(f"{path}/hirst_painting/image.jpg", NUM_OF_COLORS)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    new_color = (r,g,b)
    rgb_colors.append(new_color)


from turtle import Turtle, Screen, colormode

tim = Turtle()
tim.shape("turtle")
tim.color("blue")
tim.speed("fastest")
gap = 50
dot_size = 20
WHITE = (255,255,255)
screen = Screen()
screen.colormode(255)
tim.penup()

def draw_row(start_color):
    for col in range(COLS):
        tim.pendown()
        tim.color(rgb_colors[(start_color+col) % len(rgb_colors)])
        tim.dot(dot_size)
        tim.color(WHITE)
        tim.penup()
        tim.forward(gap)
        start_color += 1
    
    for _ in range(COLS):
        tim.backward(gap)

    return start_color


start_color_pos = 0
tim.backward(200)
tim.left(90)
tim.backward(200)

for _ in range(ROWS):
    tim.forward(gap)
    tim.right(90)
    start_color_pos = draw_row(start_color_pos)
    tim.left(90)

screen.exitonclick()
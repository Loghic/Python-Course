from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
tim.shape("turtle")
tim.color("Blue")

colours = ["Black", "Red", "Lime", "Blue", "Cyan", "Magenta", "Silver", "Maroon", "Olive", "Green",
           "Purple", "Teal", "Navy"]

def draw_square(side_len):
    for _ in range(4):
        tim.forward(side_len)
        tim.right(90)

def dashed_line(len):
    for i in range(0,len, len//10):
        if i % 20 == 0:
            tim.pendown()
        else:
            tim.penup()
        tim.forward(10)
    tim.pendown()

def draw_dashed_square(side_len):
    for _ in range(4):
        dashed_line(side_len)
        tim.right(90)


def draw_n_tagon(n_angles, side_len):
    angle = 360 // n_angles
    for _ in range(n_angles):
        tim.pencolor(random.choice(colours))
        tim.forward(side_len)
        tim.left(angle)


# draw_square(100)
# dashed_line(100)
# draw_dashed_square(100)

# draw_n_tagon(5,100)

# for shape_side_n in range(3,11):
#     draw_n_tagon(shape_side_n, 100)

direction = [0, 90, 180, 270]

colormode(255) # set colormode


def random_color():
    """Returns a tuple consisting of Red Green and Blue that are randomly selected"""
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_random_walk():
    tim.speed("fastest")
    tim.pensize(5)
    for _ in range(200):
        tim.pencolor(random_color())
        tim.setheading(random.choice(direction))
        tim.fd(20)

    tim.pensize(1)


# draw_random_walk()

def spirograph(nmr_of_circles):
    angle = 360/nmr_of_circles
    tim.speed(0)
    for _ in range(nmr_of_circles):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.left(angle)
    tim.speed(1)


# spirograph(120)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color


tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

# to Show screen
screen = Screen()
screen.exitonclick()

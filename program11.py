import turtle
import random

screen = turtle.Screen()
screen.title("Christmas Tree - Turtle Graphics")
screen.bgcolor("midnight blue")
screen.setup(width=800, height=700)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

def draw_triangle(x, y, size, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()

    for _ in range(3):
        pen.forward(size)
        pen.left(120)

    pen.end_fill()

def draw_rectangle(x, y, width, height, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()

    for side in [width, height, width, height]:
        pen.forward(side)
        pen.left(90)

    pen.end_fill()

def draw_star(x, y, size):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.pendown()
    pen.color("gold")
    pen.begin_fill()

    for _ in range(5):
        pen.forward(size)
        pen.right(144)

    pen.end_fill()

def draw_ornaments():
    colors = ["red", "yellow", "cyan", "magenta", "orange"]

    for _ in range(35):
        x = random.randint(-110, 110)
        y = random.randint(-150, 100)

        if y < -150 + abs(x) * 0.9:
            continue

        pen.penup()
        pen.goto(x, y)
        pen.dot(random.randint(6, 12), random.choice(colors))

def draw_tree():
    # Draw three green triangular layers
    draw_triangle(-150, -100, 300, "forest green")
    draw_triangle(-125, -20, 250, "green")
    draw_triangle(-100, 50, 200, "lime green")

    # Draw the tree trunk
    draw_rectangle(-25, -180, 50, 80, "saddlebrown")

    # Add the star and decorations
    draw_star(-15, 140, 30)
    draw_ornaments()

    # Display a greeting
    pen.penup()
    pen.goto(0, -250)
    pen.color("white")
    pen.write("Merry Christmas!", align="center",
              font=("Arial", 24, "bold"))

draw_tree()

screen.mainloop()

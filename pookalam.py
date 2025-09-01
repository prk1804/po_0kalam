import turtle
import math

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Pookalam Blueprint")

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# Function to draw a circle
def draw_circle(radius):
    t.penup()
    t.sety(-radius)  # move turtle to bottom
    t.pendown()
    t.circle(radius)

# Function to draw petals
def draw_petals(radius, n_petals, petal_length):
    angle = 360 / n_petals
    for _ in range(n_petals):
        t.penup()
        t.goto(0,0)
        t.forward(radius)
        t.pendown()
        t.setheading(t.towards(0,0))
        t.left(90)
        
        # Petal shape
        t.circle(petal_length, 60)
        t.left(120)
        t.circle(petal_length, 60)
        t.left(180 - angle)

# Draw blueprint
t.color("brown")  # outline color

# Inner circle
draw_circle(50)

# First layer of petals
draw_petals(50, 8, 50)

# Second circle
draw_circle(120)

# Second layer of petals
draw_petals(120, 12, 80)

# Third circle
draw_circle(200)

# Third layer of petals
draw_petals(200, 16, 100)

t.hideturtle()
screen.mainloop()

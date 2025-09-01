import turtle
import math

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Pookalam Blueprint")

t = turtle.Turtle()
t.speed(10)
t.pensize(2)

# Function to draw a circle at center
def draw_circle(radius):
    t.penup()
    t.goto(0, -radius)   # Move to bottom of circle
    t.pendown()
    t.circle(radius)

# Function to draw semicircles fitted around the central circle
def draw_semicircles(center_radius, n_petals, petal_radius):
    angle = 360 / n_petals
    for i in range(n_petals):
        theta = math.radians(i * angle)
        # center of semicircle lies on central circle
        x = center_radius * math.cos(theta)
        y = center_radius * math.sin(theta)

        t.penup()
        t.goto(x, y)
        t.setheading(i * angle - 90)  # orient mouth inward
        t.forward(petal_radius)       # move to edge
        t.pendown()
        t.circle(petal_radius, 180)   # semicircle outward

# -------------------
# Draw Pookalam Base
# -------------------

# Central circle
inner_radius = 50
draw_circle(inner_radius)

# Semicircles around it
petal_radius = 30
draw_semicircles(inner_radius, 12, petal_radius)

# Correct outer circle (envelops everything)
outer_radius = inner_radius + 2 * petal_radius
draw_circle(outer_radius)

t.hideturtle()
screen.mainloop()
import turtle
import math

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Pookalam Blueprint")

t = turtle.Turtle()
t.speed(10)
t.pensize(2)

# Function to draw a circle at center
def draw_circle(radius):
    t.penup()
    t.goto(0, -radius)   # Move to bottom of circle
    t.pendown()
    t.circle(radius)

# Function to draw semicircles fitted around the central circle
def draw_semicircles(center_radius, n_petals, petal_radius):
    angle = 360 / n_petals
    for i in range(n_petals):
        theta = math.radians(i * angle)
        # center of semicircle lies on central circle
        x = center_radius * math.cos(theta)
        y = center_radius * math.sin(theta)

        t.penup()
        t.goto(x, y)
        t.setheading(i * angle - 90)  # orient mouth inward
        t.forward(petal_radius)       # move to edge
        t.pendown()
        t.circle(petal_radius, 180)   # semicircle outward

# -------------------
# Draw Pookalam Base
# -------------------

# Central circle
inner_radius = 50
draw_circle(inner_radius)

# Semicircles around it
petal_radius = 30
draw_semicircles(inner_radius, 12, petal_radius)

# Correct outer circle (envelops everything)
outer_radius = inner_radius + 2 * petal_radius
draw_circle(outer_radius)

t.hideturtle()
screen.mainloop()

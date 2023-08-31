import turtle

# Create turtle object
t = turtle.Turtle()


# Set turtle speed
t.speed(0)
t.shape("turtle")

# Set up colors
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# Draw rainbow
for i in range(300):
    t.pencolor(colors[i%6])
    t.width(i/100 + 1)
    t.forward(i)
    t.left(59)

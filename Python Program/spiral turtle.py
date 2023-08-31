import turtle

# Create a turtle object
t = turtle.Turtle()
t.shape("turtle")

# Set the speed of the turtle
t.speed(0)

# Set the starting angle
angle = 0

# Draw the spiral
for i in range(200):
    t.forward(i)
    t.right(angle)
    angle += 1

# Exit the turtle window when clicked
turtle.exitonclick()

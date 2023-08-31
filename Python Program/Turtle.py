import turtle

# set up the turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# draw the apple logo
t.penup()
t.goto(0, -150)
t.pendown()
t.color("black", "gray")
t.begin_fill()
t.circle(150)
t.end_fill()

t.penup()
t.goto(-50, 50)
t.pendown()
t.color("white")
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()

t.penup()
t.goto(50, 50)
t.pendown()
t.color("white")
t.begin_fill()
for i in range(3):
    t.forward(100)
    t.right(120)
t.end_fill()

# exit on click
turtle.exitonclick()

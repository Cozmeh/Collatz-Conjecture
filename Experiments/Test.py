import turtle , random
import CollatzChecker as cc
collatz = cc.CollatzChecker()
t = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor("black")
width = 800
height = 600
screen.setup(width=width, height=height)

startX = -width / 2
startY = -height / 2
turtlesize = 0.5
lineColor = "white"
Even_Turn = 10
Odd_Turn = 20
forward = 5
drawDirection = 90

Number = 1000


# Function to check if a number is even or odd
def isEven(num):
    return num % 2 == 0

# Function to draw the collatz sequence
for num in range(2,Number):
    print("Current Number: ", num)

    r = random.randrange(0, 255) / 255
    lineColor = (r,r,r)

    t.goto(startX, startY)
    t.setheading(drawDirection)
    t.turtlesize(turtlesize)
    t.hideturtle()
    t.color(lineColor)
    t.width(2)
    t.pendown()
    turtle.tracer(0, 0)

    steps = collatz.sequence_list(num)[::-1]
    for step in steps:
        if isEven(step):
            t.right(Even_Turn)
            t.forward(forward)
        else:
            t.left(Odd_Turn)
            t.forward(forward)

    t.penup()

turtle.done()
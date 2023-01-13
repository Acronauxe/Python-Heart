from turtle import *

t = Turtle()
t.speed(5)

# Red Heart

t.penup()
t.goto(0, -200)
t.pendown()

t.pencolor("red")
t.begin_fill()
t.fillcolor("red")

t.left(50)
t.forward(266)
t.circle(100, 200)
t.right(140)
t.circle(100, 200)
t.forward(266)
t.left(50)

t.end_fill()

done()

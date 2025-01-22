#this piece draws the first circle of my heart 
import turtle
turtle.Screen().bgcolor("light blue")
t = turtle.Turtle()
t.begin_fill()

t.goto(100, 0)
t.color("pink")

for i in range(70):
    t.forward(5)
    t.left(5)

#This makes the second circle in the heart

c = turtle.Turtle()
c.begin_fill()
c.goto(10, 0)
c.color("pink")

for i in range(70):
    c.forward(5)
    c.left(5)


#this makes the cone of the heart finishing it!
p = turtle.Turtle()
p.begin_fill()
p.goto(70, -100)
p.color("pink")

for i in range(3):
    p.goto(162, 55)
t.end_fill()
c.end_fill()
p.end_fill()


turtle.exitonclick()
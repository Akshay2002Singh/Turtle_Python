import turtle
t = turtle.Turtle()

turtle.title("Audi")
turtle.bgcolor("black")
t.pencolor("red")
t.speed(0)
t.pensize(3)
t.penup()
t.goto(-120,40)
t.pendown()

c = t.clone()
c.penup()
c.goto(-120,-220)
c.pendown()
for i in range(4):
    t.circle(100)
    t.penup()
    t.forward(80)
    t.pendown()
    c.circle(100)
    c.penup()
    c.forward(80)
    c.pendown()
t.hideturtle()
c.hideturtle()
turtle.mainloop()
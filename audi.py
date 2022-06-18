import turtle
t = turtle.Turtle()

turtle.title("Audi")
turtle.bgcolor("black")
t.pencolor("red")
t.speed(0)
t.pensize(3)
t.penup()
t.goto(-120,0)
t.pendown()
for i in range(4):
    t.circle(100)
    t.penup()
    t.forward(80)
    t.pendown()
turtle.mainloop()
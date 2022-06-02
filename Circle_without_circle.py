import turtle

def curve(n):
    for i in range(n):
        t.forward(1)
        t.right(1)

t= turtle.Turtle()
t.pensize(3)
t.speed(0)
turtle.bgcolor('red')
t.pencolor('black')
t.fillcolor("black")
t.begin_fill()
curve(360)
t.end_fill()
t.hideturtle()
turtle.mainloop()  
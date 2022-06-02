import turtle

def curve(n):
    for i in range(n):
        t.forward(2)
        t.right(3)

t= turtle.Turtle()
t.pensize(3)
t.speed(1)
turtle.bgcolor('red')
t.pencolor('black')
t.fillcolor("black")
t.begin_fill()
t.left(130)
t.forward(100)
curve(75)
t.left(189)
curve(73)
t.right(5)
t.forward(108)
t.end_fill()
t.hideturtle()
turtle.mainloop()  
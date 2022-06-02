import turtle
t= turtle.Turtle()
turtle.bgcolor('black')
t.pencolor('red')
t.speed(0)
for i in range(34):
    t.circle(100)
    t.left(12)
turtle.hideturtle()
turtle.mainloop()  
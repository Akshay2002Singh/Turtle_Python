import turtle
t= turtle.Turtle()
turtle.bgcolor('black')
t.pencolor('red')
t.penup()
t.goto(0,-200)
t.pendown()
t.pensize(1)
t.speed(0)
t.shape("turtle")
for i in range(10,240,10):
	t.circle(i)
turtle.hideturtle()
turtle.mainloop()  
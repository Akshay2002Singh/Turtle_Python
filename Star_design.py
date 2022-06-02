import turtle
t= turtle.Turtle()
turtle.bgcolor('black')
t.pencolor('red')
t.penup()
t.goto(-50,-50)
t.bk(200)
t.left(9)
t.pendown()
t.pensize(1)
t.speed(0)
for i in range(130):
	t.fd(400-i)
	t.left(150)
	
turtle.hideturtle()
turtle.mainloop()

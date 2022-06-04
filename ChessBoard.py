import turtle
def square(n):
    t.forward(n)
    t.left(90)
    t.forward(n)
    t.left(90)
    t.forward(n)
    t.left(90)
    t.forward(n)
    t.left(90)
t = turtle.Turtle()
turtle.bgcolor("green")
turtle.title("Python Chess Board")
t.shape("turtle")
t.speed('fastest')
t.pensize(0)
wid = 40
t.penup()
t.goto(-150,150)
t.pendown()
for i in range(8):
    # print(i)
    for j in range(8):
        # print(j)
        if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
            t.fillcolor("white")
        else:
            t.fillcolor("black")
        t.begin_fill()
        square(wid)
        t.end_fill()
        t.forward(wid)
    if i!=7:
        t.backward(wid*8)
        t.right(90)
        t.forward(wid)
        t.setheading(0)

t.hideturtle()

turtle.mainloop()

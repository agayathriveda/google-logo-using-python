import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(10)

t.color("#4285F4", "#4285F4")
t.pensize(3)
t.forward(120)
t.right(90)
t.circle(-150, 50)
t.color("#34A853")
t.circle(-150, 100)
t.color("#FBBC05")
t.circle(-150, 60)
t.color("#EA4335", "#EA4335")
t.begin_fill()
t.circle(-150, 100)
t.right(90)
t.forward(50)
t.right(90)
t.circle(100, 100)
t.right(90)
t.forward(50)
t.end_fill()
t.begin_fill()
t.color("#FBBC05", "#FBBC05")
t.right(180)
t.forward(50)
t.right(90)
t.circle(100, 60)
t.right(90)
t.forward(50)
t.right(90)
t.circle(-150, 60)
t.end_fill()
t.right(90)
t.forward(50)  # -----#
t.right(90)
t.circle(100, 60)
t.color("#34A853", "#34A853")
t.begin_fill()
t.circle(100, 100)
t.right(90)
t.forward(50)
t.right(90)
t.circle(-150, 100)
t.right(90)
t.forward(50)
t.end_fill()
t.right(90)
t.circle(100, 100)
t.color("#4285F4", "#4285F4")
t.begin_fill()
t.circle(100, 25)
t.left(115)
t.forward(65)
t.right(90)
t.forward(42)
t.right(90)
t.forward(124)
t.right(90)
t.circle(-150, 50)
t.right(90)
t.forward(50)
t.end_fill()
t.up()
t.goto(100, 100)
t.down()
t.hideturtle()
turtle.done()
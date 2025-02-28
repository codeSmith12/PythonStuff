import turtle
pen = turtle.Turtle()



# BIG RED
pen.right(90)
pen.color("red")
pen.begin_fill()
pen.circle(100,-180)
pen.end_fill()
# pen.goto(0,0)
pen.goto(20,0)
pen.right(180)

# MEDIUM BLUE
pen.color("blue")
pen.begin_fill()
pen.circle(80,-180)
pen.end_fill()
pen.goto(50,0)

# SMALL GREEN
pen.color("lime")
pen.right(180)
pen.begin_fill()
pen.circle(50,-180)
pen.end_fill()


pen.color("yellow")
pen.goto(70,0)
pen.right(180)
pen.begin_fill()
pen.circle(30,-180)
pen.end_fill()


turtle.mainloop()
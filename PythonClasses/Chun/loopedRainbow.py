import turtle

pen = turtle.Turtle()
pen.speed(0)
colors = ["red","blue","lime","yellow","orange"]
turtle.bgcolor("black")
radius = 200
xOffset = radius/len(colors)

for i in range(len(colors)):
    pen.goto(-i*xOffset+(xOffset*5),0) # added xOffset*5 to bring it to the middle. not sure why it works
    pen.setheading(90)
    pen.color(colors[i])
    pen.begin_fill()
    pen.circle(radius, 180)
    pen.end_fill()
    radius -= xOffset
   
   
turtle.mainloop()
   
import turtle
# Y kanan
y2=turtle.Turtle()
y2.left(90)
y2.forward(50)
y2.right(45)
y2.forward(40)
# Bikin Y kiri
y1 = turtle.Turtle()
y1.left(90)
y1.forward(50)
y1.left(45)
y1.forward(40)

#Bikin 8
y2.goto(90,0)
y2.circle(20)
y2.circle(-15)

#Bikin 3
y2.goto(150,0)
y2.circle(20,200)
y2.right(180)
y2.circle(20,200)

#Bikin 6
y2.goto(210,0)
y2.circle(20,360)
y2.left(180)
y2.circle(10,-90)

#Bikin A
y2.goto(270,0)
y2.left(45)
y2.forward(70)
y2.right(90)



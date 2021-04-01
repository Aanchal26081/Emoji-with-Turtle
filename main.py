import turtle

# Creating turtle pen
pen = turtle.Turtle()
window = turtle.Screen()

# set the fillcolor
pen.fillcolor('yellow')

# start filling
pen.begin_fill()

# drawing circle of radius r
pen.up()
pen.goto(0,-120)
pen.down()
pen.circle(200)

# Ending the filing function
pen.end_fill()

# Values for eye 1
pen.fillcolor("white")
pen.begin_fill()
pen.up()
pen.goto(-70,130)
pen.down()
pen.pensize(2)
pen.circle(40)
pen.end_fill()


# Values for eye 2
pen.fillcolor("white")
pen.begin_fill()
pen.up()
pen.goto(70,130)
pen.down()
pen.pensize(2)
pen.circle(40)
pen.end_fill()

# values for inner eye
pen.fillcolor("black")
pen.begin_fill()
pen.up()
pen.goto(-70,140)
pen.down()
pen.pensize(2)
pen.circle(20)
pen.end_fill()

# values for inner eye
pen.fillcolor("black")
pen.begin_fill()
pen.up()
pen.goto(70,140)
pen.down()
pen.pensize(2)
pen.circle(20)
pen.end_fill()

# Mouth
pen.up()
pen.goto(-100,20)
pen.down()
pen.pensize(5)
pen.right(90)
pen.circle(100,180)
pen.left(90)
pen.forward(200)

# nose
pen.fillcolor("red")
pen.begin_fill()
pen.up()
pen.goto(30,80)
pen.down()
pen.right(60)
pen.forward(60)
pen.left(120)
pen.forward(60)
pen.left(120)
pen.forward(60)
pen.end_fill()

import turtle

def diamond(t):
    for i in range(8):
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.left(45)
    
chloe = turtle.Turtle()

diamond(chloe)

chloe.penup()
chloe.left(90)
chloe.forward(90)
chloe.right(90)
chloe.pendown()
chloe.color("red")
diamond(chloe)

chloe.penup()
chloe.forward(90)
chloe.pendown()
chloe.color("green")
diamond(chloe)

chloe.penup()
chloe.right(90)
chloe.forward(90)
chloe.left(90)
chloe.pendown()
chloe.color("blue")
diamond(chloe)


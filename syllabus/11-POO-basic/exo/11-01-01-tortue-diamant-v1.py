import turtle

def draw_diamond(t, c):
    t.color(c)
    for i in range(8):
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.left(45)
    
wn = turtle.Screen()

tortue1 = turtle.Turtle()
draw_diamond( tortue1, "red" )
 
tortue2 = turtle.Turtle()
tortue2.penup()
tortue2.forward(240)
tortue2.pendown()
draw_diamond( tortue2, "blue" )

tortue3 = turtle.Turtle()
tortue3.penup()
tortue3.left(90)
tortue3.forward(240)
tortue3.right(90)
tortue3.forward(240)
tortue3.pendown()
draw_diamond( tortue3, "black" )

tortue4 = turtle.Turtle()
tortue4.penup()
tortue4.left(90)
tortue4.forward(240)
tortue4.right(90)
tortue4.pendown()
draw_diamond( tortue4, "green" )

wn.mainloop()

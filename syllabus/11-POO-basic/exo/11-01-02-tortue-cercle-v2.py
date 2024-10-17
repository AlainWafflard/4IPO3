import turtle
lucie = turtle.Turtle()

for i in range(1,10):
    lucie.penup()
    lucie.home()
    lucie.right(90)
    lucie.forward(25*i)
    lucie.left(90)
    lucie.pendown()
    lucie.circle(25*i)


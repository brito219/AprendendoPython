import turtle
t=turtle.Turtle()
wn = turtle.Screen()              # Inicializa a janela e seus atributos
wn.bgcolor("white")
t.penup()
#draw straight line

t.goto(-30,50) #centering in the screen
t.pendown()
t.pensize(10)
t.pencolor("red")
 
t.forward(10)
t.right(90)
t.forward(150)
t.circle(-50,180)

wn.exitonclick()
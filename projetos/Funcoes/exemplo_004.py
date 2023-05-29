import turtle
tartaruga = turtle.Turtle()
# Apontando pra baixo e removendo a caneta

wn = turtle.Screen()              # Inicializa a janela e seus atributos
wn.bgcolor("blue")

tartaruga.right(90)
tartaruga.penup()
fonte1 = ("Comic Sans", 20, "italic")
tartaruga.write("eu", False, "center", fonte1)
tartaruga.forward(40)
fonte2 = ("Comic Sans", 20, "normal")
tartaruga.write("sou", False, "center", fonte2)
tartaruga.forward(40)
fonte3 = ("Comic Sans", 20, "bold")
tartaruga.write("Gay", False, "center", fonte3)

wn.exitonclick()
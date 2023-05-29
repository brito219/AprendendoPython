import turtle

def quadrado(t, tam):
    """Faca a tartaruga t desenhar um quadrado multicolorido de lado tam."""
    for i in ['red','black','red','black']:
        t.color(i)
        t.forward(tam)
        t.left(90)

wn = turtle.Screen()              # Inicializa a janela e seus atributos
wn.bgcolor("white")

tess = turtle.Turtle()            # cria tess e seus atributos
tess.pensize(3)

tamanho = 20                      # tamanho do menor quadrado
for i in range(15):
    quadrado(tess, tamanho)
    tamanho = tamanho + 10       # aumenta o tamanho para a próxima vez
    tess.forward(10)             # move tess um pouco à frente
    tess.right(18)               # e dá uma virada nela

wn.exitonclick()

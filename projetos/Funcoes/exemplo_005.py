import turtle
tartaruga = turtle.Turtle()

wn = turtle.Screen()              # Inicializa a janela e seus atributos
wn.bgcolor("white")
# Imagens
pokemons = ["pikachu.gif", "bulbassaur.gif", "charizard.gif", "squirtle.gif"]
# Posicao de cada imagem
posicoes = [(200, 200), (-200, 200), (-200, -200), (200, -200)]
tartaruga.penup()
# Registrando a imagem, mudando a forma e carimbando
for pokemon, posicao in zip(pokemons, posicoes):
    turtle.register_shape(pokemon)
    tartaruga.shape(pokemon)
    tartaruga.setpos(posicao)
    tartaruga.stamp()

wn.exitonclick()
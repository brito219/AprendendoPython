import random

#gerador de numeros aleatorios da mega sen

def nms():
    return random.sample(range(1, 61), 6)

def ennt(numeros):
    print("Números gerados mega sena: ")
    for numero in numeros:
        print(numero, end="  ")
    print(" ")

print("Gerador de números da mega-sena")

numeros = nms()
ennt(numeros)

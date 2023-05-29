a, b, c = map(float, input().split())

if a + b > c and a + c > b and b + c > a:
    # se a soma de dois lados for maior que o terceiro, forma um triângulo
    perimetro = a + b + c
    print("Perimetro = %.1f" % perimetro)
else:
    # caso contrário, forma um trapézio e calcula a área
    area = ((a + b) * c) / 2
    print("Area = %.1f" % area)

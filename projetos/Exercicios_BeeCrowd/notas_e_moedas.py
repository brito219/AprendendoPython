
'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. 
A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. 
As notas consideradas são de 100, 50, 20, 10, 5, 2. 
As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. 
A seguir mostre a relação de notas necessárias.
Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).
Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.
'''
reais, centavos = map(int, input().split('.'))
centavos = centavos + reais*100

notas = [100, 50, 20, 10, 5, 2]

print("NOTAS:")
for nota in notas:
    qtde = centavos//(nota*100)
    print('{} nota(s) de R$ {}.00'.format(qtde, nota))
    centavos = centavos%(nota*100)

moedas = [100, 50, 25, 10, 5, 1]

print("MOEDAS:")
for moeda in moedas:
    qtde = centavos//moeda
    m = moeda//100
    md = moeda%100
    print('{} moeda(s) de R$ {}.{:02}'.format(qtde, m, md))
    centavos = centavos%moeda
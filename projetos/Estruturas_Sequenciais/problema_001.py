'''
Problema: dadas cinco notas de uma prova dos(as) estudantes de
uma disciplina, calcular a média das notas da prova e a quantidade de
estudantes que obtiveram nota maior que a média e a quantidade de
estudantes que obtiveram nota menor que a média
'''

nota1, nota2, nota3, nota4, nota5 = input("Informe as notas: ").split()
nota1, nota2, nota3 = float(nota1),float(nota2),float(nota3)
nota4, nota5 = float(nota4), float(nota5)

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print("Média das provas: %f" % media)

menor = 0
if nota1 < media:
    menor += 1
if nota2 < media:
    menor += 1
if nota3 < media:
    menor += 1
if nota4 < media:
    menor += 1
if nota5 < media:
    menor += 1

maior = 0
if nota1 > media:
    maior += 1
if nota2 > media:
    maior += 1
if nota3 > media:
    maior += 1
if nota4 > media:
    maior += 1
if nota5 > media:
    maior += 1
print("Quantidade com nota inferior à média: %d" % menor)
print("Quantidade com nota superior à média: %d" % maior)

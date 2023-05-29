# -*- coding: utf-8 -*-

'''
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

Salário	Percentual de Reajuste
0 - 400.00 - 15%
400.01 - 800.00 - 12%
800.01 - 1200.00 - 10%
1200.01 - 2000.00 - 7%
Acima de 2000.00 - 4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.
Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.
Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste (ambos devem ser apresentados com 2 casas decimais) e o percentual 
de reajuste ganho, conforme exemplo abaixo.
'''
salario = float(input())

#caso o salario seja menor ou igual a 400
if salario <= 400 :
    reajuste = salario * 0.15
    percentual = 15
    salario += reajuste
    print(f"Novo salario: {salario:.2f}" )
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual} %")
elif salario <= 800:
    reajuste = salario * 0.12
    percentual = 12
    salario += reajuste
    print(f"Novo salario: {salario:.2f}" )
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual} %")
elif salario <= 1200 :
    percentual = 10
    reajuste = salario * 0.10
    salario += reajuste
    print(f"Novo salario: {salario:.2f}" )
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual} %")
elif salario <= 2000 :
    percentual = 7
    reajuste = salario * 0.07
    salario += reajuste
    print(f"Novo salario: {salario:.2f}" )
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual} %")
else :
    percentual = 4
    reajuste = salario * 0.04
    salario += reajuste
    print(f"Novo salario: {salario:.2f}" )
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual} %")
exit(0)
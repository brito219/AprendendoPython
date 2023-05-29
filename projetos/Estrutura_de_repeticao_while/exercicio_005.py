#!/usr/bin/env python
# -*- coding: utf-8 -*-


# tamanho da sequencia
n = int(input("Digite um número que delimitará a sequencia de somas: "))

# os dois comecam no 0 para comecar o laço
soma = 0
i = 0


while i < n:  # o while vai continuar repetindo enquanto i<n ; # o x soa os numeros que vou somar da sequencia até chegar no range que eu quero
    x = int(input())
    soma += x
    i += 1

print(soma)

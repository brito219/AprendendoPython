#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input("Digite um número inteiro não-negativo: "))

#propriedade do fatorial, 0!=1
if n == 0:
    resultado = 1

#caso nao seja 0
else:
    resultado = n
    
    while n > 1:
        n -= 1
        resultado *= n

print(resultado)

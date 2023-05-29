#!/usr/bin/env python
# -*- coding: utf-8 -*-

#recebe um valor de x e o substitui no polinomio definido

numero = int(input("Escreva um valor inteiro não negativo para x: "))

polinomio = 3*numero**3 - 5*numero**2 + 2*numero - 1

print("O resultado de %d no polinômio é de %d" % (numero,polinomio))

exit(0)

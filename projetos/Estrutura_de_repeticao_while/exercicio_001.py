#!/usr/bin/env python
# -*- coding: utf-8 -*-



n = int(input("Informe n: "))
soma = 0
numero = 1

while numero <= n:
    soma += numero
    numero = numero + 1

print("Soma dos %d primeiros inteiros é %d" % (n, soma))

exit(0)
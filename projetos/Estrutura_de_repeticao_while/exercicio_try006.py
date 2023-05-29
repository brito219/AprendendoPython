#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    n = int(input("Digite um número inteiro positivo: "))
except (ValueError, NameError):
    print("Valor Inválido")
    exit(0)
else:
    print(n)
    exit(0)

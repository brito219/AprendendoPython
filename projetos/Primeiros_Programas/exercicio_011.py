#!/usr/bin/env python
# -*- coding: utf-8 -*-

#um programa que recebe dois números inteiros positivos e devolve o menor inteiro m maior
#que i e multiplo de j

i= int(input("escreva o valor de i: "))
j = int(input("escreva o valor de j: "))

n = i + j - i % j

print("o valor é = %d" % (n*n/j))

exit(0)

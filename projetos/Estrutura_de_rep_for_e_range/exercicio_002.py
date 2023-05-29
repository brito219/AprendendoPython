#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Verifique se o programa a seguir soluciona o seguinte problema:
dado um número inteiro não-negativo n, escreva um programa
que determine quantos dígitos o número n possui. Faça pelo
menos uma simulação da execução passo a passo da sua
solução.



n = int(input("Informe n: "))

digitos = 0

if n == 0:
    digitos = 1

while n > 0:
    n /= 10
    digitos += 1

print("O número tem %d dígitos" % (digitos))


o erro ta na linha 20, onde ele faz uma divisao normal e tava retornando
valores com ponto flutuante, é so trocar o /= por //
'''


n = int(input("Informe n: "))

digitos = 0

if n == 0:
    digitos = 1

while n > 0:
    n = n//10
    digitos += 1

print("O número tem %d dígitos" % (digitos))


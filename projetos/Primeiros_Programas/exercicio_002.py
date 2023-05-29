#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Realiza operações aritméticas com números */

y = 10
r = 25 + y
print("A soma de %d e %d é %d" % (25, y, r))

x = 38
r = x - 25
print("A subtração de %d e %d é %d" % (x, 25, r))

x = 51
y = 17
r = x * y
print("A multiplicação de %d por %d é %d" % (x, y, r))

x = 90
y = 4
r = x / y
print("O quociente da divisão de %d por %d é %d" % (x, y, r))

x = 90
y = 4
r = x // y
print("O quociente inteiro da divisão de %d por %d é %d" % (x, y, r))

x = 17
y = 3
r = x % y
print("O resto da divisão de %d por %d é %d" % (x, y, r))

x = -7
r = -x
print("%d com sinal trocado é %d" % (x, r))

r = abs(x)
print("O valor absoluto de %d é %d" % (x, r))

x = 2
y = 3
r = x ** y
print("%d à %d potência é %d" % (x, y, r))

x = 10
y = 4
z = 15
r = x + y * z
print("A expressão %d+%d*%d é %d" % (x, y, z, r))


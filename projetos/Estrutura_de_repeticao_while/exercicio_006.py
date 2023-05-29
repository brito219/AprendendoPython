#!/usr/bin/env python
# -*- coding: utf-8 -*-


n = int(input("Digite um número que delimitará a sequencia de somas: "))
soma = 0
i = 0

#esse if serve pra só somar(que ta identado dentro do if) quando é positivo
while i < n:  
    x = int(input())
    if x > 0:
        soma += x
    i += 1

print(soma)
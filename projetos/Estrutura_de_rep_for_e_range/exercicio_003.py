#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Dado um número natural na base binária, transformá-lo para a
base decimal.
Exemplo:
Dado 10010 a saída será 18, pois
1*2⁴ + 0*2³ + 0*2² + 1*2¹ + 0*2⁰ = 18
'''

n = int(input("informe um n: "))
dec = 0
p = 1

while n > 0:
    d = n%10
    dec+=p*d
    p*= 2 
    n = n//10

print("o numero vale %d" % (dec))

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#coloca x y z em ordem crescente

x = int(input("insira o valor de x: "))
y = int(input("insira o valor de y: "))
z = int(input("insira o valor de z: "))

if x > y:
    x, y = y, x

if y > z:
    y, z = z, y

    if y > x:
        x, y = y, x

print("os três números em ordem crescente são: %d, %d, %d," % (x,y,z))

exit(0)

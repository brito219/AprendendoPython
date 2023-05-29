#!/usr/bin/env python
# -*- coding: utf-8 -*-

#dá uma descricao dependendo do delta calculado

soma = 0

print("informe três números a, b, c:")
a = float(input)
b = float(input)
c = float(input)

d= b**2 - 4*a*c

if d == 0:
    print("raíz única")
    x = -b/2*a
    print (x)
elif d > 0:
    print("raízes distintas")
    x1 = (-b + d**(0.5))/(2*a)
    x2 = (-b - d**(0.5))/(2*a)
    print("x1 = %f x2 = %f" % (x1,x2))
else:
    print("complexo")

exit(0)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

A,B,C = map(float, input().split())

print(f"TRIANGULO: {A*C/2: .3f}")
print(f"CIRCULO: {3.14159*C*C: .3f}")
print(f"TREPEZIO: {(A+B)*C/2: .3f}")
print(f"QUADRADO: {B*B: .3f}")
print(f"RETANGULO: {A*B: .3f}")

A,B,C = map(float, input().split)

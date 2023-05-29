#!/usr/bin/env python
# -*- coding: utf-8 -*-


n = int(input("Digite um número que delimitará a sequencia de somas: "))
somap = somai = 0
i = 0

while i < n:
    x = int(input())
    if x % 2 == 0:
        somap += x
    else:
        x % 2 == 1
        somai += x
    i += 1

print(somap, somai)

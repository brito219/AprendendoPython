#!/usr/bin/env python
# -*- coding: utf-8 -

n = 7  # 7 dias da semana
i = 1  # comeca com dia 1 domingo
maior = -1


while i <= n:
    x = int(input())
    if x > maior:
        maior = x
        dia = i
    i += 1

print(maior, dia)

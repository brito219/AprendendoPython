#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Conta quantos espaços a string lida tem


texto = input()
cont = 0

for letra in texto:
    if letra == " ":
        cont += 1
        
print("O texto digitado tem %d espaços" % cont)
exit(0)
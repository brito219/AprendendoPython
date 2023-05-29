#!/usr/bin/env python
# -*- coding: utf-8 -*-

#verifica comprimento, maiusculas, minusculas, espacos e separacao de uma string

t = input("Digite um texto com mais de duas palavras: ")
s1, s2 = t.split()

print("vc digitou %s que tem comprimento %d") % (t, len(t))
print("Texto maiúsculo: " + t.upper())
print("Texto maiúsculo: " + t.lower())
print("Texto sem espaços: " + t.replace(" ", ""))
print("Texto separado: " + t.split())

print(s1)
print(s2)
exit(0)

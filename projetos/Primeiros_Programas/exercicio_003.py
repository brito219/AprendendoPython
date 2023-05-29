#!/usr/bin/env python
# -*- coding: utf-8 -*-

#faz a média de 4 notas

nota1 = int(input('Escreva a primeira nota: '))
nota2 = int(input('Escreva a segunda nota: '))
nota3 = int(input('Escreva a terceira nota: ' ))
nota4 = int(input('Escreva a quarta nota: ' ))

soma = float(nota1 + nota2 + nota3 + nota4)
media = soma/4

print('A média é = %.2f' % (media))

exit(0)
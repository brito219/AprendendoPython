#!/usr/bin/env python
# -*- coding: utf-8 -*-

#recomenda um peso de acordo com uma formula relacionada a altura

h = float(input('escreva sua altura em metros: '))

homens = (72.7*h)-58
mulheres = (62.1*h)-44.7

print('sendo %d a sua altura, se você for uma  mulher seu peso recomendado é: %d, caso seja homem o peso recomendado é: %d' % (h,mulheres,homens))

exit(0)

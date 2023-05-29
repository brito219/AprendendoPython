#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Qualquer número natural de quatro algarismos pode ser dividido
#em duas dezenas formadas pelos seus dois primeiros e dois
#últimos dígitos.
#Exemplos:
#1297: 12 e 97; 5314: 53 e 14.
#Verifique se o programa a seguir imprime todos os números
#naturais de quatro algarismos cuja raiz quadrada é a soma das
#dezenas formadas pela divisão acima. Por exemplo, 9801 é um
#dos números a ser impresso, já que
#9801 = 99 = 98 + 01.

import math 

for num in range (1000,10000):
    dd = num % 100
    DD = num // 100

    if math.sqrt(num) == DD + dd:
        print(num)
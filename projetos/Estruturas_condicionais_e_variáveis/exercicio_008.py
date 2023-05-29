#Escreva um programa que receba dois tempos no formato
#hh:mm:ss (um tempo por linha), some os dois tempos e escreva
#o tempo resultante. Por exemplo, para os tempos 03:10:32 e
#04:55:40, você deve escrever na tela 08:06:12. Dica: para ler os
#tempos, você vai precisar utilizar input.split() de uma forma
#diferente da que usamos até agora, procure informações sobre a
#função split() do Python.

#!/usr/bin/env python
# -*- coding: utf-8 -*-


temp1 = int(input("Escreva o tempo inicial no modelo hh:mm:ss: ").split(":"))
temp2 = int(input("Escreva o tempo final no modelo hh:mm:ss: ").split(":"))


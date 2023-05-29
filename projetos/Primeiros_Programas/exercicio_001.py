#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Recebe um número inteiro e emite uma
# mensagem de acordo com esse número

idade = int(input("Quantos anos você tem? "))


if idade < 30:
    print("Puxa! Você é bem jovem!")

elif idade > 60:
    print("Você já não é tão jovem!")

else:
    print("Você não é jovem nem velho!")


print("Até breve!")


exit(0)

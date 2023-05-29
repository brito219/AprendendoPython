#entrada
n1, n2, n3, n4 = map(float, input().split())

#média
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10

#print da média
print('Media: %.1f' % media)

#verificar aprovacao
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print('Aluno em exame.')

    # nota do exame
    nex = float(input())

    # calcular media final do rapaz do exame
    mf = (media + nex) / 2

    #print da nota do exame
    print("Nota do exame: %.1f" % nex)

    # ver se o aluno reprovou
    if mf >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')

    # print da mf
    print("Media final: %.1f" % mf)

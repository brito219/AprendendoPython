gabarito = input("escreva as respostas corretas das questões (sem espaços, ex: ABCDEF): ") 
n = int(input("número de estudantes: "))

rp_estudantes = [] #resposta de cada estudante

for i in range(n):
    resposta = input("escreva as respostas do estudante %d: " % (i+1))
    rp_estudantes.append(resposta) #armazenando as respostas na lista rp_estudantes

qntacertos = [] #quantidade de caertos de cada estudante

# Comparar as respostas de cada estudante com o gabarito e contar os acertos
for resposta_estudante in rp_estudantes:
    acertos = 0
    for i in range(len(gabarito)):
        if resposta_estudante[i] == gabarito[i]:
            acertos += 1
    qntacertos.append(acertos)


for i in range(n):
    print("estudante %d: %d acertos" % (i+1, qntacertos[i]))

#resolucao do problema 001 fazendo uso da nova ferramenta que aprendi
#as listas

n = int(input("Digite a quantidade de notas: "))

notas = [] #lista com as notas 
for i in range(n):
    notas.append(float(input()))  #append insere as notas 


media = 0.0
for nota in notas:
    media += nota
media /= n


menor = maior = 0
for nota in notas:
    if nota < media:
        menor += 1
    if nota >= media:
        maior += 1

print("Média: %2.2f, %d menores e %d maiores" % (media, menor, maior))

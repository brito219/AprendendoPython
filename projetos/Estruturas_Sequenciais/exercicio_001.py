#Dado um n inteiro e uma sequência de n números inteiros (um por
#linha), imprima a sequência em ordem inversa à de leitura.

n = int(input("digite a quantidade de notas : "))
l = []

for i in range (n):
    l.append(int(input))

for i in range (n-1, -1, -1):
    print(l[i]) #devolver so um elemento da lista com s[i] ou slice

for x in l:  #as duas ultimas formas printam normal
    print(x)

for x in range (n):
    print(l[x])
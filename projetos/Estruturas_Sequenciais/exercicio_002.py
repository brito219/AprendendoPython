'''
Dado um inteiro n que representa uma quantidade de dias e uma
sequência de n valores (um por linha) representando as
t desses dias, responda quais dias tiveram
temperatura acima da média.
'''

n = int(input("digite a quantidade de dias: ")) #quantidade de dias
t = [] #lista pra armazenar temperatura

for i in range(n): #adiciona temperatura a lista
    temp = float(input("Digite a temperatura do dia %d: " % (i+1)))
    t.append(temp)

media = sum(t) / n #media temperatura
print(" a média é %.2f " % media) #printei pra ver se tava dando certo

dam = [] #dias acima da media

for i in range(n): # Verifica os dias com temperatura acima da média e adiciona à lista
    if t[i] > media:
        dam.append(i+1)

print("dias com temperatura acima da média:", dam) # Exibe os dias com temperatura acima da média

Algumas operações suportadas por listas, supondo listas s e t ,
inteiros i , j e k , e algum valor/variável de qualquer tipo x :


Operação Resultado
x in s True = se algum item de s é igual a x, False c.c
x not in s True = se nenhum item de s é igual a x, False c.c
s + t = devolve a concatenação de s e t
s[i] = i-ésimo item de s (começando em 0)
s[i:j] = fatia de i até j-1
len(s) = devolve o comprimento de s
min(s) = devolve o menor elemento de s
max(s) = devolve o maior elemento de s
sum(s) = devolve a soma dos elementos de s
s.count(x) = devolve o número de ocorrências dex em s
s[i] = x = altera o valor na posição i para x
del s[slice] = remove os elementos do slice de s (pode ser 1 única posição ou um intervalo)
s.append(x) = adiciona x ao final da lista s
s.clear() = remove todos elementos de s
s.copy() = cria uma cópia de s
s.extend(t) ou s += t = estende s com os elementos de t
s.insert(i, x) = insere x em s na posição i (empurra os elementos posteriores)
s.remove(x) =remove a primeira ocorrência do valor x na lista
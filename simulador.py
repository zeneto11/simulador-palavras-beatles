from random import random


palavras = {'YOU': 20338, 'I': 15302,
'ME': 8838, 'A': 7830,
'TO': 7390, 'THE': 11432,
'AND': 5362, 'LOVE': 4642,
'YEAH': 1952, 'ALL': 3953,
'ON': 917, 'GIRL': 1084,
'IS': 2532, 'NEED': 2061,
'IN': 1303, 'COME': 0,
'BE': 577, 'NO': 577,
'THAT': 518, 'GOOD': 1075,
'TOO': 1167, 'MUCH': 1150}

palavras = dict(sorted(palavras.items(), key=lambda item: item[1], reverse=True)) #ordenandando os valores no dicionário
print(palavras)
soma_total = sum(palavras.values())
print(soma_total)

nome_palavra = list(palavras.keys())
valor_palavra = list(palavras.values())

for n in range(1):
    palavras_geradas = []

    for j in range(len(nome_palavra)):
        valor_sucessor = random() * soma_total
        soma = 0
        i = 0
        x = -1
        while i < len(nome_palavra) and soma < valor_sucessor:
                soma += valor_palavra[i]
                x += 1
                i += 1
        palavras_geradas.append(nome_palavra[x])

print(set(palavras_geradas))

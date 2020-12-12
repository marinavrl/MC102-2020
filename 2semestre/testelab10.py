"""Testar funcoes """

"""
matriz = [['q', 'i', 'a', 'u', 'k', 'r', 't'], 
          ['c', 'p', 'w', 'n', 'z', 's', 't'], 
          ['o', 'k', 'i', 'i', 'i', 'b', 'q'], 
          ['u', 'n', 'i', '*', 'a', 'm', 'p'], 
          ['p', 'c', 'o', 'a', 'o', 'z', 'r'], 
          ['a', 'y', 'z', 'm', 'v', 'v', 'd'], 
          ['c', 'h', 'j', 'p', 'd', 'f', 'u']]

palavras = ['unicamp'] """

for palavra in palavras:
    for l in range(palavra):
        for i in range(len(matriz)):
            linha = i
            for j in range(len(linha)):
                coluna = j
                if palavra[l] == matriz[linha][coluna]:

def horizontal(matriz, linha, coluna, palavra):
    for l in range(palavra):
        if palavra[l] == matriz[linha][coluna]:

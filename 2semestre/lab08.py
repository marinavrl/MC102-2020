###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Ocorrência de Palavras
# Nome: Marina Victória Roncalio de Lima
# RA: 241482
###################################################

"""O programa deve contabilizar a freq
da palavra sozinha bem como dentro de outras """

# Leitura de dados

L = int(input()) # quantidade de linhas do texto

conjunto = {".", ",", ":", ";", "!", "?"}

linhas = []

for _ in range(L): #recebe as L linhas
    linha0 = input().split()
    linha = []
    for palavra in linha0:
        palavra = palavra.lower()
        for i in range(len(palavra)):
            if palavra[i] in conjunto:
                palavra = palavra.replace(palavra[i], "")
        linha.append(palavra)

    linhas += linha #devolve a lista arrumada com as palavras repetidas

print(linhas)

N = int(input()) # recebe a quantidade de palavras desejadas

busca = []

for _ in range(N):
    palavra = input()
    palavra = palavra.lower()
    busca.append(palavra)

print(busca)

"""ocorrencia = 0"""

"""Como saída, seu programa deve fornecer, para cada palavra, 
a quantidade de vezes que ela ocorre exatamente e a quantidade de
 palavras similares, mas não exatamente iguais."""

#montar uma lista com as palavras buscadas (mantem a ordem
# do input); devolver a saída de acordo com essa lista
#usar um for para percorrer e imprimir de acordo
#talvez seja bom uma lista de tuplas: (palavra, ocorrencia)
#ver como fazer a lista de tuplas aos poucos


for palavra in linhas:


"""
# Processamento do texto




# Saída de dados

print("Palavra buscada:", palavra)
print("Ocorrencia:", ocorrencia)
print("Palavras similares:", similares) """
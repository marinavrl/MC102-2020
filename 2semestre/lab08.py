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

N = int(input()) # recebe a quantidade de palavras desejadas

ocorrencia = 0

for palavra in linhas:


"""
# Processamento do texto




# Saída de dados

print("Palavra buscada:", palavra)
print("Ocorrencia:", ocorrencia)
print("Palavras similares:", similares) """
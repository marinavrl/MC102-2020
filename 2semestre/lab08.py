###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Ocorrência de Palavras
# Nome: Marina Victória Roncalio de Lima
# RA: 241482
###################################################

# Leitura de dados

L = int(input())

conjunto = {".", ",", ":", ";", "!", "?"}

linhas = []

for _ in range(L):
    linha0 = input().split()
    linha = []
    for palavra in linha0:
        palavra = palavra.lower()
        for i in range(len(palavra)):
            if palavra[i] in conjunto:
                palavra = palavra.replace(palavra[i], "")
        linha.append(palavra)

    linhas += linha

N = int(input())

busca = []

for _ in range(N):
    palavra = input()
    busca.append(palavra)

for palavra in busca:
    palavra0 = palavra.lower()
    k = len(palavra0)
    j = len(palavra0) - 1
    ocorrencia = 0
    similares = 0
    for buscada in linhas:
        if buscada == palavra0:
            ocorrencia += 1
        elif buscada != palavra0 and len(buscada) >= k:
            if buscada[0:k] == palavra0:
                similares += 1
            elif k == 2 and buscada[0:k] != palavra0:
                for i in range(len(buscada)):
                    if buscada[i:len(buscada)] == palavra0:
                        similares += 1
                    elif buscada[i:len(buscada)-1] == palavra0:
                        similares += 1
                    elif buscada[i:i+k] == palavra0:
                        similares += 1
            elif k>=3 and buscada[0:k] != palavra0:
                if buscada[0:j] == palavra0[0:j] and len(palavra0[0:j]) > 3:
                    similares += 1
                elif buscada[0:j] != palavra0[0:j]:
                    for i in range(len(buscada)):
                        if buscada[i:] == palavra0:
                            similares += 1
                        elif buscada[i:len(buscada)-1] == palavra0:
                            similares += 1


    # Saída de dados

    print("Palavra buscada:", palavra)
    print("Ocorrencia:", ocorrencia)
    print("Palavras similares:", similares)
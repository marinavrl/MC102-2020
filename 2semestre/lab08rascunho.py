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
    linha0 = input().split() #lista com as palavras nao editadas
    linha = [] #cada linha do texto
    for palavra in linha0: #percorre a lista
        palavra = palavra.lower()
        for i in range(len(palavra)):
            if palavra[i] in conjunto:
                palavra = palavra.replace(palavra[i], "")
        linha.append(palavra) #forma a lista editada

    linhas += linha #devolve a lista arrumada com as palavras repetidas

print(linhas)
"""linhas = ['teus', 'olhos', 'sao', 'meus', 'livros', 'que', 'livro', 'ha', 
'ai', 'melhor', 'em', 'que', 'melhor', 'se', 'leia', 'a', 'pagina', 'do', 'amor'] """

N = int(input()) # recebe a quantidade de palavras desejadas

busca = []

for _ in range(N):
    palavra = input()
    busca.append(palavra)

print(busca) #busca tem as palavras sem lower pra devolver
#na configuracao certa

for palavra in busca: # percorre a lista busca
    palavra0 = palavra.lower() #deixa igual em linhas
    k = len(palavra0)
    j = len(palavra0) - 1
    ocorrencia = 0
    similares = 0
    for buscada in linhas:
        if buscada == palavra0:
            ocorrencia += 1
        elif buscada != palavra0:
            if buscada[0:k] == palavra0 or buscada[0:j] == palavra0[0:j]:
                similares += 1

    # Saída de dados

    print("Palavra buscada:", palavra)
    print("Ocorrencia:", ocorrencia)
    print("Palavras similares:", similares)






"""Como saída, seu programa deve fornecer, para cada palavra, 
a quantidade de vezes que ela ocorre exatamente e a quantidade de
 palavras similares, mas não exatamente iguais."""

#montar uma lista com as palavras buscadas (mantem a ordem
# do input); devolver a saída de acordo com essa lista
#usar um for para percorrer e imprimir de acordo
#talvez seja bom uma lista de tuplas: (palavra, ocorrencia)
#ver como fazer a lista de tuplas aos poucos


"""for palavra in linhas:"""


"""
# Processamento do texto




# Saída de dados

print("Palavra buscada:", palavra)
print("Ocorrencia:", ocorrencia)
print("Palavras similares:", similares) """
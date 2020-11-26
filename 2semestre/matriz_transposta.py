#estrutura da matriz

""" M = [[1, 2, 3, 4],
         [5, 6, 7, 8]] """

#leitura da matriz

def lê_matriz():
    M = []
    while True:
        temp = input().split()
        if temp == []:
            return M
        linha = []
        for i in temp:
            linha.append(int(i))
        M.append(linha)

#calcula as dimensoes da matriz

def dimensões(M):
    linhas = len(M)
    colunas = len(M[0])
    for i in range(1, linhas):
        if len(M[i]) != colunas:
            return ()
    return (linhas, colunas)

def transposta(M):
    T = []
    (linhas, colunas) = dimensões(M)
    for j in range(colunas):
        T.append([])
        for i in range(linhas):
            T[j].append(M[i][j])
    return T

def imprime_matriz(M):
    for linha in M:
        # converte os elementos da lista para string
        aux = [str(i) for i in linha]
        print(" ".join(aux))


def main():
    M = lê_matriz()
    (linhas, colunas) = dimensões(M)
    print(M)
    imprime_matriz(M)
    print(linhas)
    print(colunas)
    T = transposta(M)
    print(T)
    imprime_matriz(T)

main()

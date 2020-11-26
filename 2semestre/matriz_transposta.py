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

def main():
    M = lê_matriz
    print(M)

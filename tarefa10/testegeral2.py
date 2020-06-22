def matriz_imagem(L):
    imagem = []
    for i in range(2, len(L)):
        imagem.append(list(L[i].strip()))
    return imagem

def main():
    L = ['P1', '6 10', '000010', '000010', '000010', '000010', '000010', '000010', '100010', '011100', '000000', '000000']
    imagem = matriz_imagem(L)
    print(imagem)

main()    
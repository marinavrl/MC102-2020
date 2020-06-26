def decodificar(largura, altura, codificacao):
    imagem_codificada = codificacao
    for i in range(0,len(imagem_codificada),2):
        imagem_codificada[i] = int(imagem_codificada[i])
    imagem = []
    for _ in range(altura):
        imagem.append([])
    linhas_impares = []
    linhas_pares = []
    for k in range(0, len(imagem_codificada), 2):
        for _ in range(imagem_codificada[k]):
            linhas_impares.append(imagem_codificada[k+1][0])
            linhas_pares.append(imagem_codificada[k+1][1])
    i = 0
    for j in range(0, len(linhas_impares), largura):
        for elemento in linhas_impares[j:j+largura]:
            imagem[i].append(elemento)
        for elemento in linhas_pares[j:j+largura]:
            imagem[i+1].append(elemento)
        i += 2
    return imagem
                
#'P1C', '16', '16', '1 00 14 01 2 00 1 11 1 00 1 11 8 00 1 11 1 01 1 11 2 00 1 11 1 00 1 11 8 00 1 11 1 00 1 11 2 00 1 11 1 00 1 11 8 00 1 11 1 00 1 11 2 00 1 11 2 00 8 10 2 00 1 11 2 00 1 11 2 00 6 11 2 10 1 11 1 00 1 11 2 00 1 11 2 00 6 11 2 00 1 11 1 00 1 11 3 00 13 10 1 00']
#6 10 4 00 1 11 5 00 1 11 5 00 1 11 1 00 1 10 3 01 1 10 7 00
def main():
    codificacao = ['4', '00', '1', '11', '5', '00', '1', '11', '5', '00', '1', '11', '1', '00', '1', '10', '3', '01', '1', '10', '7', '00']
    largura = 6
    altura = 10
    imagem = decodificar(largura, altura, codificacao)
    print(imagem)

main()

"""imagem_codificada = codificacao
    for i in range(0,len(imagem_codificada),2):
        imagem_codificada[i] = int(imagem_codificada[i])
    imagem = []
    for _ in range(altura):
        imagem.append([])
    linhas_impares = []
    linhas_pares = []
    for k in range(0, len(imagem_codificada), 2):
        for _ in range(imagem_codificada[k]):
            linhas_impares.append(imagem_codificada[k+1][0])
            linhas_pares.append(imagem_codificada[k+1][1])
    i = 0
    for j in range(0, len(linhas_impares), largura):
        for elemento in linhas_impares[j:j+largura]:
            imagem[i].append(elemento)
        for elemento in linhas_pares[j:j+largura]:
            imagem[i+1].append(elemento)
        i += 2"""
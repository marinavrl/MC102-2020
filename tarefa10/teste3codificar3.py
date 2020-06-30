def codificar(largura, altura, imagem):
    """ Le a matriz de bits, sua largura e altura e devolve a codificacao """
    largura = int(largura)
    altura = int(altura)
    codificacao = []
    a = 1 #define antes
    for i in range(0,altura,2):
        for j in range(largura):
            point = True #ajuda a marcar que nao ta repetindo contagem
            if j < largura - 1:#faz a soma de strings
                if imagem[i][j] + imagem[i+1][j] == imagem[i][j+1] + imagem[i+1][j+1]:
                    a+=1
                    point = False
            if j == largura - 1 and i+2<altura:
                if imagem[i][j] + imagem[i+1][j] == imagem[i+2][0] + imagem[i+3][0]:
                    a+=1
                    point = False
            if point or i+j==(altura + largura - 3):
                codificacao.append(str(a))
                codificacao.append(imagem[i][j] + imagem[i+1][j])
                a = 1 #comeca a contar de novo 
    return codificacao

def main():
    imagem = [
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '1', '1', '1', '1', '0', '0', '1', '1', '1', '1', '0', '0', '1', '1', '1', '1', '0', '0', '1', '1', '1', '1', '0'],
        ['0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0'],
        ['0', '1', '1', '1', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '1', '1', '1', '0'],
        ['0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0'],
        ['0', '1', '0', '0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '1', '1', '1', '1', '0', '0', '1', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ]
    largura = len(imagem[0])
    altura = len(imagem)
    codificacao = codificar(largura, altura, imagem)
    print(codificacao)

main()
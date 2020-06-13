def codificar(largura, altura,imagem):
    codificacao = []
    codificacao.append('P1C')
    codificacao.append(str(largura))
    codificacao.append(str(altura))
    altura = len(imagem)
    largura = len(imagem[0])
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(altura):
        if i % 2 != 0:
            continue
        else:
            for j in range(largura):
                if j != imagem[-1]:#nao da certo porque n se refere ao ultimo elem da sublista, sim a ultima lista
                    if imagem[i][j] == '0' and imagem[i + 1][j] == '0':
                        a += 1
                    elif imagem[i][j] == '0' and imagem[i + 1][j] == '1':
                        b += 1
                    elif imagem[i][j] == '1' and imagem[i + 1][j] == '0':
                        c += 1
                    elif imagem[i][j] == '1' and imagem[i + 1][j] == '1':
                        d += 1
            if imagem[i][j] == '0' and imagem[i + 1][j] == '0':
                if str(a) and '00' not in codificacao and a != 0:
                    if j == imagem[-1]:
                        a += 1
                    else:
                        codificacao.append(str(a))
                        codificacao.append('00')
            elif imagem[i][j] != '0' and imagem[i + 1][j] == '1':
                if str(b) and '01' not in codificacao and b != 0:
                    if j == imagem[-1]:
                        b += 1
                    else:
                        codificacao.append(str(b))
                        codificacao.append('01')
            elif imagem[i][j] == '1' and imagem[i + 1][j] == '0':
                if str(c) and '10' not in codificacao and c != 0:
                    if j == imagem[-1]:
                        c += 1
                    else:
                        codificacao.append(str(c))
                        codificacao.append('10')
            elif imagem[i][j] == '1' and imagem[i + 1][j] == '1':
                if str(d) and '11' not in codificacao and d != 0:
                    if j == imagem[-1]:
                        d += 1
                    else:
                        codificacao.append(str(d))
                        codificacao.append('11')
    return codificacao

    """"if j != len(imagem[0])-1 and i != len(imagem) - 1:
                    if imagem[i][j] == '0' and imagem[i + 1][j] == '0':
                        a += 1
                        continue
                    elif imagem[i][j] == '0' and imagem[i + 1][j] == '1':
                        b += 1
                        continue
                    elif imagem[i][j] == '1' and imagem[i + 1][j] == '0':
                        c += 1
                        continue
                    elif imagem[i][j] == '1' and imagem[i + 1][j] == '1':
                        d += 1
                        continue """

def main():
    imagem = [
        ['0', '0', '0', '0', '1', '0'],
        ['0', '0', '0', '0', '1', '0'],
        ['0', '0', '0', '0', '1', '0'],
        ['0', '0', '0', '0', '1', '0'],
        ['0', '0', '0', '0', '1', '0'],
        ['0', '0', '0', '0', '1', '0'],
        ['1', '0', '0', '0', '1', '0'],
        ['0', '1', '1', '1', '0', '0'],
        ['0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0'],
    ]
    largura = str(len(imagem[0]))
    altura = str(len(imagem))
    codificacao = codificar(largura, altura, imagem)
    print(' '.join(codificacao))

main()

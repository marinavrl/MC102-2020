def codificar(largura, altura,imagem):
    codificacao = []
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(len(imagem)):
        if i % 2 != 0:
            continue
        else:
            for j in range(len(imagem[0])):
                if j != len(imagem[0])-1 and i != len(imagem) - 1:
                        if imagem[i][j] == '0' and imagem[i + 1][j] == '0':
                            a += 1
                            if imagem[i][j + 1] != '0' and imagem[i + 1][j + 1] != '0':
                                codificacao.append(str(a))
                                codificacao.append('00')
                                a = 0
                        elif imagem[i][j] == '0' and imagem[i + 1][j] == '1':
                            b += 1
                            if imagem[i][j + 1] != '0' or imagem[i + 1][j + 1] != '1':
                                codificacao.append(str(b))
                                codificacao.append('01')
                                b = 0
                        elif imagem[i][j] == '1' and imagem[i + 1][j] == '0':
                            c += 1
                            if imagem[i][j + 1] != '1' or imagem[i + 1][j + 1] != '0':
                                codificacao.append(str(c))
                                codificacao.append('10')
                                c = 0
                        elif imagem[i][j] == '1' and imagem[i + 1][j] == '1':
                            d += 1
                            if imagem[i][j + 1] != '1' or imagem[i + 1][j + 1] != '1':
                                codificacao.append(str(d))
                                codificacao.append('11')
                                d = 0
                elif j == len(imagem[0])-1 and i < len(imagem) - 2:
                    if imagem[i][j] == '0' and imagem[i + 1][j] == '0':
                        a += 1
                        if imagem[i + 2][0] != '0' or imagem[i + 3][0] != '0':
                            codificacao.append(str(a))
                            codificacao.append('00')
                            a = 0
                    elif imagem[i][j] == '0' and imagem[i + 1][j] == '1':
                        b += 1
                        if imagem[i + 2][0] != '0' and imagem[i + 3][0] != '1':
                            codificacao.append(str(b))
                            codificacao.append('01')
                            b = 0
                    elif imagem[i][j] == '1' and imagem[i + 1][j] == '0':
                        c += 1
                        if imagem[i + 2][0] != '1' and imagem[i + 3][0] != '0':
                            codificacao.append(str(c))
                            codificacao.append('10')
                            c = 0
                    elif imagem[i][j] == '1' and imagem[i + 1][j] == '1':
                        d += 1
                        if imagem[i + 2][0] != '1' and imagem[i + 3][0] != '1':
                            codificacao.append(str(d))
                            codificacao.append('11')
                            d = 0
                else:
                    if imagem[i][j] == '0' and imagem[i + 1][j] == '0':
                        a += 1
                        codificacao.append(str(a))
                        codificacao.append('00')
                    elif imagem[i][j] == '0' and imagem[i + 1][j] == '1':
                        b += 1
                        codificacao.append(str(b))
                        codificacao.append('01')
                    elif imagem[i][j] == '1' and imagem[i + 1][j] == '0':
                        c += 1
                        codificacao.append(str(c))
                        codificacao.append('10')
                    elif imagem[i][j] == '1' and imagem[i + 1][j] == '1':
                        d += 1
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
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], 
    ['0', '1', '1', '1', '1', '0', '0', '1', '1', '1', '1', '0', '0', '1', '1', '1', '1', '0', '0', '1', '1', '1', '1', '0'], 
    ['0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0'], 
    ['0', '1', '1', '1', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '1', '1', '1', '0'], 
    ['0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0'], 
    ['0', '1', '0', '0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '1', '1', '1', '1', '0', '0', '1', '0', '0', '0', '0'], 
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']]
    largura = str(len(imagem[0]))
    altura = str(len(imagem))
    codificacao = codificar(largura, altura, imagem)
    print(' '.join(codificacao))

main()

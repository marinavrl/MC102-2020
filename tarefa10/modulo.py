def codificar(largura,altura,imagem):
    codificacao = []
    m = len(imagem)
    n = len(imagem[0])
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(m):
        if i % 2 != 0:
            continue
        else:
            for j in range(n):
                if imagem[i][j] == '0' and imagem[i + 1][j] == '0': # ver se mudando tudo ra if faz sentido
                    a += 1
                elif imagem[i][j] == '0' and imagem[i + 1][j] == '1':
                    b += 1
                elif imagem[i][j] == '1' and imagem[i + 1][j] == '0':
                    c += 1
                elif imagem[i][j] == '1' and imagem[i + 1][j] == '1':
                    d += 1
    for i in range(m):
        if i % 2 != 0:
            continue
        else:
            for j in range(n):
                if imagem[i][j] == '0' and imagem[i + 1][j] == '0' and a != 0:
                    if str(a) and '00' not in codificacao:
                        codificacao.append(str(a))
                        codificacao.append('00')
                elif imagem[i][j] == '0' and imagem[i + 1][j] == '1' and b != 0:
                    if str(b) and '01' not in codificacao:
                        codificacao.append(str(b))
                        codificacao.append('01')
                elif imagem[i][j] == '1' and imagem[i + 1][j] == '0' and c != 0:
                    if str(c) and '10' not in codificacao:
                        codificacao.append(str(c))
                        codificacao.append('10')
                elif imagem[i][j] == '1' and imagem[i + 1][j] == '1' and d != 0:
                    if str(d) and '11' not in codificacao:
                        codificacao.append(str(d))
                        codificacao.append('11')
    return codificacao


def decodificar(largura, altura, codificacao):

    return imagem


def carregar_imagem_codificada(nome_do_arquivo):
    return largura, altura, codificacao


def carregar_imagem_decodificada(nome_do_arquivo):
    return largura, altura, imagem


def escrever_imagem_codificada(largura, altura, codificacao, nome_do_arquivo):
    pass


def escrever_imagem_decodificada(largura, altura, imagem, nome_do_arquivo):
    pass

def codificar(imagem):
        """le uma matriz de 0 e 1 e codifica para run-length"""
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
                if imagem[i][j] == '0' and imagem[i + 1][j] == '0':
                    a += 1
                elif imagem[i][j] == '0' and imagem[i + 1][j] == '1':
                    b += 1
                elif imagem[i][j] == '1' and imagem[i + 1][j] == '0':
                    c += 1
                elif imagem[i][j] == '1' and imagem[i + 1][j] == '1':
                    d += 1
    if a != 0:
        codificacao.append(str(a))
        codificacao.append('00')
    if b != 0:
        codificacao.append(str(b))
        codificacao.append('01')
    if c != 0:
        codificacao.append(str(c))
        codificacao.append('10')
    if d != 0:
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

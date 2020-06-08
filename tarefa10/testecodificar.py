def codificar(imagem):#comecar com a matriz para run-length
    """le uma matriz de 0 e 1 e codifica para run-lenght"""
    codificacao = []
    tipo_arquivo = 'P1C'
    codificacao.append(tipo_arquivo)
    altura = 0
    largura = 0
    L0 = []
    L = []
    for l in imagem:
        altura += 1
    for a in l:
        largura += 1
    L0.append(largura)
    L0.append(altura)
    codificacao.append(L0)#ate aqui ok!
    k = 0
    for _ in imagem:#vercomo professor fez na aula
        for b in imagem[]:
            if a in imagem[]
    return codificacao

def main():
    imagem = [
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['1', '1', '1', '1', '0', '0', '0', '0'],
        ['1', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '1', '1', '1', '1', '1', '1', '1'],
    ]
    codificacao = codificar(imagem)
    print(codificacao)

main()

def codificar(largura,altura,imagem):
    codificacao = []
    codificacao.append('P1C')
    codificacao.append(largura)
    codificacao.append(altura)
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

def decodificar(largura, altura, codificacao):
    imagem = []
    m = int(altura)
    n = int(largura)
    for _ in range(m):
        l = []
        imagem.append(l)
    for i in range(len(imagem)):
        for k in range(3, len(codificacao)):
            if i % 2 == 0:
                a = codificacao[k]
                if a != '00' and a != '01' and a != '10' and a != '11':
                    a = int(a)
                    for _ in range(a):
                        if len(imagem[i]) < n:
                            imagem[i].append(codificacao[k + 1][0])
                            imagem[i + 1].append(codificacao[k + 1][1])
                        elif len(imagem[i]) == n:
                            if i != len(imagem) - 2:
                                i += 2
                                if len(imagem[i]) < n:
                                    imagem[i].append(codificacao[k + 1][0])
                                    imagem[i + 1].append(codificacao[k + 1][1])
                                elif len(imagem[i]) == n:
                                    if i != len(imagem) - 2:
                                        i += 2
                                        continue
                                    else:
                                        if len(imagem[i]) < n:
                                            imagem[i].append(codificacao[k + 1][0])
                                            imagem[i + 1].append(codificacao[k + 1][1])
    return imagem

def carregar_imagem_codificada(nome_do_arquivo):
    """recebe  o arquivo no formato P1C"""
    with open(nome_do_arquivo) as arquivo: #percorre as linhas do arquivo como se elas fossem strings numa lista
        L = []
        for line in arquivo:
            Ls = line.strip()
            L.append(Ls)
    largura = L[1][0]
    altura = ' '
    for i in range(1, len(L[1])): 
        if L[1][i] != ' ':
            largura += L[1][i]
        else:
            break
    for j in range(1, len(L[1])):
        if L[1][j] == ' ':
            j += 1
            if L[1][j] != ' ':
                altura += L[1][j]
                if j == len(L[1]) - 1:
                    break #largura e altura deu certo
    largura = int(largura)
    altura = int(altura)
    codificacao = []
    codificacao.append(L[2].strip())
    return largura, altura, codificacao

def carregar_imagem_decodificada(nome_do_arquivo):
    """Essa função recebe o nome de um arquivo de imagem no formato PBM (veja os exemplos de arquivos .pbm fornecidos em algum editor de texto) e devolver as informações:
dois inteiros: largura e altura da imagem
uma matriz de inteiros 0 ou 1: que correspondem ao pixels da imagem."""
    with open(nome_do_arquivo) as arquivo: #percorre as linhas do arquivo como se elas fossem strings numa lista
        L = []
        for line in arquivo:
            Ls = line.strip()
            L.append(Ls)
    imagem = []
    for i in range(2, len(L)):
        imagem.append(list(L[i].strip())) #devolve a matriz com os zeros e uns separados
    largura = len(imagem[0])
    altura = len(imagem)
    return largura, altura, imagem


def escrever_imagem_codificada(largura, altura, codificacao, nome_do_arquivo):
    """cria um arquivo chamado nome_do_arquivo
    escreve dos dados do arquivo por linhas
    tipo
    largura altura
    codificacao"""
    with open(nome_do_arquivo, "w") as arquivo:
        arquivo.write('P1C')
        arquivo.write(f'{largura} {altura}')
        for a in codificacao:
            a = str(a)
            arquivo.write(a)

def escrever_imagem_decodificada(largura, altura, imagem, nome_do_arquivo):
    with open(nome_do_arquivo, "w") as arquivo:
        arquivo.write('P1')
        arquivo.write(f'{largura} {altura}')
        for linha0 in imagem:
            linha0 = linha0.strip()
            linha = linha0 + "\n"
            arquivo.write(linha)

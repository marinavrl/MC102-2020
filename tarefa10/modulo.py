def codificar(largura,altura,imagem):
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
                a = 1   #comeca a contar de novo
    return codificacao

def decodificar(largura, altura, codificacao):
    imagem = []
    m = int(altura)
    n = int(largura)
    for _ in range(m):
        l = []
        imagem.append(l)
    for i in range(len(imagem)):
        for k in range(len(codificacao)):
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
            Ls = line.strip().split()
            L.append(Ls)
    largura_altura = L[1]
    largura = largura_altura[0]
    altura = largura_altura[1]
    largura = int(largura)
    altura = int(altura)
    codificacao = L[2]
    return largura, altura, codificacao
#mudar decodificar para a o q era antes 

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
        arquivo.write('P1C\n')
        arquivo.write(f'{largura} {altura}\n')
        for a in codificacao:
            a = str(a)
            arquivo.write(f'{a} ')

def escrever_imagem_decodificada(largura, altura, imagem, nome_do_arquivo):
    with open(nome_do_arquivo, "w") as arquivo:
        arquivo.write('P1\n')
        arquivo.write(f'{largura} {altura}\n')
        linha0 = ''
        linha = ''
        for i in range(len(imagem)):      
            for j in range(len(imagem[0])):
                linha0 += imagem[i][j]
            linha = linha0 + '\n'
            linha0 = '' 
            arquivo.write(linha)
    #arquivo.write(linha)
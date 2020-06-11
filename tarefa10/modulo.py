def codificar(largura,altura,imagem):
    #botar o P1C segundo os casos de teste
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


def carregar_imagem_codificada(nome_do_arquivo):#o objetivo da tarefa eh completar
    #olhando os casos de teste voce vai entender o que tem que fazer usando open etc
    #ASSISTE A AULA DE ARQUIVOS!!!!
    #o teste da ferramenta online funciona!!! olhar no site
    return largura, altura, codificacao


def carregar_imagem_decodificada(nome_do_arquivo):
    """Essa função recebe o nome de um arquivo de imagem no formato PBM (veja os exemplos de arquivos .pbm fornecidos em algum editor de texto) e devolver as informações:
dois inteiros: largura e altura da imagem
uma matriz de inteiros 0 ou 1: que correspondem ao pixels da imagem

A primeira coisa que vc tem que fazer é entender o que cada função deve fazer."""
#a maior duvida eh a ordem dos bits e se os padroes se repetem, como fazer com que faca sentido
#olhar os casos de teste nos "testes"
    return largura, altura, imagem


def escrever_imagem_codificada(largura, altura, codificacao, nome_do_arquivo):
    pass


def escrever_imagem_decodificada(largura, altura, imagem, nome_do_arquivo):
    pass

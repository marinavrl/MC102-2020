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

from modulo import * #pega todas as funcoes do modulo
# conectar a carregar_imagem_codificada com a decodificar
""" 1) Carregar a imagem codificada.. ok
    2) Decodificar para a matriz...ok
    3) ... mexer para destacar as bordas
    4) verificar se codificar faz sentido pra saida
    ...
    """
def destacar_bordas(largura, altura, imagem):
    """ 1) Adicionar altura listas vazias a  nova_imagem
        2)ver largura e adicionar  largura '0's em cada lista da nova_imagem
        3) percorrer cada item de imagem
        4) adicionar ao item correspondente em nova_imagem se for igual a zero e se estiver na ultima linha
        da matriz e se for o primeiro ou ultimo bit de cada linha 
        caso contrario, adicionar zero     """
    nova_imagem = []
    for m in range(altura):
        l = []
        nova_imagem.append(l)
        for n in range(largura):
            nova_imagem[m].append('0')
    for i in range(len(imagem)):
        for j in range(len(imagem[0])):
            if imagem[i][j] == '0':
                nova_imagem[i][j] = '0'
            elif imagem[i][j] == '1' and imagem[i-1][j] == '0':
                nova_imagem[i][j] = '1'
            elif imagem[i][j] == '1' and j == 0:
                nova_imagem[i][j] = '1'
            elif imagem[i][j] == '1' and imagem[i+1][j] == '0':
                nova_imagem[i][j] = '1'
            elif imagem[i][j] == '1' and j == len(imagem[0])-1:
                nova_imagem[i][j] = '1'
            elif imagem[i][j] == '1' and imagem[i-1][j-1] == '0':
                nova_imagem[i][j] == '1'
            elif imagem[i][j] == '1' and imagem[i-1][j+1] == '0':
                nova_imagem[i][j] == '1'
            elif imagem[i][j] == '1' and imagem[i+1][j-1] == '0':
                nova_imagem[i][j] == '1'
            elif imagem[i][j] == '1' and imagem[i+1][j+1] == '0':
                nova_imagem[i][j] == '1'
            elif imagem[i][j] == '1' and imagem[i-1][j-1] == '1' and imagem[i-1][j] == '1' and imagem[i-1][j+1] == '1' and imagem[i][j-1] == '1' and imagem[i][j+1] == '1' and imagem[i+1][j-1] == '1' and imagem[i+1][j] == '1' and imagem[i+1][j+1] == '1':
                nova_imagem[i][j] == '0'
    return nova_imagem
def main():

    arquivo_entrada = input()
    arquivo_saida = input()

    largura, altura, codificacao = carregar_imagem_codificada(arquivo_entrada)
    imagem = decodificar(largura, altura, codificacao)
    nova_imagem = destacar_bordas(largura, altura, imagem)

    codificacao = codificar(largura, altura, nova_imagem)
    escrever_imagem_codificada(largura, altura, codificacao, arquivo_saida)


if __name__ == '__main__':
    main()

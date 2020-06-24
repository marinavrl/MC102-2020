from modulo import * #pega todas as funcoes do modulo
# conectar a carregar_imagem_codificada com a decodificar
""" 1) Carregar a imagem codificada.. ok
    2) Decodificar para a matriz...ok
    3) ... mexer para destacar as bordas
    4) verificar se codificar faz sentido pra saida
    ...
    """
def destacar_bordas(largura, altura, imagem):
    """imagem eh matriz de bits
    largura e altura delimitam"""


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

def carregar_imagem_codificada(nome_do_arquivo):
    """Ler um arquivo de texto e carregar os dados nas
    variáveis. Olhar o exemplo de código fornecido 
    que tem os parâmetros e a saída e completar as 
    funções."""
    #algoritmo
    """ 1) ler arquivo em formato pbm
        2) separa cada linha do arquivo num elemento
        de uma lista.
        3) pega o segundo elemento que sera a string
        contendo a largura e altura separadas por 
        espaco.
        4) atribui ele a uma variavel
        5) percorre essa variavel e identifica o
        primeiro numero e atribui a largura
        6) ao identificar o segundo numero, atribuie a largura
        7)a partir da terceira linha/elemento da lista, 
        fazer para a matriz imagem
         """
    with open(nome_do_arquivo) as arquivo:
        L = []
        for line in arquivo:
            Ls = line.strip()
            L.append(Ls)
    return L       # a duvida eh como acessar os arquivos de teste

def main():
    L = carregar_imagem_codificada("jota.pbm") #nao da pra testar com os arquivos
    print(L)

main()





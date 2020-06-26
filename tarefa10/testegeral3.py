def testar_c_i_c(nome_do_arquivo):
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

def main():
    largura, altura, codificacao = testar_c_i_c("testes/toy.p1c") #codificacao depois
    print(f'{largura} and {altura} and {codificacao}')

main()

#matriz.append(list(linha.strip()))
#largura_altura equivale a a linha de arquivo
"""talvez baste soh pegar o arquivo a partir da terceira linha e fazer a funcao de codificacao"""
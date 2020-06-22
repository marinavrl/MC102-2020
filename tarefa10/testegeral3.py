def testar_c_i_c(nome_do_arquivo):
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
    codificacao = []
    codificacao.append(L[2].strip())
    return largura, altura, codificacao

def main():
    largura, altura, codificacao = testar_c_i_c("testes/feep.p1c") #codificacao depois
    print(f'{largura} and {altura} and {codificacao}')

main()

#matriz.append(list(linha.strip()))
#largura_altura equivale a a linha de arquivo
"""talvez baste soh pegar o arquivo a partir da terceira linha e fazer a funcao de codificacao"""
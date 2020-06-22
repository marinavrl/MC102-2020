def striplista(largura_altura):
    largura = largura_altura[0]
    altura = ' '
    for i  in range(1, len(largura_altura)):
        if largura_altura[i] != ' ':
            largura += largura_altura[i]
        else:
            break
    for i in range(1, len(largura_altura)):
        if largura_altura[i] == ' ':
            altura = largura_altura[len(largura_altura)-i]
#corrigir
        else:
            altura += largura_altura[len(largura_altura)-i-1]
    return largura, altura

def main():
    largura_altura = "12 10"
    (largura, altura) = striplista(largura_altura)
    print(f'{largura} and {altura}')

main()

#matriz.append(list(linha.strip()))
#largura_altura equivale a a linha de arquivo
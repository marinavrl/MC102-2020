def listar_palavras_arquivo(texto, stopwords):
    with open(texto, 'r', encoding='utf-8') as arquivo:
        tirar_pontos = ''
        L = ''
        for line in arquivo:
            L = line.strip().lower() + " "
            for letra in L:
                if not (ord(letra) in range(46,65) or (ord(letra) in range(33,45))):
                    tirar_pontos+=letra
            L0 = tirar_pontos.split()
    for _ in L0:
        for palavra0 in L0:
            if palavra0 in stopwords:
                L0.remove(palavra0)
    return L0

def contar_frequencia(L0):
    palavras_freq = []
    for i in range(len(L0)):
        a = 0
        for j in range(len(L0)):
            if L0[i] == L0[j]:
                a+=1
                palavra = L0[i]
            else:
                continue
        freq = a
        tupla = (palavra, freq)
        if tupla in palavras_freq:
            continue
        else:
            palavras_freq.append(tupla)
    n = len(palavras_freq)
    palavras_freq.sort()
    for _ in range(n-1):
        for i in range(n-1):
            if palavras_freq[i+1][1] > palavras_freq[i][1]:
                aux = palavras_freq[i]
                palavras_freq[i] = palavras_freq[i+1]
                palavras_freq[i+1] = aux
    return palavras_freq

def quartil_lista(palavras_freq):
    """ Todas as palavras que tem freq maior ou igual a cinco e organiza em ordem decrescente,
     depois pega o primeiro quarto de palavras, o quartil vai ser a ultima desse quarto"""
    lista = []
    for i in range(len(palavras_freq)):
        if palavras_freq[i][1] >= 5:
            lista.append(palavras_freq[i])
    quarto = []
    for i in range(len(lista)//4):
        quarto.append(lista[i])
    a = 0
    lista2 = []
    lista4 = []
    for j in range(len(lista)):
        if lista[j][1] >= quarto[len(quarto)-1][1]:
            a+=1
            lista4.append(lista[j][0])
        lista2.append(lista[j][0])
    lista1 = []
    for b in lista2:
        if b not in lista4:
            lista1.append(b)
    return lista1, lista2, a


def main():
    texto = input()
    stopwords = input().split()
    L0 = listar_palavras_arquivo(texto, stopwords)
    palavras_freq = contar_frequencia(L0)
    lista1, lista2, a = quartil_lista(palavras_freq)
    print(' '.join(lista2[0:3]))
    print(a)
    print(' '.join(lista1[0:3]))

main()
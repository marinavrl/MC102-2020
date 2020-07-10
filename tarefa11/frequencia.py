def listar_palavras_arquivo(texto):#stopwords
    with open(texto, 'r', encoding='utf-8') as arquivo:
        tirar_pontos = ''
        L = ''
        for line in arquivo:
            L = line.strip().lower() + " "
            for letra in L:
                if not (ord(letra) in range(46,65) or (ord(letra) in range(33,45))):
                    tirar_pontos+=letra
            L0 = tirar_pontos.split()
    #for _ in L0:
     #   for palavra0 in L0:
      #      if palavra0 in stopwords:
       #         L0.remove(palavra0)
    return L0

def contar_frequencia(L0, stopwords): #count
    palavras_freq = []
    for palavra in L0:
        if palavra not in stopwords:
            freq = L0.count(palavra)
            tupla = (palavra, freq)
            if tupla not in palavras_freq:
                palavras_freq.append(tupla)
    palavras_freq.sort()
    palavras_freq.sort(key=lambda val: val[1], reverse=True)
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
    L0 = listar_palavras_arquivo(texto)
    palavras_freq = contar_frequencia(L0, stopwords)
    lista1, lista2, a = quartil_lista(palavras_freq)
    print(' '.join(lista2[0:3]))
    print(a)
    print(' '.join(lista1[0:3]))

main()
def listar_palavras_arquivo(texto):
    with open(texto) as arquivo:
        L = []
        for line in arquivo:
            Ls = line.strip().split()
            L.append(Ls)
    for a in L:
        if a == []:
            L.remove(a)
    L0 = []
    for i in range(len(L)):
        for b in L[i]:
            L0.append(b)
    return L0

def tirar_stopwords(L0, stopwords): # recebe lista de stopwords da entrada, ver entrada do problema
    """ identifica as stop words em L0 e remove"""
    for _ in L0:
        for palavra0 in L0:
            for palavra1 in stopwords:
                if palavra0 == palavra1:
                    L0.remove(palavra0)
    return L0

def editar_L0(L0):
    """ tira as coisas que atrapalham a contagem de palavras que se repetem muito(Pontuacoes e aspas) """
    for i in range(len(L0)):
        if L0[i][0:2] == "''" and L0[i][len(L0[i])-2:len(L0[i])] == "''":
            L0[i] = L0[i][2:len(L0[i])-1]
        elif L0[i][0:2] == "''":
            L0[i] = L0[i][2:len(L0[i])]
        elif L0[i][len(L0[i])-2:len(L0[i])] == "''":
            L0[i] = L0[i][0:len(L0[i])-2]
        elif L0[i][len(L0[i])-1] == ',' or L0[i][len(L0[i])-1] == '.':
            L0[i] = L0[i][0:len(L0[i])-1]
    return L0

def contar_frequencia(L0):
    """ Recebe a lista sem stopwords e conta a freq de cada palavra e associa a freq a palavra pelas tuplas"""
    #tupla = (palavra, frequencia)
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
    return palavras_freq 
#esta contando corretamente

def ordenar_freq_decresc(palavras_freq):
    """ordena nela as palavras da mais a menos freq  """
    n = len(palavras_freq)
    for _ in range(n-1):
        for i in range(n-1):
            if palavras_freq[i+1][1] > palavras_freq[i][1]:
                aux = palavras_freq[i]
                palavras_freq[i] = palavras_freq[i+1]
                palavras_freq[i+1] = aux
    return palavras_freq
#ordena ok

def quartil_lista(palavras_freq):
    """ Todas as palavras que tem freq maior ou igual a cinco e organiza em ordem decrescente,
     depois pega o primeiro quarto de palavras, o quartil vai ser a ultima desse quarto"""
    lista = []
    for i in range(len(palavras_freq)):
        if palavras_freq[i][1] >= 5:
            lista.append(palavras_freq[i][0])
    return lista

def quartil_palavras(lista):
    quarto = []
    a = 0
    for i in range(len(lista)//4):
        quarto.append(lista[i])
        a+=1
    return quarto, a

def quartil_resto(lista, quarto):
    lista1 = []
    for b in lista:
        for c in quarto:
            if b!=c:
                lista1.append(b)
    return lista1


def main():
    texto = input() #recebe o nome do arquivo//// testes/texto1.in
    stopwords = input().split() #lista com as stopwords //// a à ainda ao aos aqui as às assim cada clara claro com como da das de demais desta destes deve do dois dos e é em entanto entre estas existem geral já longo mais maneira melhor mesmo na não nas neste no nos nossa novas novo nunca o os ou outras outro para pela pelo pelos por qual quanto que se sempre seu sobre sua suas talvez todas todavia todo todos tudo um uma
    L0 = listar_palavras_arquivo(texto)
    L0 = tirar_stopwords(L0, stopwords)
    L0 = editar_L0(L0)
    palavras_freq = contar_frequencia(L0)
    palavras_freq = ordenar_freq_decresc(palavras_freq)
    lista = quartil_lista(palavras_freq)
    print(' '.join(lista[0:3]))
    (quarto, a) = quartil_palavras(lista)
    print(a)
    lista1 = quartil_resto(lista, quarto)
    print(' '.join(lista1[0:3]))

main()

#conjunto = set(L0)
#print(conjunto)

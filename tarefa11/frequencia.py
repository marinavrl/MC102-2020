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

def main():
    texto = input() #recebe o nome do arquivo
    #stopwords = input().split() #lista com as stopwords
    #L0 = listar_palavras_arquivo(texto)
    #L0 = tirar_stopwords(L0, stopwords)
    #L0 = editar_L0(L0)
    #palavras_freq = contar_frequencia(L0)
    #palavras_freq = ordenar_freq_decresc(palavras_freq)
    #verquartil
    print(L0)

main()

#conjunto = set(L0)
#print(conjunto)

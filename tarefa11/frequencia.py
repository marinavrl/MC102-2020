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
#conjunto = set(L0)
#print(conjunto)
def tirar_stopwords(L0, stopwords): # recebe lista de stopwords da entrada, ver entrada do problema
    """ identifica as stop words em L0 e remove"""
    for _ in L0:
        for palavra0 in L0:
            for palavra1 in stopwords:
                if palavra0 == palavra1:
                    L0.remove(palavra0)
    return L0
    pass
def contar_frequencia(L0):
    """ Recebe a lista sem stopwords e conta a freq de cada palavra e associa a freq a palavra pelo dict(tupla)"""
    #tupla = (palavra, frequencia)
    pass

def main():
    texto = input() #recebe o nome do arquivo
    #stopwords = input().split() #lista com as stopwords
    #L0 = tirar_stopwords(L0, stopwords)
    L0 = listar_palavras_arquivo(texto)
    print(L0)

main()

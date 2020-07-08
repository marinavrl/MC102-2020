def listar_palavras_arquivo(texto):
    with open(texto, 'r', encoding='utf-8') as arquivo:
        L = []
        for line in arquivo:
            Ls = line.strip().lower().split()
            L.append(Ls)
    for a in L:
        if a == []:
            L.remove(a)
    L0 = []
    for i in range(len(L)):
        for b in L[i]:
            L0.append(b)
    return L0, L

def main():
    texto = "testes/texto2.in"
    L0, L = listar_palavras_arquivo(texto)
    print(L0)

main()
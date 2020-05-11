def bubble_sort(L):
    n = len(L)
    for _ in range(n-1):
        for i in range(n - 1):
            if L[i] > L[i + 1]:
                aux = L[i]
                L[i] = L[i+1]
                L[i+1] = aux

def organizar(L):
    i = 0
    freq = []
    lista = []
    for a in L:
        if a not in lista:
            k=a 
            lista.append(a)
            for a in L:
                if k == a:
                    i += 1
            freq.append(i)
            i = 0
    return lista,freq

def ordem_crescente(lista, freq):    
    for _ in range(len(lista) - 1):
        for c in range(len(lista) - 1):
            if freq[c] > freq[c + 1]:
                k = freq[c + 1]
                freq[c + 1] = freq[c]
                freq[c] = k
                k0 = lista[c + 1]
                lista[c + 1] = lista[c]
                lista[c] = k0
            elif freq[c] == freq[c + 1]:
                if lista[c] > lista[c + 1]:
                    k0 = lista[c + 1]
                    lista[c + 1] = lista[c]
                    lista[c] = k0
    return lista                     

def main():
    L = input().split()
    bubble_sort(L)
    lista, freq = organizar(L)
    ordem_crescente(lista, freq)
    print(' '.join(lista))

main()



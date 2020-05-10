def bubble_sort(L):
    n = len(L)
    for _ in range(n-1):
        for i in range(n - 1):
            if L[i] > L[i + 1]:
                aux = L[i]
                L[i] = L[i+1]
                L[i+1] = aux

def organizar(L):
    i = 0 #contagem da freq de cada numero
    freq = [] #vai ser a lista de freq
    lista = [] #vai ser uma lista com um representante de cada numero da lista original
    for a in L: #vai percorrer cada elemento da lista original
        if a not in lista: #caso o numero apontado na lista original nao esteja em listinha
            k=a #define uma cte com esse numero
            lista.append(a) #e o acrescentei em listinha
            for a in L: #percorre a lista de novo, procurando o numero que foi adicionado a listinha
                if k == a: #se o numero apontado pelo 'for' for igual a esse
                    i += 1 #adiciono 1 a frequencia dele
            freq.append(i) #no final, adiciono a frequencia desse numero a lista de freq
            i = 0 #zero a contagem para o prox numero
    return lista,freq #e no final retorno ambos

#relacionar freq a listinha e devolver a saida na ordem crescente de freq
def ordem_crescente(lista, freq):
    """Ordena uma lista
    lista<-- lista que sera ordenada
    freq<-- jeito de ordenar a lista"""
    for c in range(len(lista) - 1):
        if freq[c] > freq[c + 1]: #freq
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

L = input().split() #aqui peco o input dos numeros
bubble_sort(L)
organizar(L) #pego os dois resultados da funcao e atribuo as variaveis listinha e frequencia
ordem_crescente(lista, freq)
print(lista) #agora mostro na tela os dois
#OBS:a atribuicao dos resultados da funcao na linha 17 esta na sequencia em que os valores foram retornados
# pela funcao. Nao precisa usar os parenteses, eles indicam que aquilo eh uma tupla 



#funcao dentro de funcao
#funcoes secundarias
def f(L):
    l0 = []
    for b in L:
        n = int(b)
        m = 0
        for k in range(2,n + 1):
            if n % k == 0:
                m += 1
        if m == 1:
            l0.append(b)
        else:
            l0.append(0)
    return l0

def g(l0):
    for j in range(len(l0)):
        l0[j] = l0[j]**2
    return l0

def h(l0):
    soma = 0
    for a in l0:
        soma += a
    return soma
#se a sequencia for vazia ou nao tiver numeros primos, saida eh 0

#funcao filtra
#filtrar os numeros primos da lista
def filtra(f, lista):
#retorna lista1. Aplica uma funcao f a cada elemento de uma lista e retorna os elementos para os quais a funcao retorna true
    lista1 = []
    l0 = f(lista)
    for c in l0:
        lista1.append(c)
    return lista1

#funcao mapeia
#eleva esses numeros primos ao quadrado
def mapeia(g, lista1):
#retorna lista2. Aplica uma funcao g a cada elemento de uma lista e devolve uma nova lista
    g(lista1)
    lista2 = lista1
    return lista2

#funcao reduz
#soma esses quadrados
def reduz(h, lista2):
#retorna lista3. Acumula os valores de uma lista de forma que produz um único valor por meio de uma funcao que recebe dois valores e retorna um
    soma = h(lista2)
    return soma

def main():
    lista = input().split()
    lista1 = filtra(f, lista)
    lista2 = mapeia(g, lista1)
    soma = reduz(h, lista2)
    print(f'{soma}')

main()
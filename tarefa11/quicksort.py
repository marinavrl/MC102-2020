import random

def _quicksort(L):
    #print('Quicksort, Parameter L:', L) --- visualizacao
    if len(L) <= 1:
        return L
    menor, igual, maior = [], [], []
    pivot = random.choice(L)

    for d in L:
        if d < pivot:
            menor.append(d)
        elif d == pivot:
            igual.append(d)
        else:
            maior.append(d)

    #print('result: ', _quicksort(menor) + igual + _quicksort(maior))--- visualizacao
    return _quicksort(menor) + igual + _quicksort(maior)

def quicksort(L, crescente=True):
    if crescente:
        return _quicksort(L)
    else:
        return _quicksort(L)[::-1]

def main():
    L = [3, 2, -1, 9, 17, 4, 1, 0]
    L = quicksort(L, crescente=False)
    print(L)

main()




def bubble_sort(L):
    n = len(L)
    for _ in range(n - 1):
        for i in range(n - 1):
            if L[i] > L[i + 1]:
                aux = L[i]
                L[i] = L[i+1]
                L[i+1] = aux

def main():
    L = [3, 2, 1]
    bubble_sort(L)
    print(L)

main()
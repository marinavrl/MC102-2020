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
        l0[j] = int(l0[j])
        l0[j] = l0[j]**2
    return l0

def h(l0):
    soma = 0
    for a in l0:
        soma += a
    return soma

def main():
    L = input().split()
    l0 = f(L)
    g(l0)
    soma = h(l0)
    print(f'{soma}')

main()
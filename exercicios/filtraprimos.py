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


def main():
    L = input().split()
    l0 = f(L)
    print(' '.join(l0))

main()

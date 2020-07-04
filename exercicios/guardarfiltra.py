def f(L):
    retorno = True
    while retorno:
        for b in L:
            n = int(b)
            m = 0
            for k in range(2,n + 1):
                if n % k == 0:
                    m += 1
            if m == 1:
                retorno = True
            else:
                retorno = False

        return retorno


def main():
    L = input().split()
    retorno = f(L)
    print(f'{retorno}')

main()

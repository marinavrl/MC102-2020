def f(L):
    """ identifica os primos e retorna True se forem e False se nao"""
    for b in L:
        n = int(b)
        m = 0
        for k in range(2,n + 1):
            if n % k == 0:
                m += 1
        if m == 1:
            return True
            print(f'{b} eh primo')
        else:
            return False
            print(f'{b} nao eh primo')

def filtra(L, f):
    """ aplica f aos elementos de uma lista de devolve aqueles para os quais o retorno eh True"""
    l0 = []
    for a in L:
        if f:
            l0.append(a)
        else:
            l0.append(0)
    return l0

def main():
    L = ['2', '3', '45', '5', '6', '7']
    l0 = filtra(L, f)
    print(l0)

main()

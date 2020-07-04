def printar_repetidos(L):
    l = []
    for _ in L:
        for a in L:
            if a in l:
                continue
            else:
                for b in L:
                    if a == b:
                        l.append(a)
                        break
            break
    return l

def main():
    L = input().split()
    l = printar_repetidos(L)
    print(' '.join(l))

main()


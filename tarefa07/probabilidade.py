#lista de inteiros nao negativos
L = input().split()
#l recebe os elementos de L sem repeticao, em ordem crescente, e em ordem crescente de probabilidade
l = []
for b in L:
    if b in l:
        continue
    else:
        l.append(b)
print(' '.join(l))


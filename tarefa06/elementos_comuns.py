# recebe duas listas e devolve uma terceira
A = input().split()
B = input().split()
C = []
# elementos comuns de A e B
for i in A:
    if i in C:
        continue
    for j in B:
        if i == j:
            C.append(i)
            break
print(' '.join(C))

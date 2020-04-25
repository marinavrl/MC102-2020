A = input().split()
B = input().split()
C = []
for i in A:
    for j in B:
        if i == j:
            C.append(i)
print('{C}')            
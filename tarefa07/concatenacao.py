#listas
A = input().split()
B = input().split()
C = []
#soma dos elementos de A e B em C
if len(A) == len(B):
    for i in range(len(A)):
            C.append(A[i] + B[i])
print(' '.join(C))
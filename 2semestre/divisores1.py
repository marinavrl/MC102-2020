"""recebe um inteiro e devolve todos os divisores
positivos, um por linha"""

N = int(input())
numero_d = 0

for d in range(1, N + 1):
    if N % d == 0 :
        print(d)
        numero_d += 1
print(numero_d)


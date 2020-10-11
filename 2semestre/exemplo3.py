"""a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if (a <= b) and (a <= c):
    print(a)
elif (b <= c):
    print(b)
else:
    print(c)"""

n = int(input("Digite um número inteiro positivo: "))
potencia = 1
for i in range(n):
 potencia = potencia * 2
print(potencia)
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if (a <= b) and (a <= c):
    print(a)
elif (b <= c):
    print(b)
else:
    print(c)
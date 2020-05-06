# lê uma string com três partes
a, b, c = input().split()

# converte strings em números
a = float(a)
b = float(b)
c = float(c)

# termine esse programa aqui...
if b > a and b > c:
    a, b = b, a
if c > a and c > a:
    a, c = c, a

pitagoras = c**2 + b**2 == a**2
cosseno1 = c**2 + b**2 < a**2

if pitagoras and a != 0 and b != 0 and c != 0:
    print("retângulo")
elif a < b + c and cosseno1 and a != 0 and b != 0 and c != 0:
    print("obtusângulo")
elif a < b + c and a != 0 and b != 0 and c != 0:
    print("acutângulo")
else:
    print("não forma triângulo")



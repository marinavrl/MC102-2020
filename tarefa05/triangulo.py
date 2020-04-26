# lê uma string com três partes
a, b, c = input().split()

# converte strings em números
a = float(a)
b = float(b)
c = float(c)

# termine esse programa aqui...
if c**2 + b**2 == a**2 and a != 0 and b != 0 and c != 0:
    print("retângulo")
elif c**2 + b**2 < a**2 and (c**2 + b**2 - a**2)/2*b*c > -1 and (c**2 + b**2 - a**2)/2*b*c < 0 and a != 0 and b != 0 and c != 0:
    print("obtusângulo")
elif c**2 + b**2 > a**2 and (c**2 + b**2 - a**2)/2*b*c > 0 and (c**2 + b**2 - a**2)/2*b*c < 1 or c == b == a != 0:
    print("acutângulo")
else:
    print("não forma triângulo")


c = float(input())
b = float(input())
a = float(input())
if c**2 + b**2 == a**2:
    print("retângulo")
elif c**2 + b**2 < a**2 and (c**2 + b**2 - a**2)/2*b*c > -1 and (c**2 + b**2 - a**2)/2*b*c < 0:
    print("obtusângulo")
elif c**2 + b**2 > a**2 and (c**2 + b**2 - a**2)/2*b*c > 0 and (c**2 + b**2 - a**2)/2*b*c < 1 or c == b == a:
    print("acutângulo")
else:
    print("não forma triângulo")




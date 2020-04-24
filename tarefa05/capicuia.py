numero = input()
if len(numero) == 1:
    print("sim")
elif len(numero) == 2 and numero[0] == numero[1]:
    print("sim")
elif len(numero) == 3 and numero[0] == numero[2]:
    print("sim")
elif len(numero) == 3 and numero[0] == numero[1] == numero[2]:
    print("sim")
elif len(numero) == 4 and numero[0] == numero[3] and numero[1] == numero[2]:
    print("sim")
elif len(numero) == 4 and numero[0] == numero[1] == numero[2] == numero[3]:
    print("sim")
else:
    print("não")
    
#quantidade de letras num texto
texto = input()
lista0 = list(texto)
lista1 = []
print(lista0)
for l0 in lista0:
    if l0 != ' ' and l0 != ',' and l0 != '.' and l0 != ':' and l0 != ';' and l0 != '-' and l0 != '?':
        lista1.append(l0)
print(lista1)
quantidade = 0
for l1 in lista1:
    quantidade += 1
print(quantidade)





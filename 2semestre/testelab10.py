matriz = []
linha = input()

while linha.isdigit() == False:
    linha = linha.split()
    matriz.append(linha)
    linha = input()
    if linha.isdigit():
        N = int(linha)
        break

print(matriz)
print(N) #matri e N ok


"""
matriz = [['q', 'i', 'a', 'u', 'k', 'r', 't'], 
          ['c', 'p', 'w', 'n', 'z', 's', 't'], 
          ['o', 'k', 'i', 'i', 'i', 'b', 'q'], 
          ['u', 'n', 'i', '*', 'a', 'm', 'p'], 
          ['p', 'c', 'o', 'a', 'o', 'z', 'r'], 
          ['a', 'y', 'z', 'm', 'v', 'v', 'd'], 
          ['c', 'h', 'j', 'p', 'd', 'f', 'u']]
"""
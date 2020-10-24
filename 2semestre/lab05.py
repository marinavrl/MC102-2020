###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Números da Mega-Sena
# Nome: Marina Victória Roncalio de Lima
# RA: 241482
###################################################

"""João sempre entrega no caixa da lotérica suas apostas com os seis números ordenados de maneira crescente.
Os números devem ter paridades alternadas. Ou seja, se o primeiro número for par, o segundo deve ser ímpar,
o terceiro par e assim por diante. Se o primeiro número for ímpar, o segundo deve ser par, o terceiro ímpar 
e assim por diante.
A soma dos 6 números da aposta não pode ser um número múltiplo de 7 ou 13. """

"""Lista com os n2 e outra lista com os n5 de acordo com os numeros fornecidos"""

"""laco para criar as possibilidades de listas a partir da lista de n2 combinada a lista de n5
Se a lista estiver de acordo com as restricoes, devolve como saida a cada laco """

# Leitura de dados
n1 = int(input())
n3 = int(input())
n4 = int(input())
n6 = int(input())

# Impressão dos quatro números fornecidos como entrada

print("Primeiro:", "{:02}".format(n1))
print("Terceiro:", "{:02}".format(n3))
print("Quarto:", "{:02}".format(n4))
print("Sexto:", "{:02}".format(n6))

# Processamento e impressão da lista de possíveis apostas

print("Lista de apostas:")

for a in range(n1 + 1, n3):
    for b in range(n4 + 1, n6):
        n2 = a
        n5 = b
        s = n1 + n2 + n3 + n4 + n5 + n6
        if s % 7 == 0 or s % 13 == 0:
            continue
        if n1 % 2 == 0 and n2 % 2 == 0:
            continue
        elif n1 % 2 != 0 and n2 % 2 != 0:
            continue
        if n4 % 2 == 0 and n5 % 2 == 0:
            continue
        elif n4 % 2 != 0 and n5 % 2 != 0:
            continue
        else:
            print("{:02} - {:02} - {:02} - {:02} - {:02} - {:02}".format(n1, n2, n3, n4, n5, n6))

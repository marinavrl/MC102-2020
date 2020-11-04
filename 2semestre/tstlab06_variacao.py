from copy import deepcopy

lista_compra = [15.06, 34.83, 38.97, 20.58, 19.97, 29.70, 33.71, 39.49, 29.96, 22.94, 22.99, 28.82, 24.23, 39.75, 21.07, 39.44, 29.53, 31.84, 24.59, 39.41, 37.72, 34.67, 30.11, 21.00, 19.87, 23.35, 36.82, 35.07, 28.65, 15.92]

"""lista_venda = [15.06, 34.83, 38.97, 20.58, 19.97, 9.70, 33.71, 39.49, 29.96, 22.94, 22.99, 28.82, 24.23, 39.75, 21.07, 39.44, 29.53, 31.84, 24.59, 39.41, 37.72, 34.67, 30.11, 21.00, 19.87, 23.35, 36.82, 35.07, 28.65, 15.92]"""

lista_venda = deepcopy(lista_compra)

Q = 50000.00

K = 10

lucro_maximo = 0

qtde_acoes1 = 0

valor_compra = lista_compra[0]

valor_venda = lista_venda[0]

dia_compra = 1

dia_venda = 1

for a in lista_compra:
    qtde_acoes0 = int(Q//a)
    if qtde_acoes0 > qtde_acoes1:
        qtde_acoes1 = qtde_acoes0
    for b in lista_venda:
        if lista_compra.index(a) <= lista_venda.index(b) <= lista_compra.index(a) + K:
            lucro_maximo0 = qtde_acoes1 * (b - a)
            if lucro_maximo0 > lucro_maximo:
                lucro_maximo = lucro_maximo0
                valor_compra = a
                valor_venda = b
                dia_compra = lista_compra.index(a) + 1
                dia_venda = lista_venda.index(b) + 1
                qtde_acoes1 = int(Q//valor_compra)
                """print(qtde_acoes1)"""
                lucro_maximo = qtde_acoes1 * (valor_venda - valor_compra)

print(valor_compra, valor_venda)
print(dia_compra, dia_venda)
lucro = float(lucro_maximo)
print(lucro)
qtde_acoes = int(Q//valor_compra)
print(qtde_acoes)

"""from copy import deepcopy
lista_venda = deepcopy(lista_compra) """


        
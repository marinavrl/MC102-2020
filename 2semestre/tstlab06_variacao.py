lista_compra = [15.06, 34.83, 38.97, 20.58, 19.97, 29.70, 33.71, 39.49, 29.96, 22.94, 22.99, 28.82, 24.23, 39.75, 21.07, 39.44, 29.53, 31.84, 24.59, 39.41, 37.72, 34.67, 30.11, 21.00, 19.87, 23.35, 36.82, 35.07, 28.65, 15.92]

lista_venda = [15.06, 34.83, 38.97, 20.58, 19.97, 29.70, 33.71, 39.49, 29.96, 22.94, 22.99, 28.82, 24.23, 39.75, 21.07, 39.44, 29.53, 31.84, 24.59, 39.41, 37.72, 34.67, 30.11, 21.00, 19.87, 23.35, 36.82, 35.07, 28.65, 15.92]

Q = 50000.00

lucro_maximo = 0

qtde_acoes0 = 0

for a in lista_compra:
    qtde_acoes = int(Q//a)
    if qtde_acoes > qtde_acoes0:
        qtde_acoes0 = qtde_acoes
    for b in lista_venda:
        if lista_venda.index(b) <= lista_compra.index(a) + 10:
            lucro_maximo0 = qtde_acoes0 * (b - a)
            if lucro_maximo0 > lucro_maximo:
                lucro_maximo = lucro_maximo0
                valor_compra = a
                valor_venda = b
                dia_compra = lista_compra.index(a) + 1
                dia_venda = lista_venda.index(b) + 1

print(valor_compra, valor_venda)
print(dia_compra, dia_venda)
print(lucro_maximo)
print(qtde_acoes0)


        
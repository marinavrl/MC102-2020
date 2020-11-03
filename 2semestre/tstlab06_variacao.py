lista_compra = [12.55, 13.32, 15.13, 15.65, 16.37, 20.90, 15.21, 13.88, 11.45, 10.50]

lista_venda = [12.55, 13.32, 15.13, 15.65, 16.37, 20.90, 15.21, 13.88, 11.45, 10.50]

Q = 5000.00

K = 2

lucro_maximo = 0

qtde_acoes = 0

for a in lista_compra:
    qtde_acoes0 = int(Q//a)
    if qtde_acoes0 > qtde_acoes: #ta chateando aqui
        qtde_acoes = qtde_acoes0
    for b in lista_venda:
        if lista_compra.index(a) <= lista_venda.index(b) <= lista_compra.index(a) + K:
            lucro_maximo0 = qtde_acoes * (b - a)
            if lucro_maximo0 > lucro_maximo:
                lucro_maximo = lucro_maximo0
                valor_compra = a
                valor_venda = b
                dia_compra = lista_compra.index(a) + 1
                dia_venda = lista_venda.index(b) + 1
                qtde_acoes = int(Q//valor_compra)
                print(qtde_acoes)
                lucro_maximo = qtde_acoes * (valor_venda - valor_compra)

print(valor_compra, valor_venda)
print(dia_compra, dia_venda)
print(lucro_maximo)
print(qtde_acoes)


        
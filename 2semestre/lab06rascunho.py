###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - De Volta para o Passado
# Nome: Marina Victória Roncalio de Lima
# RA: 241482
###################################################

""" Laços aninhados (dois fors) para percorrer a lista
de valores duas vezes/ armazenar em duas listas(comprado e
vendido), armazenar a variação de lucro máximo e ir mudando
essa variavel a cada laco, se for maior do que o valor
anterior"""

from copy import deepcopy

# Leitura de dados

N = int(input())

lista_compra = [] #lista para armazenar os valores diários das ações

for _ in range(N):
    valor_dia = float(input())
    lista_compra.append(valor_dia)

lista_venda = deepcopy(lista_compra)

K = int(input())

Q = float(input())

# Escolha da melhor variação de valores da ação

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
                lucro_maximo = qtde_acoes1 * (valor_venda - valor_compra)

lucro = float(lucro_maximo)
qtde_acoes = int(Q//valor_compra)

# Saída de dados

print('Dia da compra:', dia_compra)
print('Valor de compra: R$', format(valor_compra, '.2f').replace('.', ','))
print('Dia da venda:', dia_venda)
print('Valor de venda: R$', format(valor_venda, '.2f').replace('.', ','))
print('Quantidade de acoes compradas:', qtde_acoes)
print('Lucro: R$', format(lucro, '.2f').replace('.', ','))

#Rascunhos

"""lucro_maximo = 0 #versao atual

qtde_acoes1 = 0

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
                ""print(qtde_acoes1)""
                lucro_maximo = qtde_acoes1 * (valor_venda - valor_compra)

print(valor_compra, valor_venda)
print(dia_compra, dia_venda)
lucro = lucro_maximo
print(lucro)
qtde_acoes = int(Q//valor_compra)
print(qtde_acoes)
 """

"""lucro_maximo = 0 #versao anterior

qtde_acoes = 0

for a in lista_compra:
    qtde_acoes0 = int(Q//a)
    if qtde_acoes0 > qtde_acoes:
        qtde_acoes = qtde_acoes0
    for b in lista_venda:
        if lista_venda.index(b) <= lista_compra.index(a) + K:
            lucro_maximo0 = qtde_acoes * (b - a)
            if lucro_maximo0 > lucro_maximo:
                lucro_maximo = lucro_maximo0
                valor_compra = a
                valor_venda = b
                dia_compra = lista_compra.index(a) + 1
                dia_venda = lista_venda.index(b) + 1

lucro = lucro_maximo """

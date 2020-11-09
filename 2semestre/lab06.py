###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - De Volta para o Passado
# Nome: Marina Victória Roncalio de Lima
# RA: 241482
###################################################

""" Programa para auxiliar na compra e venda das
ações da empresa """

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

#for a in lista_compra:
for i in range(N):
    a = lista_compra[i]
    #if qtde_acoes0 > qtde_acoes1:
        #qtde_acoes1 = qtde_acoes0
#    for b in lista_venda:
    for j in range(i+1, i+K+1):
        #if lista_compra.index(a) <= lista_venda.index(b) <= lista_compra.index(a) + K:
        if j <= N-1:
            b = lista_compra[j]
            qtde_acoes0 = int(Q//a)
            lucro_maximo0 = qtde_acoes0 * (b - a)
            if lucro_maximo0 > lucro_maximo:
                valor_compra = a
                valor_venda = b
                dia_compra = i+1
                dia_venda = j+1
                qtde_acoes1 = qtde_acoes0
                lucro_maximo = lucro_maximo0

lucro = float(lucro_maximo)
qtde_acoes = int(Q//valor_compra)

# Saída de dados

print('Dia da compra:', dia_compra)
print('Valor de compra: R$', format(valor_compra, '.2f').replace('.', ','))
print('Dia da venda:', dia_venda)
print('Valor de venda: R$', format(valor_venda, '.2f').replace('.', ','))
print('Quantidade de acoes compradas:', qtde_acoes)
print('Lucro: R$', format(lucro, '.2f').replace('.', ','))

###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - De Volta para o Passado
# Nome: Marina Victória Roncalio de Lima
# RA: 241482
###################################################

""" Programa para auxiliar na compra e venda das
ações da empresa """

# Leitura de dados

N = int(input())

lista_compra = [] #lista para armazenar os valores diários das ações

for _ in range(N):
    valor_dia = float(input())
    lista_compra.append(valor_dia)

lista_venda = lista_compra

K = int(input())

Q = float(input())

# Escolha da melhor variação de valores da ação

lucro_maximo = 0

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

lucro = lucro_maximo

# Saída de dados

print('Dia da compra:', dia_compra)
print('Valor de compra: R$', format(valor_compra, '.2f').replace('.', ','))
print('Dia da venda:', dia_venda)
print('Valor de venda: R$', format(valor_venda, '.2f').replace('.', ','))
print('Quantidade de acoes compradas:', qtde_acoes)
print('Lucro: R$', format(lucro, '.2f').replace('.', ','))

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

lista_valores = [] #lista para armazenar os valores diários das ações

for _ in range(N):
    valor_dia = float(input())
    lista_valores.append(valor_dia)

K = int(input())

Q = float(input())

#criar lista em ordem crescente de valores

lista_ordenada = sorted(lista_valores)

# Escolha da melhor variação de valores da ação

for a in lista_valores:
    b = lista_ordenada[N-1]
    if a == b:
        valor_venda = a
        i = lista_valores.index(a)
        dia_venda = i + 1
        

if valor_venda != lista_valores[0]: #escolhendo valor compra
    lista_possiveis = sorted(lista_valores[i-K:i+1])
    valor_compra = lista_possiveis[0]

else:
    valor_compra = valor_venda

dia_compra = lista_valores.index(valor_compra) + 1

qtde_acoes = int(Q // valor_compra)

lucro = qtde_acoes * (valor_venda - valor_compra)

# Saída de dados

print('Dia da compra:', dia_compra)
print('Valor de compra: R$', format(valor_compra, '.2f').replace('.', ','))
print('Dia da venda:', dia_venda)
print('Valor de venda: R$', format(valor_venda, '.2f').replace('.', ','))
print('Quantidade de acoes compradas:', qtde_acoes)
print('Lucro: R$', format(lucro, '.2f').replace('.', ','))

###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - De Volta para o Passado
# Nome: Marina Victória Roncalio de Lima
# RA: 241482
###################################################

""" Programa para auxiliar na compra e venda das
ações da empresa """

# Leitura de dados

"""O preço varia por dia, então, se você comprar
num dia em que a ação está mais barata e vender
quando estiver mais cara você obtém um lucro
maior, lembrando do limite de tempo para
vendê-las."""

"""Programa recebe um valor N (número de dias que 
você tem registro do preço das ações); N <= 30 """

"""Nas próximas N linhas, serão lidos os preços
diários das ações """

"""Será lido um valor K (número máximo de dias
permitido entre a compra e a venda da ação) """

"""Ler um valor Q (quantidade de dinheiro que
levará na viagem) """

"""Comprar e vender ações em um único dia, de modo
a ter o maior lucro possível.
As ações são vendidas por inteiro.
Deve-se sempre comprar a maior quantidade possível
de ações."""

"""A saída contem o dia e o valor da compra de
cada ação,  o dia e o valor de venda de cada ação,
a quantidade de ações compradas, e o lucro total
obtido."""


# Escolha da melhor variação de valores da ação




# Saída de dados

print('Dia da compra:', dia_compra)
print('Valor de compra: R$', format(valor_compra, '.2f').replace('.', ','))
print('Dia da venda:', dia_venda)
print('Valor de venda: R$', format(valor_venda, '.2f').replace('.', ','))
print('Quantidade de acoes compradas:', qtde_acoes)
print('Lucro: R$', format(lucro, '.2f').replace('.', ','))
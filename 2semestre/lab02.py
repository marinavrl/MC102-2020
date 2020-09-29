###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Chegada na Estação
# Nome: Marina Victória Roncalio de Lima
# RA: 241482
###################################################

# Leitura de dados
"""x: distância em quilômetros entre as duas estações (valor inteiro).
t: diferença em minutos do tempo de saída dos dois trens (valor inteiro).
v_1: velocidade do trem T1 em km/h (valor real).
v_2: velocidade do trem T2 em km/h (valor real)."""

x = int(input())
t = int(input())
v_1 = float(input())
v_2 = float(input())

# Cálculo dos tempos de viagem

t1 = x/v_1 #tempo que T1 leva para atingir B
t2 = x/v_2 + t/60 #tempo que T2 leva para atingir B

# Impressão da resposta

if t1 < t2:
    print(True)
else:
    print(False)

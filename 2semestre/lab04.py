###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Street Fighter
# Nome: Marina Victória Roncalio de Lima
# RA: 241482
###################################################


# Leitura do hp dos lutadores
HP_RYU = int(input())
HP_KEN = int(input())

# Leitura da sequência de golpes
GOLPES_RYU = 0
GOLPES_KEN = 0
while True:
    golpe = int(input())
    if golpe > 0 : #Ryu
        GOLPES_RYU += 1
        print("RYU APLICOU UM GOLPE:", golpe)
        HP_KEN = HP_KEN - golpe
        if HP_KEN <= 0:
            print("HP RYU =", HP_RYU)
            print("HP KEN =", 0)
            break
        else:
            print("HP RYU =", HP_RYU)
            print("HP KEN =", HP_KEN)
    else: #ken
        GOLPES_KEN += 1
        print("KEN APLICOU UM GOLPE:", golpe*(-1))
        HP_RYU = HP_RYU + golpe
        if HP_RYU <= 0:
            print("HP RYU =", 0)
            print("HP KEN =", HP_KEN)
            break
        else:
            print("HP RYU =", HP_RYU)
            print("HP KEN =", HP_KEN)

# Impressão do vencedor e do número de golpes aplicados

if HP_RYU > 0:
    print("LUTADOR VENCEDOR: RYU")
    print("GOLPES RYU =", GOLPES_RYU)
    print("GOLPES KEN =", GOLPES_KEN)
elif HP_KEN > 0:
    print("LUTADOR VENCEDOR: KEN")
    print("GOLPES RYU =", GOLPES_RYU)
    print("GOLPES KEN =", GOLPES_KEN)
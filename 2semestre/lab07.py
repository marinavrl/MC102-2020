###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Nota de MC102
# Nome: Marina Victória Roncalio de Lima
# RA: 241482
###################################################

# Leitura de dados

N = int(input())

lista = [] #lista de tuplas (nota, peso)

for _ in range(N):
    tupla = ()
    nota = float(input())
    tupla = tupla + tuple([nota])
    lista.append(tupla)

for j in range(len(lista)):
    peso = int(input())
    lista[j] = lista[j] + tuple([peso])

# Cálculo da média ponderada dos laboratórios

soma_ponderada = 0

soma_pesos = 0

for i in range(len(lista)):
    soma_ponderada += lista[i][0]*lista[i][1]
    soma_pesos += lista[i][1]

media = soma_ponderada/soma_pesos

# Verificação da situação do aluno

if media >= 5.0 or media < 2.5:

    print("Media laboratorios:", format(media, ".1f").replace(".", ","))
    
    nota_final = media
    
    if nota_final < 2.5:
        print("Situacao: Reprovado por nota")
        print("Nota final:", format(nota_final, ".1f").replace(".", ","))
    
    elif nota_final >= 5.0:
        print("Situacao: Aprovado por nota")
        print("Nota final:", format(nota_final, ".1f").replace(".", ","))

# Cálculo da nota do exame, caso o aluno tenha ido para o exame

elif media >= 2.5 and media < 5.0:
    M = int(input())

    lista1 = []

    for _ in range(M):
        tupla1 = ()
        lab = int(input())
        tupla1 = tupla1 + tuple([lab])
        lista1.append(tupla1)
    for i in range(len(lista1)):
        nota_lab = float(input())
        lista1[i] = lista1[i] + tuple([nota_lab])

    for i in range(len(lista1)):
        for j in range(len(lista)):
            if lista1[i][0] == lista[j][2]:
                lista1[i] = lista1[i] + tuple([lista[j][1]])

    print("Media laboratorios:", format(media, ".1f").replace(".", ","))

    # Calcular a media_exame

    soma_ponderada1 = 0

    soma_pesos1 = 0

    for i in range(len(lista1)):
        soma_ponderada1 += lista1[i][1]*lista1[i][2]
        soma_pesos1 += lista1[i][2]

    media_exame = soma_ponderada1/soma_pesos1

    nota_final = float(min(5, (media + media_exame) / 2))

    if nota_final == 5.0:
        print("Situacao: Aprovado no exame")
    else:
        print("Situacao: Reprovado no exame")

    print("Nota final:", format(nota_final, ".1f").replace(".", ","))
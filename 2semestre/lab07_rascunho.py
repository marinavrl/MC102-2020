# Leitura de dados

N = int(input())

lista = [] #lista de tuplas (nota, peso)

for _ in range(N):
    tupla = ()
    nota = float(input())
    tupla = tupla + tuple([nota])
    lista.append(tupla)

print(lista)

for j in range(len(lista)):
    peso = int(input())
    lista[j] = lista[j] + tuple([peso])

print(lista)

# Cálculo da média ponderada dos laboratórios

soma_ponderada = 0

soma_pesos = 0

for i in range(len(lista)):
    soma_ponderada += lista[i][0]*lista[i][1]
    soma_pesos += lista[i][1]

media = soma_ponderada/soma_pesos

print(media)

# Verificação da situação do aluno

if media >= 5.0 or media < 2.5:
    
    nota_final = media
    
    if nota_final < 2.5:
        print("Situacao: Reprovado por nota")
        print("Nota final:", format(nota_final, ".1f").replace(".", ","))
    
    elif nota_final >= 5.0:
        print("Situacao: Aprovado por nota")
        print("Nota final:", format(nota_final, ".1f").replace(".", ","))

elif media >= 2.5 and media < 5.0:

#recebe a lista dos labs que irão compor o exame

    M = int(input())

    lista1 = []

    for _ in range(M):
        tupla1 = ()
        lab = int(input())
        tupla1 = tupla1 + tuple([lab])
        lista1.append(tupla1)

#recebe as notas do aluno em cada lab

        nota_final = min{5, (media + media_exame) / 2}
    if nota_final >= 5.0:
        aluno aprovado
    else:
        aluno reprovado"""
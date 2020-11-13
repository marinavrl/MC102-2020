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

print("Media laboratorios:", format(media, ".1f").replace(".", ","))

# Verificação da situação do aluno



# Caso o aluno tenha sido aprovado por nota
print("Situacao: Aprovado por nota")

# Caso o aluno tenha sido reprovado por nota
print("Situacao: Reprovado por nota")




# Cálculo da nota do exame, caso o aluno tenha ido para o exame

# Caso o aluno tenha sido aprovado no exame
print("Situacao: Aprovado no exame")

# Caso o aluno tenha sido repravado no exame
print("Situacao: Reprovado no exame")






# Saída de dados

print("Nota final:", format(nota_final, ".1f").replace(".", ","))
"""recebe a nota em cada uma das tarefas e a presenca dx estudante. 
Devolve "Aprovadx", se cumpriu os criterios, "Reprovadx" caso contrario.

Criterios "Aprovadx":
ter 75% de frequencia
conceito >= C em todas as tarefas"""

#Algoritmo
"""Le as notas de cada tarefa dadas no teclado. Se todas forem diferentes de D, continua para verificar a frequencia.
Caso contrario, x alunx eh reprovadx.
Le a frequencia. Se, do total, 75% ou mais for 'presente', x alunx eh aprovadx. Caso contrario,
o aluno eh reprovadx."""
def ler_notas():
    notas_tarefas = input().split()
    return notas_tarefas

def verificar_notas(notas_tarefas):
    D = 'D'
    k = 0
    for nota in notas_tarefas:
        if nota == D:
            k += 1
        else:
            k += 0
    if k >= 1:
        print("Reprovadx")
    else:
        freq = listar_frequencia()
        i = contar_frequencia(freq)
        verificar_faltou(i, freq)

def listar_frequencia():
    freq = []
    while True:
        try:
            lido = input()
            freq.append(lido)
        except EOFError:
            break
    return freq

def contar_frequencia(freq):
    i = 0
    for p in freq:
        if p == 'faltou':
            i += 1
    return i

def verificar_faltou(i, freq):
    if i > 0.25 * len(freq):
        print("Reprovadx")
    else:
        print("Aprovadx")

def main():
    notas_tarefas = ler_notas()
    verificar_notas(notas_tarefas)

main()






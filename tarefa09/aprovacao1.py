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
    #Devolve uma lista com o nome das tarefas e o conceito recebidos do teclado
    #Digite o nome das tarefas e suas respectivas notas, assim: 'tarefa0 A tarefa1 C'
    notas_tarefas = input().split()
    return notas_tarefas#OK!

def verificar_notas(notas_tarefas):#Recebe uma lista com o nome das tarefas e o conceito, nessa ordem, e verifica se ha alguma nota D.
    #Se houver, reprovadx, caso contrario, continua
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
        freq = listar_frequencia()#OK!
        i = contar_frequencia(freq)#OK!
        verificar_faltou(i, freq)#OK!

def listar_frequencia():
    #Digite as presencas em cada aula e, ao terminar, pressione Control + D
    freq = []
    while True:
        try:
            lido = input()
            freq.append(lido)
        except EOFError:
            break
    return freq#OK!

def contar_frequencia(freq):
    """So eh executada se o aluno obtiver todas as notas acima de D. Recebe a lista de frequencias, 
    na quantidade que o usuario quiser. Conta a quantidade de 'faltou'."""
    i = 0
    for _ in freq:
        for p in freq:
            if p == 'faltou':
                i += 1
        break
    return i #OK!

def verificar_faltou(i, freq):
    """Verifica se i >25% do total de elementos de freq, alunx reprovadx. Caso contrario, alunx aprovadx."""
    if i > 0.25 * len(freq):
        print("Reprovadx")
    else:
        print("Aprovadx")#OK!

def main():
    notas_tarefas = ler_notas()
    verificar_notas(notas_tarefas)

main()






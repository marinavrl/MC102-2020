def verificar_notas(notas_tarefas):#mudar pra True e False
    k = 0
    for nota in notas_tarefas:
        if nota == 'D':
            k += 1
        else:
            k += 0
    if k >= 1: #nem todo if precisa de else
        print("Reprovadx")
    else:
        print("Aprovado")

def main():
    notas_tarefas = ['tarefa0', 'A', 'tarefa1', 'B', 'tarefa2', 'C', 'tarefa3', 'D']
    verificar_notas(notas_tarefas)

main()
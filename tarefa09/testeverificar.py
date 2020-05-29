def verificar_notas_reprovado(notas_tarefas):#mudar pra True e False
    k = 0
    for nota in notas_tarefas:
        if nota == 'D':
            k += 1
        else:
            k += 0
    if k >= 1: #nem todo if precisa de else
        return True
    else:
        return False

def main():
    notas_tarefas = ['tarefa0', 'A', 'tarefa1', 'B', 'tarefa2', 'C', 'tarefa3', 'D']
    if verificar_notas_reprovado(notas_tarefas):
        print("Reprovadx")

main()
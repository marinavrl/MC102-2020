def ler_notas():#Devolve uma lista com o nome das tarefas e o conceito recebidos do teclado
    print("Digite o nome das tarefas e suas respectivas notas, assim: 'tarefa0 A tarefa1 C'.")
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
    if k == 1:
        print("Reprovadx")
    else:
        print("Aprovadx")#OK!

def main():
    notas_tarefas = ler_notas()
    print(notas_tarefas)
    verificar_notas(notas_tarefas)

main()  
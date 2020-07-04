def presenca():
    lista = []
    lido = input()
    fim = 0
    while lido != fim:
        try lista.append(lido)
        except EOFError:
            

    return lista

def main():
    lista = presenca()
    print(lista)

main()

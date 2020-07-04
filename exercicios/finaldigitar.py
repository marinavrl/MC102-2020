def presenca():
    print("Digite as presencas em cada aula e, ao terminar, pressione Control + D")
    freq = []
    while True:
        try:
            lido = input()
            freq.append(lido)
        except EOFError:
            break
    return freq#OK!

def contar_frequencia(freq):
    i = 0
    for _ in freq:
        for p in freq:
            if p == 'faltou':
                i += 1
        break
    return i #OK!

def main():
    freq = presenca()
    i = contar_frequencia(freq)
    print(i)

main()

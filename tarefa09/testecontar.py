def contar_frequencia(freq):
    i = 0
    for p in freq:
        if p == 'faltou':
            i += 1
    return i

def main():
    freq = ['faltou', 'presente', 'presente', 'presente', 'faltou']
    i = contar_frequencia(freq)
    print(i)

main()
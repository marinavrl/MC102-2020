def contar_frequencia(freq):
    i = 0
    for _ in freq: #equivalente ao while True
        for p in freq:
            if p == 'faltou':
                i += 1
        break
    return i

def main():
    freq = ['faltou', 'faltou', 'faltou', 'presente', 'faltou']
    i = contar_frequencia(freq)
    print(i)

main()
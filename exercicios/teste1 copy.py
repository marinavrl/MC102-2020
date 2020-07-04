def contar_frequencia(freq):
    """So eh executada se o aluno obtiver todas as notas acima de D. Recebe a lista de frequencias, 
    na quantidade que o usuario quiser. Conta a quantidade de 'faltou'.
    Se ela for >25% do total, alunx reprovadx. Caso contrario, alunx aprovadx."""
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
        print("Aprovadx") #OK!

def main():
    freq = ['faltou', 'faltou', 'faltou', 'presente', 'presente', 'faltou', 'faltou', 'presente', 'faltou', 'presente']
    i = contar_frequencia(freq)
    verificar_faltou(i, freq)

main()

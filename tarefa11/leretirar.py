def listar_palavras_arquivo(texto):
    with open(texto, 'r', encoding='utf-8') as arquivo:
        tirar_pontos = ''
        L = ''
        for line in arquivo:
            L = line.strip().lower() + " "
            for letra in L:
                if not (ord(letra) in range(46,65) or (ord(letra) in range(33,45))):
                    tirar_pontos+=letra
            L0 = tirar_pontos.split()
    return L, L0

def main():
    texto = "testes/texto1.in"
    L, L0 = listar_palavras_arquivo(texto)
    print(L)
    print(L0)

main()
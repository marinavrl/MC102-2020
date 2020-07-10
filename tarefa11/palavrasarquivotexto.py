def listar_palavras_arquivo(texto, stopwords):
    with open(texto, 'r', encoding='utf-8') as arquivo:
        tirar_pontos = ''
        L = ''
        for line in arquivo:
            L = line.strip().lower() + " "
            for letra in L:
                if not (ord(letra) in range(46,65) or (ord(letra) in range(33,45))):
                    tirar_pontos+=letra
            L0 = tirar_pontos.split()
    for _ in L0:
        for palavra0 in L0:
            if palavra0 in stopwords:
                L0.remove(palavra0)
    return L0

def main():
    texto = "testes/texto4.in"
    stopwords = input().split() #a à ainda ao aos aqui as às assim cada clara claro com como da das de demais desta destes deve do dois dos e é em entanto entre estas existem geral já longo mais maneira melhor mesmo na não nas neste no nos nossa novas novo nunca o os ou outras outro para pela pelo pelos por qual quanto que se sempre seu sobre sua suas talvez todas todavia todo todos tudo um uma
    L0 = listar_palavras_arquivo(texto, stopwords)
    print(L0)

main()
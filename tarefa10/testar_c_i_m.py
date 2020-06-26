def carregar_imagem_decodificada(nome_do_arquivo): # le do formato p1c
    with open(nome_do_arquivo) as arquivo: #percorre as linhas do arquivo como se elas fossem strings numa lista
        L = []
        for line in arquivo:
            Ls = line.strip()
            L.append(Ls)
    imagem = []
    for i in range(2, len(L)):
        imagem.append(list(L[i].strip())) #devolve a matriz imagem com os zzeros e uns
    largura = len(imagem[0])
    altura = len(imagem)
    return largura, altura, imagem
    
 

def main():
    largura, altura, imagem = carregar_imagem_decodificada("testes/feep.pbm")
    print(f'{largura} {altura} {imagem}')

main()

##return largura, altura, codificacao
##matriz.append(list(linha.strip()))




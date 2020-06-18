def decodificar(largura, altura, codificacao):
    imagem = []
    #devido as opcoes  00, 01, 10, 11
    #criar uma lista para cada combinacao correspondente
    #adicionar os 0s e 1s de acordo com a combinacao

    #algoritmo
    """1) Adicionar altura listas vazias na imagem
       2) Para um elemento a partir do terceiro de codificacao, ver se eh diferente de 00, 01, 10, 11
       3) Se for, fazer uma variavel que receba esse negocio em int
       4) Ver o proximo e adicionar o primeiro elemento da string na lista de indice par e o segundo 
       na lista seguinte"""
    m = int(altura)
    n = int(largura)
    for _ in range(m):
        l = []
        imagem.append(l)
    for i in range(len(imagem)):
        for k in range(3, len(codificacao)):#2 e 3
            if i % 2 == 0:
                a = codificacao[k]
                if a != '00' and a != '01' and a != '10' and a != '11':
                    a = int(a)
                    for _ in range(a):
                        if len(imagem[i]) < n:
                            imagem[i].append(codificacao[k + 1][0])
                            imagem[i + 1].append(codificacao[k + 1][1])
                        elif len(imagem[i]) == n:
                            if i != len(imagem) - 2:
                                i += 2
                                #repetir os passos
                                if len(imagem[i]) < n:
                                    imagem[i].append(codificacao[k + 1][0])
                                    imagem[i + 1].append(codificacao[k + 1][1])
                                elif len(imagem[i]) == n:
                                    if i != len(imagem) - 2:
                                        i += 2
                                        continue
                                    else:
                                        if len(imagem[i]) < n:
                                            imagem[i].append(codificacao[k + 1][0])
                                            imagem[i + 1].append(codificacao[k + 1][1])
                        
    return imagem        
                

#6 10 4 00 1 11 5 00 1 11 5 00 1 11 1 00 1 10 3 01 1 10 7 00
def main():
    codificacao = ['P1C', '6', '10', '4', '00', '1', '11', '5', '00', '1', '11', '5', '00', '1', '11', '1', '00', '1', '10', '3', '01', '1', '10', '7', '00']
    largura = codificacao[1]
    altura = codificacao[2]
    imagem = decodificar(largura, altura, codificacao)
    print(imagem)

main()
#deu certooooo
"""[
    ['0', '0', '0', '0', '1', '0'], 
    ['0', '0', '0', '0', '1', '0'], 
    ['0', '0', '0', '0', '1', '0'], 
    ['0', '0', '0', '0', '1', '0'], 
    ['0', '0', '0', '0', '1', '0'], 
    ['0', '0', '0', '0', '1', '0'], 
    ['1', '0', '0', '0', '1', '0'], 
    ['0', '1', '1', '1', '0', '0'], 
    ['0', '0', '0', '0', '0', '0'], 
    ['0', '0', '0', '0', '0', '0']] """
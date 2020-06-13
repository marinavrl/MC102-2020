def decodificar(largura, altura, codificacao):
    #contrario da codificar
    largura = codificacao[1]
    altura = codificacao[2]
    imagem = []
    imagem.append('P1')
    #notar que as codificacoes terao no max dez elementos pois
    #devido as opcoes  00, 01, 10, 11
    #criar uma lista para cada combinacao correspondente
    #adicionar os 0s e 1s de acordo com a combinacao
    
    return imagem

codificacao = ['8', '6', '4', '01', '4', '00', '16', '11'] #exemplo de codificacao resultante da funcao codificar
imagem = [
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['1', '1', '1', '1', '0', '0', '0', '0'],
    ['1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1'],
]
largura == 8
altura == 6
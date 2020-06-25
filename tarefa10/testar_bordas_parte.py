nova_imagem = []
altura = 8
largura = 8
imagem = [
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['1', '1', '1', '1', '0', '0', '0', '0'], 
    ['1', '1', '1', '1', '1', '1', '1', '1'],        
    ['1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1'],
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ]
for m in range(altura):
    l = []
    nova_imagem.append(l)
    for n in range(largura):
        nova_imagem[m].append('0')
for i in range(len(imagem)):
        for j in range(len(imagem[0])):
            if imagem[i][j] == '0':
                nova_imagem[i][j] = '0'
            elif imagem[i][j] == '1' and imagem[i-1][j] == '0':
                nova_imagem[i][j] = '1'
            elif imagem[i][j] == '1' and j == 0:
                nova_imagem[i][j] = '1'
            elif imagem[i][j] == '1' and imagem[i+1][j] == '0':
                nova_imagem[i][j] = '1'
            elif imagem[i][j] == '1' and j == len(imagem[0])-1:
                nova_imagem[i][j] = '1'
            elif imagem[i][j] == '1' and imagem[i-1][j-1] == '0':
                nova_imagem[i][j] == '1'
            elif imagem[i][j] == '1' and imagem[i-1][j+1] == '0':
                nova_imagem[i][j] == '1'
            elif imagem[i][j] == '1' and imagem[i+1][j-1] == '0':
                nova_imagem[i][j] == '1'
            elif imagem[i][j] == '1' and imagem[i+1][j+1] == '0':
                nova_imagem[i][j] == '1'
            elif imagem[i][j] == '1' and imagem[i-1][j-1] == '1' and imagem[i-1][j] == '1' and imagem[i-1][j+1] == '1' and imagem[i][j-1] == '1' and imagem[i][j+1] == '1' and imagem[i+1][j-1] == '1' and imagem[i+1][j] == '1' and imagem[i+1][j+1] == '1':
                nova_imagem[i][j] == '0'
print(nova_imagem)
"""[
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['1', '1', '1', '1', '0', '0', '0', '0'], 
    ['1', '0', '0', '1', '1', '1', '1', '1'],        
    ['1', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1'],
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ] """
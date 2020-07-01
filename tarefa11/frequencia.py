"""tarefa: dicionarios e tuplas"""
"""Stop words: artigos, preposicoes e conectivos.
O programa: conta a freq com que as palavras aparecem 
nos arquivos de texto
e encontra palavras-chaves no texto.
As palavras chave dao uma ideia sobre o topico principal doo texto
se se tratar de mais de um assunto, o topico secundario nao vai ser tao frequente  """
""" entrada: linha com o caminnho do arquivo
linha com as stop words
saida: 
primeira linha: deve conter as 3 palavras mais frequentes, da mais a menos
segunda linha:número de palavras cuja frequência 
é maior ou igual à da última 
palavra do primeiro quartil, 
quando consideramos as palavras da 
mais à menos frequente. Para determinar o quartil, 
desconsidere palavras que se repetem 5 vezes ou menos.
"""
#quartil== pega as que tem freq>=5 e organiza em ordem decrescente depois pega o primeiro quarto dessas,
# o quartil vai ser a ultima palavra desse quarto
nome1 = input()
nome2 = input()
nome3 = input()
#print(f'Hello, {nome1}.') FAZER LISTA/DICIONARIO PARA SEPARAR AS 3 MAIS FREQ?
#print(f'Hello, {nome2}.') SEGUNDA LINHA
#print(f'Hello, {nome3}.') TERCEIRA LINHA


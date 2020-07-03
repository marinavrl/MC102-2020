"""tarefa: dicionarios e tuplas""" #ler a parte de conjuntos unidade de colecoes
"""Stop words: artigos, preposicoes e conectivos.
O programa: conta a freq com que as palavras aparecem 
nos arquivos de texto
e encontra palavras-chaves no texto.
As palavras chave dao uma ideia sobre o topico principal doo texto
se se tratar de mais de um assunto, o topico secundario nao vai ser tao frequente  """
""" entrada: linha com o caminnho do arquivo...exemplo testes/texto3.in
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
def listar_palavras_arquivo(texto):
    with open(texto) as arquivo:
        L = []
        for line in arquivo:
            Ls = line.strip().split()
            L.append(Ls)
    for a in L:
        if a == []:
            L.remove(a)
    L0 = []
    for i in range(len(L)):
        for b in L[i]:
            L0.append(b)
    return L0 #melhor manter a lista pra contar a freq
#conjunto = set(L0)
#print(conjunto)
def tirar_stopwords(L0, stopwords): # recebe lista de stopwords da entrada, ver entrada do problema
    """ identifica as stop words em L0 e remove"""
    pass
def contar_frequencia():
    """ Recebe a lista sem stopwords e ordena da mais para a menos frequente, retornando uma lista organizada"""
    pass

def main():
    texto = "testes/texto0.in" #input
    stopwords = [] #lista recebe as stopwords
    L0 = listar_palavras_arquivo(texto)

"""conjunto com todas as palavras do arquivo, falta procurar as certas pra cada caso """
#conjunto = set(L)

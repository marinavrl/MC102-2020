"""Transformar todas as letras de uma string em maiúsculas:
print("mEU tESte".upper())
>>>MEU TESTE
 """

"""def funcao():
    if ...:
        return True
    elif ...:
        return False """

"""  * Recebe uma grade de caracteres e uma lista de
palavras
     * Deve contabilizar a ocorrencia de cada palavra
     * Destacar as palavras encontradas na grade 
     tornando as letras maiúsculas
     * Caractere '*' permanece inalterado """

"""A entrada do programa consiste em: L linhas 
representando a grade, sendo que os caracteres 
de cada linha são separados por um único espaço; 
um valor inteiro N indicando a quantidade de palavras 
que devem ser buscadas; e N palavras, uma por linha"""

"""Cada palavra deverá passar pelas 4 funções,
na main isso deve dar um for pra lista """

matriz = []
linha = input()

# Dica: use linha.isdigit(), linha.split() e matriz.append()
# para processar a entrada e armazenar a matriz de caracteeres

# Leitura e processamento das palavras

"""fazer um for para a lista"""

print("-" * 40)
print("Lista de Palavras")
print("-" * 40)

print("Palavra:", palavra)
print("Ocorrencias:", ocorrencias)
print("-" * 40)

# Impressão da matriz

for linha in matriz:
  print(" ".join(linha))
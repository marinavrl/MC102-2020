conjunto = set()

N = int(input())

for _ in range(N):
    i = 0
    palavra = input()
    conjunto.add(palavra)
    if palavra in conjunto:
        i += 1


print(conjunto)

""" - cria uma lista quando recebe cada linha (pelo split)
    - soma essa lista na principal
    - limpa a lista principal e tira as pontuacoes
    """
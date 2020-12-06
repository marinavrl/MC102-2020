# Leitura da lista de seleções

selecoes = []
dic = {}
for i in range(2):
  selecao = input()
  selecoes.append(selecao)
  dic[selecao] = {"partidas": 0, #dicionario de duas dimensões
                  "vitorias": 0, #um dicionario pra cada selecao
                  "derrotas": 0,
                  "penaltis": 0,
                  "normal": 0,
                  "marcados": 0,
                  "sofridos": 0}
print(selecoes)
print(dic)

# Leitura das partidas e processamento dos dados
###Para cada resultado, fazer split da entrada
##analisar se tem parenteses, pa ai é penalti

"""Seu programa receberá os resultados das 16 partidas 
que ocorreram até o final da competição, também sendo um 
resultado por linha"""

"""for i in range(16):
  resultado = input()
  resultado_split = resultado.split()
#for pais in resultado_split:"""
#comparar com a chave correspondente no dic e somar
#nos zeros

"""Quando a partida é decidida durante o 
tempo normal de jogo o formato do resultado é dado na 
seguinte forma:

<País 1> <Gols do país 1> x <Gols do país 2> <País 2> """

"""Quando a partida é decidida nos pênaltis o formato
do resultado é dado na seguinte forma:

<País 1> <Gols do país 1> x <Gols do país 2> (<Pênaltis do país 1> x <Pênaltis do país 2>) <País 2> """

"""
# Saída de dados

for selecao in selecoes:
  print("-" * 50)
  print("Pais:", selecao)
  print("Partidas:", dic[selecao]["partidas"])
  print("Partidas decididas em tempo normal de jogo:", dic[selecao]["normal"])
  print("Partidas decicidas nos penaltis:", dic[selecao]["penaltis"])
  print("Vitorias:", dic[selecao]["vitorias"])
  print("Derrotas:", dic[selecao]["derrotas"])
  print("Gols marcados:", dic[selecao]["marcados"])
  print("Gols sofridos:", dic[selecao]["sofridos"])

print("-" * 50)
print("Pais campeao:", campeao)
print("-" * 50) """

"""Como saída, para cada país, seguindo a ordem da lista:

Nome do país.
Quantidade de partidas disputadas.
Quantidade de partidas decididas em tempo normal de jogo.
Quantidade de partidas decicidas nos pênaltis.
Número de vitórias.
Número de derrotas.
Quantidade de gols marcados.
Quantidade de gols sofridos. """

"""Note que os gols marcados e sofridos não devem 
contabilizar aqueles marcados na decisão por pênaltis. """

"""Por fim, seu programa deve exibir o país campeão 
da Copa do Mundo de Futebol. Note que para ser 
campeão da competição o país não pode ter nenhuma 
derrota durante a etapa de "mata-mata". """
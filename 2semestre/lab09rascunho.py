# Leitura da lista de seleções

selecoes = []
dic = {}
for i in range(16):
  selecao = input()
  selecoes.append(selecao)
  dic[selecao] = {"partidas": 0, #dicionario de duas dimensões
                  "vitorias": 0, #um dicionario pra cada selecao
                  "derrotas": 0,
                  "penaltis": 0,
                  "normal": 0,
                  "marcados": 0,
                  "sofridos": 0}
"""print(selecoes)
print(dic)"""

# Leitura das partidas e processamento dos dados
###Para cada resultado, fazer split da entrada
##analisar se tem parenteses, pa ai é penalti

"""Seu programa receberá os resultados das 16 partidas 
que ocorreram até o final da competição, também sendo um 
resultado por linha"""

resultados = []

for i in range(16):
  resultado = input()
  resultado_split = resultado.split()
  resultados.append(resultado_split)

"""print(resultados) """

C = {"0", "(0", "0)", "1", "(1", "1)", "2", "(2", "2)",
 "3", "(3", "3)", "4", "(4", "4)", "5", "(5", "5)", "6", "(6", "6)", "7", "(7", "7)", 
 "8", "(8", "8)", "9", "(9", "9)", "10", "(10", "10)", "x"}

D = {"(0", "0)", "(1", "1)", "(2", "2)", "(3", "3)", "(4", "4)", "(5", "5)", "(6", "6)", "(7", "7)", 
"(8", "8)", "(9", "9)", "(10", "10)"}

for result in resultados:#contar a quantidade total de partidas etc
  for i in range(len(result)):
    if result[i] not in C:
      pais = result[i]
      dic[pais]["partidas"] += 1 #ok
    elif result[i] in C: #contar partidas normais ou penaltis
        if i == 1:
          if result[4] in D:
            pais = result[0]
            dic[pais]["penaltis"] += 1
          else:
            pais = result[0]
            dic[pais]["normal"] += 1
        elif i == 3:
          if result[4] in D:
            pais = result[7]
            dic[pais]["penaltis"] += 1
          else:
            pais = result[4]
            dic[pais]["normal"] += 1

for result in resultados: #identificar as vitorias
  if len(result) == 5: #passar para int
    result1 = int(result[1])
    result3 = int(result[3])
    if result1 > result3:
      pais = result[0]
      dic[pais]["vitorias"] += 1
    elif result1 < result3:
      pais = result[4]
      dic[pais]["vitorias"] += 1
  elif len(result) == 8:
    result14 = int(result[4][1])
    result60 = int(result[6][0])
    if result[4][1] > result[6][0]:
      pais = result[0]
      dic[pais]["vitorias"] += 1
    elif result[4][1] < result[6][0]:
      pais = result[7]
      dic[pais]["vitorias"] += 1

for result in resultados: #identificar as derrotas
  if len(result) == 5: #passar para int
    result1 = int(result[1])
    result3 = int(result[3])
    if result1 > result3:
      pais = result[4]
      dic[pais]["derrotas"] += 1
    elif result1 < result3:
      pais = result[0]
      dic[pais]["derrotas"] += 1
  elif len(result) == 8:
    result14 = int(result[4][1])
    result60 = int(result[6][0])
    if result[4][1] > result[6][0]:
      pais = result[7]
      dic[pais]["derrotas"] += 1
    elif result[4][1] < result[6][0]:
      pais = result[0]
      dic[pais]["derrotas"] += 1

for result in resultados: #contar gols marcados e sofridos
  if len(result) == 5: #passar para int
    result1 = int(result[1])
    result3 = int(result[3])
    pais = result[0]
    dic[pais]["marcados"] += result1
    dic[pais]["sofridos"] += result3
    pais = result[4]
    dic[pais]["marcados"] += result3
    dic[pais]["sofridos"] += result1

  elif len(result) == 8:
    result1 = int(result[1])
    result3 = int(result[3])
    pais = result[0]
    dic[pais]["marcados"] += result1
    dic[pais]["sofridos"] += result3
    pais = result[7]
    dic[pais]["marcados"] += result3
    dic[pais]["sofridos"] += result1

"""print(dic)"""

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

for selecao in selecoes:
  if dic[selecao]["derrotas"] == 0:
    campeao = selecao

print("-" * 50)
print("Pais campeao:", campeao)
print("-" * 50)
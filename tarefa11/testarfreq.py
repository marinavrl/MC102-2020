def contar_frequencia(L0):
    palavras_freq = []
    for i in range(len(L0)):
        a = 0
        for j in range(len(L0)):
            if L0[i] == L0[j]:
                a+=1
                palavra = L0[i]
            else:
                continue
        freq = a
        tupla = (palavra, freq)
        if tupla in palavras_freq:
            continue
        else:
            palavras_freq.append(tupla)
    return palavras_freq 
#esta contando corretamente
def main():
    L0 = ['Dilatação', 'tempo', 'No', 'dia', 'dia', 'corriqueira', 'ideia', 'tempo', 'algo', 'universal;', 'vez', 'sincronizados', 'relógios', 'idênticos,', 'esses', 'irão', 'ser', 'vistos', 'indicando', 'mesma', 'leitura,', 'independentemente', 'posições,', 'movimentos', 'relativos,', 'acelerações,', 'quem', 'esteja', 'observá-los.', 'A', 'mesma', 'ideia', 'atrela-se', 'noção', 'separação', 'espacial', 'pontos.', 'Espaço', 'tempo', 'são,', 'dia-a-dia', 'âmbito', 'mecânica', 'newtoniana,', 'entendidos', 'universais', 'absolutos;', 'restando', 'velocidade', 'serem', 'relativa', 'referenciais.', 'Tal', 'paradigma,', 'compatível', 'maioria', 'eventos', 'encontrados', 'cotidiano,', 'perdurou', 'dentro', 'ciência', 'até', 'início', 'século', 'XX,', 'quando', 'teoria', 'relatividade', 'veio', 'tona,', 'mostrando', 'realidade', 'natural', 'é,', 'contudo,', 'bem', 'sutil', 'pensava', 'até', 'então.', 'No', 'paradigma,', 'limite', 'relativístico,', 'inferência', 'tempo', 'deixa', 'ser', 'absoluta', 'passa', 'ser', 'algo', 'local,', 'atrelada', 'referencial', 'particular;', 'referenciais', 'movimento', 'relativo', 'sob', 'acelerações', 'distintas', 'geralmente', 'concordam', 'medidas', 'tempo', 'intervalos', 'tempo.', 'A', 'noção', 'simultaneidade', 'absoluta', 'também', 'cai', 'terra,', 'referenciais', 'diferentes', 'geralmente', 'concordarão', 'simultaneidade', 'eventos,', 'algum', 'referencial', 'eles', 'sejam', 'vistos', 'forma', 'simultânea.', 'Dilatação', 'tempo', 'designa,', 'âmbito', 'mecânica', 'einsteiniana,', 'outros', 'fenômeno', 'observador', 'percebe,', 'virtude', 'movimento', 'relativo', 'acelerado', 'referenciais,', 'relógio', 'observador', 'encontra-se', 'afastar-se,', 'fisicamente', 'idêntico', 'próprio', 'relógio,', 'está', "''andar''", 'devagar', 'tempo', 'observador', 'infere,', 'caso', 'devagar', 'tempo', 'próprio.', 'A', 'percepção', 'primeiro', 'observador', 'tempo', "''anda", "devagar''", 'relógio', 'móvel,', 'mas', 'isso', 'somente', 'verdade', 'contexto', 'referencial', 'observador', 'estático.', 'Em', 'ausência', 'aceleração,', 'princípio', 'paradoxalmente,', 'observador', 'também', 'verá', 'relógio', 'anexado', 'primeiro', 'referencial', "''andar''", 'devagar', 'próprio', 'relógio.', 'Localmente,', 'i.e.,', 'perspectiva', 'qualquer', 'observador', 'estático', 'junto', 'qualquer', 'referenciais,', 'relógios,', 'sincronizados', 'mantidos', 'juntos', 'atrasarão', 'adiantarão', 'relação', 'outro.', 'Ao', 'passo', 'relatividade', 'restrita', 'dilatação', 'tempo', 'simétrica', 'relação', 'referenciais,', 'seja,', 'qualquer', 'observador', 'relógio', 'móvel', 'atrasa-se', 'relação', 'carrega', 'consigo,', 'contexto', 'relatividade', 'geral,', 'estende-se', 'referenciais', '(covariância', 'geral),', 'dilatação', 'temporal', 'devida', 'acelerações', 'simétrica,', 'nesse', 'caso', 'ambos', 'observadores', 'concordarão', 'relógios', 'adianta', 'atrasa,', 'outro.', 'Considerando', 'novamente', 'relatividade', 'restrita,', 'intervalo', 'tempo', 'eventos', 'quaisquer', 'menor', 'possível', 'quando', 'medido', 'observador', 'detém', 'relógio,', 'sendo', 'este', 'conhecido', 'tempo', 'próprio', 'deste', 'observador.', 'Qualquer', 'observador', 'movimento', 'relativo', 'medirá', 'intervalo', 'tempo', 'maior', 'mesmos', 'eventos', 'considerados,', 'sendo', 'expressão', "''dilatação", "tempo''", 'bem', 'sugestiva,', 'portanto.']
    palavras_freq = contar_frequencia(L0)
    print(palavras_freq)

main()

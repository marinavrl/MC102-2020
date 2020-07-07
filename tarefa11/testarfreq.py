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
def main():#botar a lista editada
    L0 = ['são', 'buracos', 'negros', 'buraco', 'negro', 'região', 'espaço', 'campo', 'gravitacional', 'tão', 'intenso', 'nem', 'luz', 'consegue', 'escapar', 'dentro', 'dele', 'intensa', 'gravidade', 'comprime', 'matéria', 'até', 'haja', 'espaço', 'átomos', 'Corpos', 'celestes', 'dessa', 'natureza', 'podem', 'surgir', 'decorrência', 'morte', 'estrelas', 'supermassivas', 'Características', 'comunidade', 'científica', 'acredita', 'buracos', 'negros', 'apresentem', 'dimensões', 'bastante', 'variadas', 'menores', 'deles', 'podem', 'apresentar', 'até', 'tamanho', 'único', 'átomo', 'maiores', 'vez', 'podem', 'ter', 'raios', 'poucos', 'quilômetros', 'milhões', 'vezes', 'massa', 'Sol', 'Algumas', 'observações', 'astronômicas', 'forneceram', 'fortes', 'evidências', 'centro', 'grandes', 'galáxias', 'ocupado', 'buraco', 'negro', 'supermassivo', 'No', 'centro', 'galáxia', 'Via', 'Láctea', 'há', 'desses', 'nome', 'Sagittarius', 'buracos', 'negros', "sugam'", 'redor', 'buracos', 'negros', "sugam'", 'está', 'volta', 'campo', 'gravitacional', 'pode', 'prender', 'estrelas', 'planetas', 'longínquos', 'órbitas', 'espirais', 'Para', 'algo', 'seja', 'fato', "sugado'", 'interior', 'buraco', 'negro', 'sem', 'qualquer', 'chance', 'fuga', 'necessário', 'estabeleça', 'distância', 'mínima', 'centro', 'chamada', 'horizonte', 'eventos', 'essa', 'distância', 'velocidade', 'escape', 'seja', 'mínima', 'velocidade', 'escapar', 'buraco', 'negro', 'maior', 'própria', 'velocidade', 'luz', 'Deformações', 'espaço-tempo', 'De', 'acordo', 'teoria', 'Relatividade', 'Geral', 'Einstein', 'corpos', 'massas', 'muito', 'grandes', 'produzem', 'deformações', 'espaço-tempo', 'Essa', 'deformação', 'responsável', 'grande', 'aceleração', 'gravitacional', 'direção', 'centro', 'desses', 'corpos', 'Além', 'disso', 'grande', 'deformação', 'espaço-tempo', 'torna-o', 'curvo', 'forma', 'luz', 'propaga', 'proximidades', 'buracos', 'negros', 'percorre', 'linha', 'reta', 'mas', 'sim', 'trajetória', 'curvilínea', 'pois', 'próprio', 'espaço', 'região', 'está', 'deformado', 'dando', 'origem', 'fenômeno', 'chamado', 'lente', 'gravitacional', 'Aparência', 'buraco', 'negro', 'primeira', 'imagem', 'buraco', 'negro', 'foi', 'revelada', 'dia', '10', 'abril', '2019', 'Comissão', 'Europeia', 'descoberta', 'foi', 'feita', 'telescópio', 'Event', 'Horizon', 'projeto', 'interligou', 'oito', 'telescópios', 'teve', 'colaboração', '200', 'pesquisadores', 'buraco', 'negro', 'revelado', 'foi', 'encontrado', 'centro', 'galáxia', 'Messier', '87', 'M87', 'distância', '53', 'milhões', 'anos-luz', 'Terra', 'Ele', 'mede', '40', 'bilhões', 'quilômetros', 'diâmetro', 'três', 'milhões', 'vezes', 'tamanho', 'Terra', 'massa', '6,5', 'bilhões', 'vezes', 'Sol', 'Antes', 'descoberta', 'buracos', 'negros', 'eram', 'retratados', 'apenas', 'meio', 'animações', 'concepções', 'artísticas', 'concepções', 'artísticas', 'chegou', 'próxima', 'realidade', 'foi', 'feita', 'direção', 'arte', 'filme', 'Interestelar', 'meio', 'cálculos', 'feitos', 'físico', 'Kipp', 'Thorne', 'sob', 'direção', 'Christopher', 'Nolan', 'Quando', 'buraco', 'negro', 'atrai', 'si', 'conteúdo', 'gasoso', 'atmosfera', 'estrela', 'próxima', 'esse', 'gás', 'ganha', 'grande', 'aceleração', 'centrípeta', 'torno', 'centro', 'massa', 'buraco', 'negro', 'Com', 'aumento', 'velocidade', 'rotação', 'formado', 'disco', 'acreção', 'gás', 'presente', 'estrelas', 'está', 'repleto', 'cargas', 'elétricas', 'quando', 'aceleradas', 'produzem', 'ondas', 'eletromagnéticas', 'comprimentos', 'onda', 'possíveis', 'inclusive', 'luz', 'visível', 'Dessa', 'forma', 'volta', 'buraco', 'negro', 'atividade', 'ser', 'possível', 'observar', 'regiões', 'muito', 'luminosas', 'formatos', 'complexos', 'pois', 'grande', 'gravidade', 'local', 'deforma', 'caminho', 'percorrido', 'luz', 'emitida', 'gases', 'rotação']
    palavras_freq = contar_frequencia(L0)
    print(palavras_freq)

main()

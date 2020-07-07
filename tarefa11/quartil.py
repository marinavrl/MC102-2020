def quartil_lista(palavras_freq):
    """ Todas as palavras que tem freq maior ou igual a cinco e organiza em ordem decrescente,
     depois pega o primeiro quarto de palavras, o quartil vai ser a ultima desse quarto"""
    """ A segunda linha deve conter o número de palavras cuja frequência é maior ou igual à da
     última palavra do primeiro quartil, quando consideramos as palavra da mais à menos frequente. 
     Para determinar o quartil, desconsidere palavras que se repetem 5 vezes ou menos."""

    lista = []
    for i in range(len(palavras_freq)):
        if palavras_freq[i][1] >= 5:
            lista.append(palavras_freq[i])
    return lista#ok

def quartil_palavras(lista):
    quarto = []
    for i in range(len(lista)//4):
        quarto.append(lista[i])
    a = 0
    lista2 = []
    lista4 = []
    for j in range(len(lista)):
        if lista[j][1] >= quarto[len(quarto)-1][1]:
            a+=1
            lista4.append(lista[j][0])
        lista2.append(lista[j][0]) #tuplas em strings
    return quarto, a, lista2, lista4

def quartil_resto(lista2, lista4):
    lista1 = []
    for b in lista2:
        if b not in lista4:
            lista1.append(b)
    return lista1

def main():
    palavras_freq = [('buraco', 10), ('negro', 10), ('buracos', 6), ('centro', 6), ('negros', 6), ('luz', 5), ('foi', 4), ('grande', 4), ('gravitacional', 4), ('velocidade', 4), ('direção', 3), ('distância', 3), ('espaço', 3), ('espaço-tempo', 3), ('estrelas', 3), ('está', 3), ('massa', 3), ('milhões', 3), ('podem', 3), ('vezes', 3), ('Sol', 2), ('Terra', 2), ('aceleração', 2), ('artísticas', 2), ('até', 2), ('bilhões', 2), ('campo', 2), ('concepções', 2), ('corpos', 2), ('deformação', 2), ('descoberta', 2), ('desses', 2), ('escapar', 2), ('feita', 2), ('forma', 2), ('galáxia', 2), ('grandes', 2), ('gravidade', 2), ('gás', 2), ('meio', 2), ('muito', 2), ('mínima', 2), ('pois', 2), ('produzem', 2), ('próxima', 2), ('quilômetros', 2), ('região', 2), ('rotação', 2), ('seja', 2), ("sugam'", 2), ('tamanho', 2), ('volta', 2), ('10', 1), ('200', 1), ('2019', 1), ('40', 1), ('53', 1), ('6,5', 1), ('87', 1), ('Algumas', 1), ('Além', 1), ('Antes', 1), ('Aparência', 1), ('Características', 1), ('Christopher', 1), ('Com', 1), ('Comissão', 1), ('Corpos', 1), ('De', 1), ('Deformações', 1), ('Dessa', 1), ('Einstein', 1), ('Ele', 1), ('Essa', 1), ('Europeia', 1), ('Event', 1), ('Geral', 1), ('Horizon', 1), ('Interestelar', 1), ('Kipp', 1), ('Láctea', 1), ('M87', 1), ('Messier', 1), ('No', 1), ('Nolan', 1), ('Para', 1), ('Quando', 1), ('Relatividade', 1), ('Sagittarius', 1), ('Thorne', 1), ('Via', 1), ('abril', 1), ('aceleradas', 1), ('acordo', 1), ('acredita', 1), ('acreção', 1), ('algo', 1), ('animações', 1), ('anos-luz', 1), ('apenas', 1), ('apresentar', 1), ('apresentem', 1), ('arte', 1), ('astronômicas', 1), ('atividade', 1), ('atmosfera', 1), ('atrai', 1), ('aumento', 1), ('bastante', 1), ('caminho', 1), ('cargas', 1), ('celestes', 1), ('centrípeta', 1), ('chamada', 1), ('chamado', 1), ('chance', 1), ('chegou', 1), ('científica', 1), ('colaboração', 1), ('complexos', 1), ('comprime', 1), ('comprimentos', 1), ('comunidade', 1), ('consegue', 1), ('conteúdo', 1), ('curvilínea', 1), ('curvo', 1), ('cálculos', 1), ('dando', 1), ('decorrência', 1), ('deforma', 1), ('deformado', 1), ('deformações', 1), ('dele', 1), ('deles', 1), ('dentro', 1), ('dessa', 1), ('dia', 1), ('dimensões', 1), ('disco', 1), ('disso', 1), ('diâmetro', 1), ('eletromagnéticas', 1), ('elétricas', 1), ('emitida', 1), ('encontrado', 1), ('eram', 1), ('escape', 1), ('espirais', 1), ('essa', 1), ('esse', 1), ('estabeleça', 1), ('estrela', 1), ('eventos', 1), ('evidências', 1), ('fato', 1), ('feitos', 1), ('fenômeno', 1), ('filme', 1), ('formado', 1), ('formatos', 1), ('forneceram', 1), ('fortes', 1), ('fuga', 1), ('físico', 1), ('galáxias', 1), ('ganha', 1), ('gases', 1), ('gasoso', 1), ('haja', 1), ('horizonte', 1), ('há', 1), ('imagem', 1), ('inclusive', 1), ('intensa', 1), ('intenso', 1), ('interior', 1), ('interligou', 1), ('lente', 1), ('linha', 1), ('local', 1), ('longínquos', 1), ('luminosas', 1), ('maior', 1), ('maiores', 1), ('mas', 1), ('massas', 1), ('matéria', 1), ('mede', 1), ('menores', 1), ('morte', 1), ('natureza', 1), ('necessário', 1), ('nem', 1), ('nome', 1), ('observar', 1), ('observações', 1), ('ocupado', 1), ('oito', 1), ('onda', 1), ('ondas', 1), ('origem', 1), ('percorre', 1), ('percorrido', 1), ('pesquisadores', 1), ('planetas', 1), ('pode', 1), ('possíveis', 1), ('possível', 1), ('poucos', 1), ('prender', 1), ('presente', 1), ('primeira', 1), ('projeto', 1), ('propaga', 1), ('proximidades', 1), ('própria', 1), ('próprio', 1), ('qualquer', 1), ('quando', 1), ('raios', 1), ('realidade', 1), ('redor', 1), ('regiões', 1), ('repleto', 1), ('responsável', 1), ('reta', 1), ('retratados', 1), ('revelada', 1), ('revelado', 1), ('sem', 1), ('ser', 1), ('si', 1), ('sim', 1), ('sob', 1), ("sugado'", 1), ('supermassivas', 1), ('supermassivo', 1), ('surgir', 1), ('são', 1), ('telescópio', 1), ('telescópios', 1), ('teoria', 1), ('ter', 1), ('teve', 1), ('torna-o', 1), ('torno', 1), ('trajetória', 1), ('três', 1), ('tão', 1), ('variadas', 1), ('vez', 1), ('visível', 1), ('átomo', 1), ('átomos', 1), ('órbitas', 1), ('único', 1)]
    lista = quartil_lista(palavras_freq)
    #print(lista)
    (quarto, a, lista2, lista4) = quartil_palavras(lista)
    #print(a)
    #print(quarto)
    #print(lista2)
    print(' '.join(lista2[0:3]))
    print(a)
    lista1 = quartil_resto(lista2, lista4)
    #print(lista1)
    print(' '.join(lista1[0:3]))

main()
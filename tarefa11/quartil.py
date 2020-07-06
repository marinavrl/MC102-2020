def quartil_lista(palavras_freq):
    """ Todas as palavras que tem freq maior ou igual a cinco e organiza em ordem decrescente,
     depois pega o primeiro quarto de palavras, o quartil vai ser a ultima desse quarto"""
    """ A segunda linha deve conter o número de palavras cuja frequência é maior ou igual à da
     última palavra do primeiro quartil, quando consideramos as palavra da mais à menos frequente. 
     Para determinar o quartil, desconsidere palavras que se repetem 5 vezes ou menos."""

    lista = []
    for i in range(len(palavras_freq)):
        if palavras_freq[i][1] >= 5:
            lista.append(palavras_freq[i][0])
    return lista

def quartil_palavras(lista):
    quarto = []
    a = 0
    for i in range(len(lista)//4):
        quarto.append(lista[i])
        a+=1
    return quarto, a

def quartil_resto(lista, quarto):
    lista1 = []
    for b in lista:
        for c in quarto:
            if b!=c:
                lista1.append(b)
    return lista1

def main():
    palavras_freq = [('tempo', 15), ('observador', 11), ('referenciais', 7), ('relógio', 7), ('eventos', 4), ('relatividade', 4), ('referencial', 4), ('próprio', 4), ('devagar', 4), ('relógios', 3), ('ser', 3), ('acelerações', 3), ('A', 3), ('movimento', 3), ('relativo', 3), ('qualquer', 3), ('relação', 3), ('dilatação', 3), ('Dilatação', 2), ('No', 2), ('dia', 2), ('ideia', 2), ('algo', 2), ('sincronizados', 2), ('vistos', 2), ('mesma', 2), ('noção', 2), ('âmbito', 2), ('mecânica', 2), ('paradigma', 2), ('até', 2), ('quando', 2), ('bem', 2), ('absoluta', 2), ('geralmente', 2), ('simultaneidade', 2), ('também', 2), ('concordarão', 2), ("andar'", 2), ('caso', 2), ('primeiro', 2), ('móvel', 2), ('contexto', 2), ('estático', 2), ('outro', 2), ('restrita', 2), ('simétrica', 2), ('intervalo', 2), ('sendo', 2), ('corriqueira', 1), ('universal;', 1), ('vez', 1), ('idênticos', 1), ('esses', 1), ('irão', 1), ('indicando', 1), ('leitura', 1), ('independentemente', 1), ('posições', 1), ('movimentos', 1), ('relativos', 1), ('quem', 1), ('esteja', 1), ('observá-los', 1), ('atrela-se', 1), ('separação', 1), ('espacial', 1), ('pontos', 1), ('Espaço', 1), ('são', 1), ('dia-a-dia', 1), ('newtoniana', 1), ('entendidos', 1), ('universais', 1), ('absolutos;', 1), ('restando', 1), ('velocidade', 1), ('serem', 1), ('relativa', 1), ('Tal', 1), ('compatível', 1), ('maioria', 1), ('encontrados', 1), ('cotidiano', 1), ('perdurou', 1), ('dentro', 1), ('ciência', 1), ('início', 1), ('século', 1), ('XX', 1), ('teoria', 1), ('veio', 1), ('tona', 1), ('mostrando', 1), ('realidade', 1), ('natural', 1), ('é', 1), ('contudo', 1), ('sutil', 1), ('pensava', 1), ('então', 1), ('limite', 1), ('relativístico', 1), ('inferência', 1), ('deixa', 1), ('passa', 1), ('local', 1), ('atrelada', 1), ('particular;', 1), ('sob', 1), ('distintas', 1), ('concordam', 1), ('medidas', 1), ('intervalos', 1), ('cai', 1), ('terra', 1), ('diferentes', 1), ('algum', 1), ('eles', 1), ('sejam', 1), ('forma', 1), ('simultânea', 1), ('designa', 1), ('einsteiniana', 1), ('outros', 1), ('fenômeno', 1), ('percebe', 1), ('virtude', 1), ('acelerado', 1), ('encontra-se', 1), ('afastar-se', 1), ('fisicamente', 1), ('idêntico', 1), ('está', 1), ('infere', 1), ('percepção', 1), ('anda', 1), ('mas', 1), ('isso', 1), ('somente', 1), ('verdade', 1), ('Em', 1), ('ausência', 1), ('aceleração', 1), ('princípio', 1), ('paradoxalmente', 1), ('verá', 1), ('anexado', 1), ('Localmente', 1), ('i.e.', 1), ('perspectiva', 1), ('junto', 1), ('mantidos', 1), ('juntos', 1), ('atrasarão', 1), ('adiantarão', 1), ('Ao', 1), ('passo', 1), ('seja', 1), ('atrasa-se', 1), ('carrega', 1), ('consigo', 1), ('geral', 1), ('estende-se', 1), ('(covariância', 1), ('geral)', 1), ('temporal', 1), ('devida', 1), ('nesse', 1), ('ambos', 1), ('observadores', 1), ('adianta', 1), ('atrasa', 1), ('Considerando', 1), ('novamente', 1), ('quaisquer', 1), ('menor', 1), ('possível', 1), ('medido', 1), ('detém', 1), ('este', 1), ('conhecido', 1), ('deste', 1), ('Qualquer', 1), ('medirá', 1), ('maior', 1), ('mesmos', 1), ('considerados', 1), ('expressão', 1), ('sugestiva', 1), ('portanto', 1)]
    lista = quartil_lista(palavras_freq)
    print(' '.join(lista[0:3]))
    (quarto, a) = quartil_palavras(lista)
    print(a)
    print(quarto)
    lista1 = quartil_resto(lista, quarto)
    print(' '.join(lista1[0:3]))

main()
"""for verbete in lista:
        if verbete[0] == palavra:
            return verbete""" 
# o primeiro elemento da lista eh o primeiro adicionado e o ultimo eh o ultimo adicionado
#se a freq for igual faz:
# sorted: em ordem alfabetica
def ordenar_freq_decresc(palavras_freq):
    n = len(palavras_freq)
    for _ in range(n-1):
        for i in range(n-1):
            if palavras_freq[i+1][1] > palavras_freq[i][1]:
                aux = palavras_freq[i]
                palavras_freq[i] = palavras_freq[i+1]
                palavras_freq[i+1] = aux
    return palavras_freq

def main():
    palavras_freq = [('Dilatação', 2), ('tempo', 15), ('No', 2), ('dia', 2), ('corriqueira', 1), ('ideia', 2), ('algo', 2), ('universal;', 1), ('vez', 1), ('sincronizados', 2), ('relógios', 3), ('idênticos', 1), ('esses', 1), ('irão', 1), ('ser', 3), ('vistos', 2), ('indicando', 1), ('mesma', 2), ('leitura', 1), ('independentemente', 1), ('posições', 1), ('movimentos', 1), ('relativos', 1), ('acelerações', 3), ('quem', 1), ('esteja', 1), ('observá-los', 1), ('A', 3), ('atrela-se', 1), ('noção', 2), ('separação', 1), ('espacial', 1), ('pontos', 1), ('Espaço', 1), ('são', 1), ('dia-a-dia', 1), ('âmbito', 2), ('mecânica', 2), ('newtoniana', 1), ('entendidos', 1), ('universais', 1), ('absolutos;', 1), ('restando', 1), ('velocidade', 1), ('serem', 1), ('relativa', 1), ('referenciais', 7), ('Tal', 1), ('paradigma', 2), ('compatível', 1), ('maioria', 1), ('eventos', 4), ('encontrados', 1), ('cotidiano', 1), ('perdurou', 1), ('dentro', 1), ('ciência', 1), ('até', 2), ('início', 1), ('século', 1), ('XX', 1), ('quando', 2), ('teoria', 1), ('relatividade', 4), ('veio', 1), ('tona', 1), ('mostrando', 1), ('realidade', 1), ('natural', 1), ('é', 1), ('contudo', 1), ('bem', 2), ('sutil', 1), ('pensava', 1), ('então', 1), ('limite', 1), ('relativístico', 1), ('inferência', 1), ('deixa', 1), ('absoluta', 2), ('passa', 1), ('local', 1), ('atrelada', 1), ('referencial', 4), ('particular;', 1), ('movimento', 3), ('relativo', 3), ('sob', 1), ('distintas', 1), ('geralmente', 2), ('concordam', 1), ('medidas', 1), ('intervalos', 1), ('simultaneidade', 2), ('também', 2), ('cai', 1), ('terra', 1), ('diferentes', 1), ('concordarão', 2), ('algum', 1), ('eles', 1), ('sejam', 1), ('forma', 1), ('simultânea', 1), ('designa', 1), ('einsteiniana', 1), ('outros', 1), ('fenômeno', 1), ('observador', 11), ('percebe', 1), ('virtude', 1), ('acelerado', 1), ('relógio', 7), ('encontra-se', 1), ('afastar-se', 1), ('fisicamente', 1), ('idêntico', 1), ('próprio', 4), ('está', 1), ("andar'", 2), ('devagar', 4), ('infere', 1), ('caso', 2), ('percepção', 1), ('primeiro', 2), ('anda', 1), ('móvel', 2), ('mas', 1), ('isso', 1), ('somente', 1), ('verdade', 1), ('contexto', 2), ('estático', 2), ('Em', 1), ('ausência', 1), ('aceleração', 1), ('princípio', 1), ('paradoxalmente', 1), ('verá', 1), ('anexado', 1), ('Localmente', 1), ('i.e.', 1), ('perspectiva', 1), ('qualquer', 3), ('junto', 1), ('mantidos', 1), ('juntos', 1), ('atrasarão', 1), ('adiantarão', 1), ('relação', 3), ('outro', 2), ('Ao', 1), ('passo', 1), ('restrita', 2), ('dilatação', 3), ('simétrica', 2), ('seja', 1), ('atrasa-se', 1), ('carrega', 1), ('consigo', 1), ('geral', 1), ('estende-se', 1), ('(covariância', 1), ('geral)', 1), ('temporal', 1), ('devida', 1), ('nesse', 1), ('ambos', 1), ('observadores', 1), ('adianta', 1), ('atrasa', 1), ('Considerando', 1), ('novamente', 1), ('intervalo', 2), ('quaisquer', 1), ('menor', 1), ('possível', 1), ('medido', 1), ('detém', 1), ('sendo', 2), ('este', 1), ('conhecido', 1), ('deste', 1), ('Qualquer', 1), ('medirá', 1), ('maior', 1), ('mesmos', 1), ('considerados', 1), ('expressão', 1), ('sugestiva', 1), ('portanto', 1)]
    palavras_freq = ordenar_freq_decresc(palavras_freq)
    print(palavras_freq)

main()
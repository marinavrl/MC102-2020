# Instruções elementares
* Reconhecer instrução iterativa limitada.
* Reconhecer instrução iterativa condicional.
* Reconhecer que um número é maior ou menor que outro número.
* Dividir um número por outro.
* Reconhecer divisibilidade.
* Multiplicar dois ou mais números.
* Reconhecer números primos.
* Anotar números.
* Fatorar um número dado em fatores primos.
* Contar quantidades.
# Algoritmo para encontrar o número com maior quantidade de divisores
1) Aponte para o primeiro dos n números listados no conjunto dado.
2) Faça o seguinte n vezes:
    2.1) Fatore o número apontado em fatores primos.
    2.2) Anote o resultado da fatoração em fatores primos.
    2.3) Verifique a quantidade de cada fator primo no resultado anotado.
    2.4) Anote a quantidade de cada fator.
    2.5) Some 1 a todas as quantidades anotadas.
    2.6) Anote o resultado para cada quantidade.
    2.7) Se houver mais de uma quantidade anotada:
        2.7.1) Multiplique todos os resultados.
        2.7.2) Anote o valor resultante da multiplicação.
    2.8) Enquanto o número atual apontado não for o n-ésimo da sequência dada, aponte para o próximo número dos n listados.
3) Verifique qual dos valores anotados é maior.
4) Anote o maior número.
5) Verifique qual a ordem do número anotado na sequência de n repetições da linha (2).
6) Anote a ordem do número.
7) Verifique qual dos n números dados na entrada está na mesma ordem sequencial anotada.
8) Aponte para o número verificado.
9) Devolva como saída o número apontado.

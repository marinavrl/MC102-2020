# Instruções elementares
* Ler entrada e devolver saída.
* Somar dois números.
* Subtrair dois números.
* Reconhecer múltiplos de um número natural.
* Anotar um número.
* Interpretar a notação de datas a/b/c.
* Interpretar instrução de desvio.
* Interpretar instrução iterativa condicional.
* Interpretar sequências finitas de números.
# Algoritmo para somar um número de dias n a uma data a/b/c
1) Some o valor de a ao valor de n, obtendo o valor de a+n.
2) Anote o valor de a+n.
3) Se b=2, verifique:
    3.1) Se c for múltiplo de 4 e não for múltiplo de 100 ou for múltiplo 400, verifique também:
        3.1.1) SE A+N FOR MENOR OU IGUAL A 29 verdadeiro:
            3.1.1.1) Vá para a linha 6.
        3.1.2) SE A+N MAIOR QUE 29 verdadeiro:
            3.1.2.1) Vá para a linha 7. 
            3.1.2.2) Faça o passo 4.
    3.2) Se c não for múltiplo de 4 ou for múltiplo de 100 e não for múltiplo de 400, verifique também:
        3.2.1) SE A+N FOR MENOR OU IGUAL A 28 verdadeiro:
            3.2.1.1) Vá para a linha 6.
        3.2.2) SE A+N MAIOR QUE 28 verdadeiro:
            3.2.2.1) Vá para a linha 7.
            3.2.2.2) Faça o passo 4.
4) Se b pertence à sequência (1,3,5,7,8,10,12), verifique:
    4.1) SE A+N FOR MENOR OU IGUAL A 31 verdadeiro:
        4.1.1) Vá para a linha 6.
    4.2) Se a+n for maior que 31, verfique, também:
        4.2.1) Se b for igual a 12, faça:
            4.2.1.1) Substitua o valor de b por 1.
            4.2.1.2) Subtraia 31 de a+n, obtendo a+n-31.
            4.2.1.3) Anote o resultado.
            4.2.1.4) Devolva a+n-31 no lugar de a+n.
            4.2.1.5) Some 1 ao valor de c, obtendo o valor de c+1.
            4.2.1.6) Anote o resultado.
            4.2.1.7) Devolva c+1 no lugar de c.
            4.2.1.8) Repita o passo 4.
        4.2.2) Se b for diferente de 12, faça:
            4.2.2.1) Some 1 ao valor de b, obtendo o valor de b+1.
            4.2.2.2) Anote o resultado.
            4.2.2.3) Devolver b+1 no lugar de b.
            4.2.2.4) Subtraia 31 de a+n, obtendo o valor de a+n-31.
            4.2.2.5) Anote o resultado.
            4.2.2.6) Devolva o valor de a+n-31 no lugar de a+n.
            4.2.2.7) Repita os passos a partir do passo 3 segundo as condições.
5) Se b pertence à sequência (4,6,9,11), verifique:
    5.1) SE A+N MENOR OU IGUAL A 30 verdadeiro:
        5.1.1) Vá para a linha 6.
    5.2) SE A+N MAIOR QUE 30 verdadeiro:
        5.2.1) Vá para a linha 7.
        5.2.2) Repita o passo 4.
# 6) SE A+N MENOR OU IGUAL A W
1) Devolva a+n no lugar de a.
2) Mantenha os valores de b e c.
3) Devolva como saída a data correspondente ao novos valores de a, b e c.
# 7) SE A+N MAIOR QUE W
1) Some 1 ao valor de b, obtendo o valor de b+1.
2) Anote o resultado.
3) Devolver b+1 no lugar de b.
4) Subtraia w de a+n, obtendo o valor de a+n-w.
5) Anote o resultado.
6) Devolva o valor de a+n-w no lugar de a+n.





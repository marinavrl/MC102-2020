#list comprehension - ver tutorial python - mostra a comprehension e o algoritmo equivalente

n = int(input("Quantos números serão lidos? "))

lista = [int(input()) for i in range(n)]

print(lista)

x = int(input("Qual número deve ser removido? "))

lista = [i for i in lista if i != x]

print(lista)
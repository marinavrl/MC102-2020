###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Bruto x Líquido
# Nome: Marina Victória Roncalio de Lima
# RA: 241482
###################################################

# Leitura de dados

"""A entrada do seu programa será composta por uma única linha,
contendo um valor real, representando o salário bruto."""
salario_bruto = float(input())

# Desconto de INSS

if salario_bruto <= 1045.00:
    INSS = salario_bruto * 7.5/100
    salario_liquido0 = salario_bruto - INSS

elif 1045.00 < salario_bruto <= 2089.60:
    INSS = salario_bruto * 9.0/100
    salario_liquido0 = salario_bruto - INSS

elif 2089.60 < salario_bruto <= 3134.40:
    INSS = salario_bruto * 12.0/100
    salario_liquido0 = salario_bruto - INSS

elif 3134.40 < salario_bruto:
    INSS = salario_bruto * 14.0/100
    salario_liquido0 = salario_bruto - INSS


# Desconto de IR

if 1903.98 < salario_liquido0 <= 2826.65:
    IR = salario_liquido0 * 7.5/100 - 142.80
    salario_liquido = salario_liquido0 - IR

elif 2826.65 < salario_liquido0 <= 3751.05:
    IR = salario_liquido0 * 15.0/100 - 354.80
    salario_liquido = salario_liquido0 - IR

elif 3751.05 < salario_liquido0 <= 4664.68:
    IR = salario_liquido0 * 22.5/100 - 636.13
    salario_liquido = salario_liquido0 - IR

elif 4664.68 < salario_liquido0:
    IR = salario_liquido0 * 27.5/100 - 869.36
    salario_liquido = salario_liquido0 - IR

else:
    IR = 0.00
    salario_liquido = salario_liquido0


# Saída de dados

print("Bruto: R$", format(salario_bruto, ".2f").replace(".", ","))
print("INSS: R$", format(INSS, ".2f").replace(".", ","))
print("IR: R$", format(IR, ".2f").replace(".", ","))
print("Liquido: R$", format(salario_liquido, ".2f").replace(".", ","))

"""Bruto: R$ <Salário bruto> #salario_bruto
INSS: R$ <Desconto de INSS> #desconto_INSS
IR: R$ <Desconto de IR> #
Liquido: R$ <Salário líquido>"""
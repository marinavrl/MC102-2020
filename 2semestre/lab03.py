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
    desconto_INSS = salario_bruto * 7.5/100
    salario_liquido0 = salario_bruto - desconto_INSS




# Desconto de IR

if 1903.98 < salario_liquido0 <= 2826.65:
    desconto_IR = salario_liquido0 * 

elif 2826.65 < salario_liquido0 <= 3751.05:

 



# Saída de dados
"""
print("Bruto: R$", format(salario_bruto, ".2f").replace(".", ","))
print("INSS: R$", format(INSS, ".2f").replace(".", ","))
print("IR: R$", format(IR, ".2f").replace(".", ","))
print("Liquido: R$", format(salario_liquido, ".2f").replace(".", ","))"""

"""Bruto: R$ <Salário bruto>
INSS: R$ <Desconto de INSS>
IR: R$ <Desconto de IR>
Liquido: R$ <Salário líquido>"""
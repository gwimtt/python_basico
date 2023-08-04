"""
Faça um script em Python que leia o valor do salário de um funcionário e 
mostre se o salário é maior ou menor que o valor mínimo.
"""

salario = float(input('Digite o valor do seu salário: '))

if salario<1320:
    print('Seu salário é menor que um salário mínimo.')
elif salario==1320:
    print('Seu salário é igual a um salário mínimo.')
else:
    print('Seu salário é maior que um salário mínimo.')
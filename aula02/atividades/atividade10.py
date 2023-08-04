"""
Faça um Script em Python que solicite ao usuário digitar 2 números. 
Em seguida, imprima o total com casas decimais da divisão e o total inteiro (sem casas decimais): 
"""

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

print(f'O total com casas decimais da divisão é igual a: {num1/num2}')
print(f'O total sem casas decimais da divisão é igual a: {num1//num2}')
"""
Faça um Script em Python que solicite ao usuário informar o valor de uma compra. 
Em seguida, aplique 10% de desconto e imprima na tela tanto o valor total como também o valor com o desconto aplicado. 
"""

valor = float(input('Digite o valor da sua compra: '))
desconto = valor*10/100
valor_desconto = valor-desconto

print(f'Sua compra com 10% de desconto é igual a: {valor_desconto}')
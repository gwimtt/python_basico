"""
Faça um Script em Python que solicite ao usuário informar 3 números. 
Em seguida, multiplique os valores e envie para a saída padrão a seguinte frase: "A multiplicação entre <X>, <Y> e <Z> é igual <Total>". 
"""

num1 = float(input("Digite um número:"))
num2 = float(input("Digite outro número:"))
num3 = float(input("Digite outro número:"))

print(f'A multiplicação entre {num1}, {num2} e {num3} é igual a: {num1*num2*num3}')
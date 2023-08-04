"""
Crie um script em Python para receber dois números informados pelo usuário e mostrar todos números entre eles em ordem decrescente.
"""

v_inicial = int(input('Digite o valor inicial: '))
v_final = int(input('Digite o valor final: '))
i = v_final

while i<=0:
    print(i, end=" ")
    i = i - 1

"""
Faça um script que leia dois valores positivos e mostre a soma dos números ímpares entre eles.
"""

valor1 = int(input('Digite um valor positivo: '))
valor2 = int(input('Digite outro valot positivo: '))
i = 0


if valor1 and valor2 <= 0:
    while valor1 <= valor2:
        if valor1 %2 != 0:
            print(valor1)
        valor1+=1
    print('A soma dos valores é:', i )
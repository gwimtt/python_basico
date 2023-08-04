# leia dois números inteiros e mostre somente o menor valor

valor1 = int(input('Escreva o valor 1:'))
valor2 = int(input('Escreva o valor 2:'))

if valor1<valor2:
    print(f"{valor1} é menor.")
elif valor1==valor2:
    print("Os valores são inguais.")
else:
    print(f"{valor2} é menor.")

num1 = int(input('Escreva um numero: '))
num2 = int(input('Escreva outro numero: '))
soma = 0

if num1 < num2:
    while num1 <= num2:
        if num1 % 2 != 0:
            soma += num1
            print("A soma dos números é", soma)
elif num2 < num1:
    while num2 <= num1:
        if num2 % 2 != 0:
            soma += num2
            print("A soma dos números é", soma)
else:
    print("Números iguais.")
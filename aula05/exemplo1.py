"""#  exemplo da função range()
from types import MethodWrapperType


print(list(range(2,20))) #range é uma função que define intervalos
print(list(range(10)))
print(list(range(10, 100, 5))) # em range, o valor1=começo, valor2=fim e valor3=passos.
print('*'*70)

# loop for
for i in range(10):
    print(i, end=" ")
print('\nValor final: do contador: ', i)
print('*'*70)

# contagem de 20 até 30 usando laço for
for j in range(20,31):
    print(j, end=" ")
print('\nValor final:',j)
print('*'*70)

# contagem de 10 até 0
for z in range(10, -1, -1):
    print(z, end=' ')
print('\nValor final: ',z)
print('*'*70)
"""
"""# leia 5 números inteiros e mostre uma mensagme quando o número for par
for i in range (5):
    num = int(input('Informe o valor: '))
    if num % 2 == 0:
    
print('O número é par.')"""

# leia 5 números inteiros, some somente os valores ímpares e mostre a quantiddade de ímpares
soma = 0
n_impar = 0

for j in range (5):
    num1 = int(input('Digite um valor: '))
    if num1 % 2 != 0:
        soma += num1
        n_impar += 1

print('A soma dos valores ímpares é:', soma)
print('O valor de números ímpares digitados é:', n_impar)
# mostre a média aritméticas dos ímpares
print(f'Media: {soma/n_impar: .2f}')
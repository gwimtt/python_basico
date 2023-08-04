# estrutura de repetição while (continuação)
# leia 5 números e mostre a soma de todos os valores informados.

"""
cont = 1
soma = 0 # acumulador

while cont<=5:
    num = float(input('Informe um valor: '))
    soma+=num # sempre o valor anterior e o novo digitado pelo usuário no input.
    cont+=1 # atualização do contador por último.
print('Resultado da soma:',soma)
"""

"""
calcular a soma dos valores do intervalo (fechado)
variáveis:
a = 10
b = 25
"""

"""
a = 10
b = 25
soma = 0

while a<=b:
    print(a, end=" ")
    soma+=a
    a+=1
print(f'Resultado da soma: {soma}')
"""

# leia 2 valores inteiros e mostre a soma do intervalo entre eles.
"""
v1 = int(input('Digite o valor inicial: '))
v2 = int(input('Digite o valor final: '))
soma = 0

if v1<v2:
    while v1<=v2:
        soma+=v1
        v1+=1
    print(f'O resultado é: {soma}')
elif v2<v1:
    while v2<=v1:
        soma+=v2
        v2+=1
    print(f'O resultado é: {soma}')
else:
    print('Os valores são iguais =(')
"""

# somar 5 valores positivos informados pelo usuário
"""
soma = 0
cont = 1

while cont<=5:
    valor = float(input('Informe um valor positivo (POR FAVOR): '))
    if valor<0:
        continue # ignora a parte debaixo e volta pro input.
    soma+=valor
    cont+=1
print(f'O resultado final é: {soma}')
"""
# somar 5 valores negativos informados pelo usuário
"""
soma = 0
cont = 1

while cont<=5:
    valor = float(input('Informe um valor negativo (POR FAVOR): '))
    if valor>=0:
        print('Só zua...')
        break # quebra a parada.
    soma+=valor
    cont+=1
print(f'O resultado final é: {soma}')
"""

# leia 3 notas e mostre a média, caso seja digitado um valor negativo ou acima de 10, será solicitado um novo valor.
soma = 0
cont = 1

while cont<=3:
    nota = float(input('Digite sua nota: '))
    if nota<0 or nota>10:
        print('Digite novamente.')
        continue
    soma=soma+nota
    cont = cont+1
print(f'A soma das notas informadas é {soma}')
print(f'A média dos valores é : {soma/3:.2f}')
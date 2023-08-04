# reforçando coisas da aula passada

# estruturas de decisão (estruturas condicionais)

"""
leia a idade do aluno e defina sua categoria de acordo com as seguintes informações:
categoria - idade
sem categoria - menor do que 3
infantil - 3 até 10
juvenil - 11 até 17
adulto - 18 até 39
senior - 40 até 130
acima de 130 - idade inválida
"""

idade = int(input('Digite a sua idade: '))

if idade<3:
    print('Sem categoria.')
elif idade<=10:
    print('Você está na categoria infantil.')
elif idade<=17:
    print('Você está na categoria juvenil.')
elif idade<=39:
    print('Você está na categoria adulto.')
elif idade<=130:
    print('Você está na categoria sênior.')
else:
    print('Você é mentiroso.')
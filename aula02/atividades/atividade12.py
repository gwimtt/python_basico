"""
Faça um Script em Python que solicite ao usuário informar uma quantidade de dias, horas, minutos e segundos. 
Em seguida, converta tudo para segundos: 
"""

dias = int(input('Digite uma quantidade de dias: '))
hr = int(input('Digite uma quantidade de horas: '))
min = int(input('Digite uma quantidade de minutos: '))
seg = int(input('Digite uma quantidade de segundos: '))

print(f'{dias} dias para segundos são {dias*86400} segundos.')
print(f'{hr} horas para segundos são {hr*3600} segundos.')
print(f'{min} minutos para segundos são {min*60} segundos.')
print(f'{seg} segundos para segundos são {seg*1}')
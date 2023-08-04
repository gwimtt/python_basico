# estrutura de repetição while (enquanto).
i = 0
while i<=10:
    print(i,end=" ")
    i = i+1 

print('\nValor final do contador:',i)
print('*'*100)

# contagem iniciando em 50 até 200.
i = 50
while i<=200:
    print(i, end=" ")
    i = i+1
print('\ncabô agui: ',i)
print('*'*100)

# contagem iniciando em 10 e finalizando em 80, incrementando os valores de 10 em 10.
i = 10
while i<=80:
    print(i, end=" ")
    i = i+10
print('\ncabô agui: ',i)
print('*'*100)

# mostrar a mensagem "eu tenho que estudar" 300x.
i = 1
while i<=300:
    print(i,'- eu tenho que estudar')
    i = i+1
print('*'*100)
"""
leia um número e mostre a contagem a partir de zero até o número informado.
"""

vlr_final = int(input('Informe o valor final: '))
i = 0

while i<=vlr_final:
    print(i)
    i = i+1
print('*'*100)

# contagem decrescente iniciando em 23 até 0.
i = 23
while i>=0:
    print(i, end=' ')
    i = i-1
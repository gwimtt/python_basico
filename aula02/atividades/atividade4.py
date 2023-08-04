"""
Faça um Script em Python que solicite ao usuário informar um número. 
Em seguida, armazene este número numa variável e por fim, mostre o dobro e a metade do valor digitado. 
"""

num = float(input('Digite um número:'))
if num==0:
    print('O número informado é neutro')
else:
    print(f'O dobro de {num} é {num*2} e a metade de {num} é {num/2}')
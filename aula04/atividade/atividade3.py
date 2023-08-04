"""
3.	Faça um script que mostre os números pares em um intervalo definido pelo usuário.
"""

v_i = int(input('Digite o inicio do intervalo desejado: '))
v_f = int(input('Digite o fimn do intervalo desejado: '))
i = 0

if v_i <= v_f:
    while v_i <= v_f:
        if v_i % 2 == 0:
            print(v_i)
        v_i += 1
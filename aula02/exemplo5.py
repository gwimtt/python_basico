# leia o valor de um produto, caso o valor seja menor do que 100, mostre a seguinte mensagem:
# "você recebeu 5% de desconto, caso contrário."
# "você recebeu 10% de desconto."

valor = float(input('Digite o valor do seu produto:'))

if valor<=100:
    print(f'Você recebeu 5% de desconto.')
else:
    print(f'Você recebeu 10% de desconto.')
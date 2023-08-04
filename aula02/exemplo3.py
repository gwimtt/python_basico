# desafio - leia a idade do usuário e informe se ele é maior ou menor de idade

idade = int(input("Escreva a sua idade:"))

if idade<0:
    print('Valor inválido.')
    print('Tente novamente.')
else:
    if idade>=18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade")
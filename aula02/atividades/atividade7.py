"""
7.	Faça um Script em Python que solicite a nota das 4 provas semestrais do usuário. 
Em seguida, calcule e envie para a saída padrão a média: 
"""
print('Insira abaixa suas notas do semestre.')
print('-'*70)

nota1 = float(input('Digite a nota da sua primeira prova: '))
nota2 = float(input('Digite a nota da sua segunda prova: '))
nota3 = float(input('Digite a nota da sua terceira prova: '))
nota4 = float(input('Digite a nota da sua quarta prova: '))


print(f'A média das suas 4 notas das provas é igual a: {(nota1+nota2+nota3+nota4)/4}')

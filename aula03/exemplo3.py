# aplicar operadores lógicos com if
# leia a qtd de faltas de um aluno e sua média final

qtd_faltas = int(input('Informe a quantidade de faltas: '))
media = float(input('Informe a média final: '))

# condições de reprovação:
# qtd de faltas maior do que 8 e média menor do que 7
# analisar condição do aluno somente se o valor das faltas for maior ou igual a zero
# saber o porquê da reprovação
if qtd_faltas<0:
    print('Valor de faltas inválido.')
else:    
    if qtd_faltas>8 or media<7:
        print('REPROVADO!!!')
        if qtd_faltas>8:
            print('Você foi reprovado por faltas.')
        elif media<7:
            print('Você foi reprovado por nota.')
    else:
        print('APROVADO!!!')
valor1 = 45
valor2 = 258.45

# operadores aritméticos 
# print("Soma:",valor1+valor2)
# print("Subtração:",valor1-valor2)
# print("Multiplicação:",valor1*valor2)
# print("Divisão:",valor1/valor2)

# f-string nos valores

# print(f"Divisão com duas casas decimais: {valor1/valor2: .2f}")
# print(f"valor 2: {valor2: .1f}")
# print("-"*40)

# obter dados do teclado (entreda de dados)

usuario = input("Informe o seu nome: ")
print(f"Seja bem-vindo(a) {usuario}")

# conversão de tipos - casting

idade = int(input("Informe sua idade: "))
print(f"O nome do usuário é {usuario} e sua idade atual é {idade}")

# mostrar o dobro da idade informada pelo usuário

print(f"O dobro da sua idade é: {idade*2}") 
print("-"*40)

# mostrar tipos de dados das variáveis

# print("Idade:", type (idade))
# print("Nome:", type (usuario))

valor_curso = float(input("Informe o valor pago para o seu curso: "))
print(f"O valor informado foi {valor_curso}")

# Mostrar uma mensagem com 25% do valor do curso
# Parabéns!!! vc ganhou <valor> de cédito na próxima compra 

print(f"25% do valor do seu curso é igual a {valor_curso/4}")
print("Parabéns!!! Você ganhou R$ 50 de crédito na próxima compra.")
print("-"*40)

# solicitar quantidade de parcelas do pagamento
parcelas = int(input("Em quantas vezes você quer parcelar o valor?: "))

# mostrar valor das parcelas sem juros
print(f"O valor das parcelas sem juros é: {valor_curso/parcelas}")
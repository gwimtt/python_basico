# desafio - leia um número real e armazene o valor em uma variável
num = float(input("Escreva um número: "))
print(type(num))

# verificar se o número informado é positivo
if num>0:       # teste for True
    print("O valor informado é positívo.")
elif num==0:
    print("O valor informado é neutro.")
else:       # teste for False
    print("O valor informado é negativo.")

print("Aqui finaliza o script!!!")
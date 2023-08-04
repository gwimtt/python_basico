"""
leia 2 números e mostre a contagem do intervalo dos valores informados
"""

vlr_inicial = int(input('Digite o valor inicial da contagem: '))
vlr_final = int(input('Digite o valor final da contagem: '))

i = vlr_inicial
vlr_final = vlr_final

while i<=vlr_final:
    print(i, end=" ")
    i+=1

# jeito "certo"

vlr_inicial = int(input('Digite o valor inicial da contagem: '))
vlr_final = int(input('Digite o valor final da contagem: '))

while vlr_inicial<=vlr_final:
    print(vlr_inicial)
    vlr_inicial += 1
from random import randint

print('-=-' * 15, '\033[31mMaior e Menor Valor em Tuplas\033[m', '-=-' * 15)

n1 = str(randint(0, 10))
n2 = str(randint(0, 10))
n3 = str(randint(0, 10))
n4 = str(randint(0, 10))
n5 = str(randint(0, 10))
numeros = (n1, n2, n3, n4, n5)
print(f'Os números são: \033[34m{", ".join(numeros)}.')

maior = numeros[0]
menor = numeros[0]
for c in range(1, len(numeros)):
    if numeros[c] > maior:
        maior = numeros[c]
    elif numeros[c] < menor:
        menor = numeros[c]
print(f'O \033[33mmaior\033[0m número é \033[34m{maior}\033[0m e'
      f' o \033[33mmenor\033[0m número é \033[31m{menor}\033[0m.')

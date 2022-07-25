print('-=-' * 15, '\033[31mAnálise de Dados em Uma Tupla\033[m', '-=-' * 15)

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
n3 = int(input('Digite mais outro número: '))
n4 = int(input('Digite o último número: '))
num = (n1, n2, n3, n4)
if num.count(9) == 0:
    print('O número 9 não foi digitado.')
else:
    print(f'O número 9 foi digitado: \033[34m{num.count(9)} vezes\033[0m.')

if num.count(3) > 0:
    print(f'O número 3 foi digitado pela primeira vez na: \033[34m{num.index(3) + 1}º posição\033[0m.')
else:
    print('O número 3 não foi digitado.')

print('Os números pares são: \033[34m', end="")
for pos, n in enumerate(num):
    if num[pos] % 2 == 0:
        print(num[pos], end=" ")

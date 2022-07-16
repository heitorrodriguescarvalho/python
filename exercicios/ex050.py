print('-=-' * 15, '\033[31mSomando Somente Números Pares\033[m', '-=-' * 15)

soma = int(0)
for c in range(0, 6):
    n = int(input(f'Digite o \033[33m{c+1}º número\033[0m: '))
    if n % 2 == 0:
        soma = soma + n

print(f'\033[34mA soma de todos os números pares é \033[32m{soma}\033[34m.')

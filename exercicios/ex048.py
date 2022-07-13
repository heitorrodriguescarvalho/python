print('-=-' * 15, '\033[31mSomando Todos os Múltiplos de 3\033[m', '-=-' * 15)

soma = int(0)
for c in range(3, 500, 3):
    print(f'\033[1;33m{c}')
    soma = soma + c

print(f'\033[1;34mA soma total de todos os múltiplos de 3 é \033[1;32m{soma}\033[1;34m.')

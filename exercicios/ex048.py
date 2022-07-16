print('-=-' * 15, '\033[31mSomando Todos os Números Ímpares Múltiplos de 3\033[m', '-=-' * 15)

soma = int(0)
for c in range(3, 501, 3):
    if c % 2 == 1:
        print(f'\033[1;33m{c}')
        soma = soma + c

print(f'\033[1;34mA soma total de todos os múltiplos ímpares de 3 é \033[1;32m{soma}\033[1;34m.')

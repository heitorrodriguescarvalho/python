print('-=-' * 15, '\033[31mFunções para Fatorial\033[m', '-=-' * 15)


def fatorial(num, show=False):
    result = num
    if show:
        print(result, end=" ")
    for c in range(num-1, 0, -1):
        if show:
            print(f'x {c}', end=" ")
        result *= c
    if show:
        print('=', end=" ")
    print(result)


n = int(input('Número: '))
mostrar = str(input('Mostrar o processo (y/n): ')).strip().lower()
while mostrar not in ['y', 'n']:
    print('\033[31mValor Inválido!\033[0m')
    mostrar = str(input('Mostrar o processo (y/n): ')).strip().lower()
print('\033[37m-\033[0m' * 40)
if mostrar == 'y':
    fatorial(n, True)
else:
    fatorial(n)

print('-=-' * 15, '\033[31mFunção que descobre o maior\033[m', '-=-' * 15)


def maior(num):
    print(f'Dos números \033[33m{str(num)[1:-1]}\033[0m o maior é \033[34m{max(num)}\033[0m.')


numbers = list()
count = 0
while True:
    count += 1
    n = str(input(f'Digite o {count}º número: ')).strip().lower()
    while not n.isnumeric() and n != 'stop':
        print('\033[31mValor Inválido!\033[0m')
        n = str(input(f'Digite o {count}º número: ')).strip().lower()
    if n == 'stop':
        break
    else:
        numbers.append(int(n))
maior(numbers)


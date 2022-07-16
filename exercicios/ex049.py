print('-=-' * 15, '\033[31mTabuada\033[m', '-=-' * 15)

n = int(input('Digite um número: '))

for c in range(1, 11):
    print(f'\033[34m{n} x {c:2} = \033[33m{n*c}')

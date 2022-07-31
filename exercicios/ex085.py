print('-=-' * 15, '\033[31mListas com Pares e Ímpares\033[m', '-=-' * 15)

par = list()
impar = list()
num = [par, impar]
for c in range(0, 7):
    n = int(input(f'Digite o {c+1}º número: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
impar.sort()
par.sort()
print('\033[37m-\033[0m' * 40)
print(f'Foram cadastrados {len(num[1]) + len(num[0])} números:')
print(f'Ímpares: \033[34m{str(num[1])[1:-1]}\033[0m')
print(f'Pares: \033[34m{str(num[0])[1:-1]}\033[0m')

print('-=-' * 15, '\033[31mLista Ordenada sem Repetições\033[m', '-=-' * 15)

num = [int(input('Digite o 1º número: '))]
for c in range(1, 5):
    print('\033[37m-\033[0m' * 40)
    print(f'A lista atualmente é \033[34m{str(num)[1:-1]}\033[0m')
    n = int(input(f'Digite o {c + 1}º número: '))
    cont = 0
    while True:
        if cont == len(num):
            if n > num[-1]:
                num.append(n)
                break
            else:
                num.insert(cont, n)
                break
        elif n < num[cont]:
            num.insert(cont, n)
            break
        else:
            cont += 1
print('\033[37m-\033[0m' * 40)
print(f'A lista ficou: \033[34m{str(num)[1:-1]}\033[0m')

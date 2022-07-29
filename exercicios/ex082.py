print('-=-' * 15, '\033[31mDividindo Valores em Várias Listas\033[m', '-=-' * 15)

print('\033[31mDigite "stop" para Parar.\033[0m')
num = []
par = []
impar = []
while True:
    n = str(input('Digite números ou "stop": ')).strip().lower()
    if n.isnumeric():
        num.append(int(n))
    elif n == 'stop':
        break
    else:
        print('Digite um Valor Válido!')
    if int(n) % 2 == 0:
        par.append(int(n))
    else:
        impar.append(int(n))
    print('\033[37m-\033[0m' * 40)
num.sort()
impar.sort()
par.sort()
print(f'Todos os valores: \033[34m{str(num)[1:-1]}\033[0m;')
print(f'Números ímpares: \033[34m{str(impar)[1:-1]}\033[0m;')
print(f'Números pares: \033[34m{str(par)[1:-1]}\033[0m;')

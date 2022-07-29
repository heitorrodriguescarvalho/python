print('-=-' * 15, '\033[31mExtraindo Dados de uma Lista\033[m', '-=-' * 15)

print('\033[31mDigite "stop" para Parar.\033[0m')
num = []
while True:
    n = str(input('Digite números ou "stop": ')).strip().lower()
    if n.isnumeric():
        num.append(int(n))
    elif n == 'stop':
        break
    else:
        print('Digite um Valor Válido!')
    print('\033[37m-\033[0m' * 40)

print(f'A lista contém {len(num)} elementos;')
num.sort(reverse=True)
print(f'A lista em Ordem Decrescente fica: \033[34m{str(num)[1:-1]}\033[0m;')
if 5 in num:
    print(f'O valor 5 está na lista na {num.index(5) + 1}º posição.')
else:
    print('O valor 5 não está contido na lista.')

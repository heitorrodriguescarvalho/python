print('-=-' * 15, '\033[31mValores Únicos em uma Lista\033[m', '-=-' * 15)

numeros = []
print('\033[31mDigite "n" para Parar!\033[0m')
while True:
    num = str(input('Digite um número ou "n": ')).lower().strip()
    if num.isnumeric():
        if numeros.count(num) == 0:
            numeros.append(num)
        else:
            print('Valor repetido! Não será adicionado.')
    elif num == 'n':
        break
    else:
        print('\033[31mValor Inválido!\033[0m')
numeros.sort()
print(f'Os valores digitados foram: \033[34m{", ".join(numeros)}\033[0m')

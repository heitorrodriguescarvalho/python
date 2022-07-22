print('-=-' * 15, '\033[31mCaixa Eletrônico\033[m', '-=-' * 15)

# Analisa o valor a ser sacado.
while True:
    print('\033[34mRealizando Saque\033[0m')
    valor = int(input('Qual valor deseja sacar? \033[32mR$\033[0m'))

    # Calcula as cédulas do saque.
    cedulas50 = 0
    cedulas20 = 0
    cedulas10 = 0
    cedulas1 = 0

    while valor >= 50:
        cedulas50 += 1
        valor -= 50

    while valor >= 20:
        cedulas20 += 1
        valor -= 20

    while valor >= 10:
        cedulas10 += 1
        valor -= 10

    while valor >= 1:
        cedulas1 += 1
        valor -= 1

    # Retorna a quantidade de cédulas ao usuário.
    print(f'Cédulas de \033[33m50\033[0m: \033[34m{cedulas50}\033[0m')
    print(f'Cédulas de \033[33m20\033[0m: \033[34m{cedulas20}\033[0m')
    print(f'Cédulas de \033[33m10\033[0m: \033[34m{cedulas10}\033[0m')
    print(f'Cédulas de \033[33m1\033[0m: \033[34m{cedulas1}\033[0m')
    print('\033[37m-\033[0m' * 40)

    repetir = ''
    repetir = str(input('Deseja realizar outro saque (y/n)? ')).lower().strip()
    while repetir not in ['y', 'n']:
        print('\033[31mDigite um Valor Válido!\033[0m')
        repetir = str(input('Deseja realizar outro saque (y/n)? ')).lower().strip()
    if repetir == 'n':
        break
    print('\033[37m-\033[0m' * 40)

print('\033[34mObrigado por utilizar nosso serviço de caixa eletrônico!')
print('Tenha um bom dia :)\033[0m')

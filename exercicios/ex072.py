print('-=-' * 15, '\033[31mNúmeros por Extenso\033[m', '-=-' * 15)

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    posicao = int(input('Digite um número de \033[33m0 a 20\033[0m: '))
    while posicao not in range(0, 21):
        print('\033[31mValor Inválido!\033[0m')
        posicao = int(input('Digite um número de \033[33m0 a 20\033[0m: '))
    print(f'\033[34m{num[posicao].capitalize()}\033[0m')
    print(f'\033[37m-\033[0m' * 40)
    repetir = ''
    repetir = str(input('Deseja ver outro número (y/n)? ')).strip().lower()
    while repetir not in ['y', 'n']:
        print('\033[31mValor Inválido!\033[0m')
        repetir = str(input('Deseja ver outro número \033[33m(y/n)\033[0m? ')).strip().lower()
    if repetir == 'n':
        break
    print(f'\033[37m-\033[0m' * 40)
print('\033[31mProcesso Finalizado!\033[0m')

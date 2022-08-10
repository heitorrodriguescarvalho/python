print('-=-' * 15, '\033[31mValidando Entrada de Dados em Python\033[m', '-=-' * 15)


def isint(pergunta):
    n = str(input(pergunta))
    while not n.isnumeric():
        print('\033[31mErro: o valor não é numérico!\033[0m')
        n = str(input(pergunta))
    return n


num = isint('Digite um número: ')
print(f'Você digitou o número {num}.')

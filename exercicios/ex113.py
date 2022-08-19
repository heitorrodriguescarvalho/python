print('-=-' * 15, '\033[31mFunções Aprofundadas em Python\033[m', '-=-' * 15)


def leiaint():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except KeyboardInterrupt:
            print('Não digitado')
            n = int(0)
            break
        except:
            print('\033[31mDigite um Número Inteiro Válido!\033[0m')
        else:
            break
    return n


def leiafloat():
    while True:
        try:
            n = float(input('Digite um número real: '))
        except KeyboardInterrupt:
            print('Não digitado')
            n = float(0)
            break
        except:
            print('\033[31mDigite um Número Real Válido!\033[0m')
        else:
            break
    return n


inteiro = leiaint()
real = leiafloat()
print(f'Número Inteiro: {inteiro}')
print(f'Número Real: {real}')

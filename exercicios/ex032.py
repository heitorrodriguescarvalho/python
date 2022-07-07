ano = int(input('Em que anos nós estamos? '))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'Se estamos em {ano}, logo estamos em um ano bissexto.')
        else:
            print(f'{ano} não é um ano bissexto.1')
    else:
        print(f'Se estamos em {ano}, logo estamos em um ano bissexto.')
else:
    print(f'{ano} não é um ano bissexto.3')

print('-=-' * 15, '\033[31mAnalizando e calculando valores\033[m', '-=-' * 15)

novosValores = 'Y'
while novosValores != 'N':
    novosValores = 'N'

    # Pega os valores digitados pelo usuário.
    num = [float(input('Digite o \033[34m1º valor\033[0m: '))]
    rep = int(2)
    adNum = str('')
    while adNum != 'N':
        num.append(float(input(f'Digite o \033[34m{rep}º valor\033[0m: ')))
        rep += 1
        adNum = str('')
        while adNum not in ['Y', 'N']:
            adNum = str(input('Deseja \033[33madicionar mais um valor\033[0m (Y/N)? ')).strip().upper()
            if adNum not in ['Y', 'N']:
                print('\033[31mDigite um valor válido!\033[0m')

    # Pega qual ação o usuário quer realizar.
    print('\033[33m[ 1 ] \033[34mSomar\n'
          '\033[33m[ 2 ] \033[34mMultiplicar\n'
          '\033[33m[ 3 ] \033[34mMaior\n'
          '\033[33m[ 4 ] \033[34mNovos Números\n'
          '\033[33m[ 5 ] \033[34mSair do Programa')
    acao = int(input('\033[33m>\033[0m '))
    while acao not in range(1, 6):
        print('\033[31mValor Inválido!')
        acao = int(input('\033[33mDigite um valor válido: '))

    # Faz a soma dos valores caso seja a ação escolhida.
    if acao == 1:
        soma = float(0)
        for c in range(0, len(num)):
            soma += num[c]

        if str(soma)[-1] == '0' and str(soma)[-2] == '.':
            soma = int(soma)
        print(f'Os \033[33m{len(num)} valores somados\033[0m resultam em \033[34m{soma}\033[0m.')

    # Faz a multiplicação dos valores caso seja a ação escolhida.
    elif acao == 2:
        multiplicacao = num[0]
        for c in range(1, len(num)):
            multiplicacao = multiplicacao * num[c]

        if str(multiplicacao)[-1] == '0' and str(multiplicacao)[-2] == '.':
            soma = int(multiplicacao)
        print(f'Os \033[33m{len(num)} valores multiplicados\033[0m resultam em \033[34m{multiplicacao}\033[0m.')

    # Analisa qual é o maior valor caso a ação seja escolhida.
    elif acao == 3:
        maior = num[0]
        for c in range(1, len(num)):
            if num[c] > maior:
                maior = num[c]

        if str(maior)[-1] == '0' and str(maior)[-2] == '.':
            soma = int(maior)
        print(f'Dos \033[33m{len(num)} valores\033[0m, o maior é o \033[34m{maior}\033[0m.')

    # Faz o programa voltar para o início caso a ação seja escolhida.
    elif acao == 4:
        novosValores = 'Y'

from random import randint

print('-=-' * 15, '\033[31mJogando Impar ou Par\033[m', '-=-' * 15)

wins = 0
play = str('y')
while play != 'n':
    # Número do computador.
    comput = randint(0, 10)

    # Dados do jogador.
    while True:
        paridade = str(input('Impar ou Par (i/p)? ')).lower().strip()
        if paridade in ['i', 'p']:
            break
        else:
            print('\033[31mDigite um Valor Válido!\033[0m')

    while True:
        player = int(input('Agora, digite seu número (1 a 10): '))
        if player in range(1, 11):
            break
        else:
            print('\033[31mDigite um Valor Válido!\033[0m')

    # Verifica quem ganhou e se o jogador quer jogar novamente.
    print('\033[37m-\033[0m' * 40)
    print(f'O \033[33mComputador\033[0m escolheu \033[34m{comput}\033[0m.')
    teste = (comput + player) % 2
    if teste == 1:
        teste = 'i'
    else:
        teste = 'p'
    if teste == paridade:
        print('\033[32mVocê Ganhou!\033[0m')
        wins += 1
        while True:
            play = str(input('Que tal jogar mais uma vez (y/n)? ')).lower().strip()
            if play in ['y', 'n']:
                break
            else:
                print('\033[31mDigite um Valor Válido!\033[0m')
    else:
        print('\033[31mVocê Perdeu!\033[0m')
        play = 'n'

    print('\033[37m-\033[0m' * 40)

print(f'Você ganhou \033[34m{wins}\033[0m vezes consecutivas.')

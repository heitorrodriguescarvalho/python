from random import randint

print('-=-' * 15, '\033[31mJogando Jokenpô\033[m', '-=-' * 15)

print('''Digite:
 \033[1;33m1. \033[1;34mPedra\033[0;0m;
 \033[1;33m2. \033[1;34mPapel\033[0;0m;
 \033[1;33m3. \033[1;34mTesoura\033[0;0m.''')

print('\033[1mJokenpô...')

adversario = randint(1, 3)
if adversario == 1:
    jogadaAdversario = 'Pedra'

elif adversario == 2:
    jogadaAdversario = 'Papel'

elif adversario == 3:
    jogadaAdversario = 'Tesoura'

jogador = int(input('> '))
if jogador >= 1 and jogador <= 3:
    if jogador == 3 and adversario == 2 or jogador == 2 and adversario == 1 or jogador == 1 and adversario == 3:
        print(f'\033[1;34mParabéns, você venceu! Seu adversário havia escolhido {jogadaAdversario}.')

    elif jogador == 1 and adversario == 2 or jogador == 2 and adversario == 3 or jogador == 3 and adversario == 1:
        print(f'\033[1;31mInfelizmente, você perdeu! Seu adversário havia escolhido {jogadaAdversario}.')

    elif jogador == adversario:
        print(f'\033[1;33mQue coincidência, vocês empataram! Ambos haviam escolhido {jogadaAdversario}.')

else:
    print('\033[1;31mValor Inválido!')

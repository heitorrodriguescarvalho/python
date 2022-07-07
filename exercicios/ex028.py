from random import randint

print('O computador pensou em um número de 1 a 5')
num = int(input('Qual é sua aposta? '))

if num >= 6:
    print('Erro: O número digitado é inválido.')
else:
    if num < 0:
        print('Erro: O número digitado é inválido.')
    else:

        randomNum = randint(0, 5)
        if num == randomNum:
            print(f'Parábens, o número realmente era {num}!')
        else:
            print(f'Não foi dessa vez! O número correto era {randomNum}.')

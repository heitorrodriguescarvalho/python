from random import randint

print('-=-' * 15, '\033[31mJogo da Adivinhação\033[m', '-=-' * 15)

# O número aleatório no qual o jogador deve acertar é definido.
numRandom = randint(0, 10)

tentativas = int(0)
numPlayer = int(input('Tente acertar o número de \033[34m0 a 10\033[0m no qual o computador pensou: '))
while numRandom != numPlayer:
    numPlayer = int(input('\033[31mVocê errou\033[0m, tente novamente: '))
    tentativas += 1
print(f'\033[34mParabéns, você acertou após \033[33m{tentativas}\033[34m erro(s)!')

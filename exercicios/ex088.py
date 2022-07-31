from random import randint
from time import sleep

print('-=-' * 15, '\033[31mPalpites para a Mega Sena\033[m', '-=-' * 15)

jogos = int(input('Digite quantos jogos devem ser sorteados: '))
num = list()
valores = list()
for jogo in range(0, jogos):
    while len(num) < 6:
        n = randint(1, 60)
        if n not in num:
            num.append(n)
    num.sort()
    valores.append(num[:])
    num.clear()
print('\033[37m-\033[0m' * 40)
for c in range(0, jogos):
    print(f'Jogo {c+1}: \033[34m{str(valores[c])[1:-1]}\033[0m')
    sleep(0.75)

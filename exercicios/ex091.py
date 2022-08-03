from random import randint
from time import sleep

print('-=-' * 15, '\033[31mJogo de Dados em Python\033[m', '-=-' * 15)

num = int(input('Quantos jogadores: '))
print('Valores Sorteados:')
players = dict()
for c in range(0, num):
    players[f'player{c + 1}'] = randint(1, 6)
    print(f'    O \033[33mjogador {c + 1}\033[0m tirou \033[34m{players[f"player{c + 1}"]}\033[0m.')
    sleep(0.75)
cont = 0
print('Ranking de Pontuações:')
for i in sorted(players, key=players.get, reverse=True):
    cont += 1
    print(f'    {cont}º lugar: \033[33m{i}\033[0m com \033[34m{players[i]}\033[0m.')

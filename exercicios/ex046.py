from time import sleep

print('-=-' * 15, '\033[31mContagem Regresiva para o Estouro de Fogos de Artifício\033[m', '-=-' * 15)

input('Digite algo para começar a contagem: ')
for c in range(10, 0, -1):
    print(f'\033[1;33m{c}')
    sleep(1)

print('\033[1;34mOs Fogos foram Lançados!')

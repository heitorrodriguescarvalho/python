print('-=-' * 15, '\033[31mMaior e Menor Valor na Lista\033[m', '-=-' * 15)

num = []
for c in range(0, 5):
    num.append(int(input(f'Digite o {c + 1}º número: ')))

maior = max(num)
menor = min(num)

print('\033[37m-\033[0m' * 40)

numStr = str(num[0])
for n in range(1, len(num)):
    numStr = f'{numStr}, {num[n]}'

print(f'Você digitou os valores: {numStr}.')

cont = 0
posMaior = []
numMaior = num.count(maior)
for c in range(0, numMaior):
    posMaior.append(num.index(maior, cont))
    cont = posMaior[-1] + 1

cont = 0
posMenor = []
numMenor = num.count(menor)
for c in range(0, numMenor):
    posMenor.append(num.index(menor, cont))
    cont = posMenor[-1] + 1

posMaiorStr = posMaior[0]
for c in range(1, len(posMaior)):
    posMaiorStr = f'{posMaiorStr}, {posMaior[c]}'
posMenorStr = posMenor[0]
for c in range(1, len(posMenor)):
    posMenorStr = f'{posMenorStr}, {posMenor[c]}'

print(f'O maior valor foi \033[34m{maior}\033[0m na(s) posição(ões) \033[34m{posMaiorStr}\033[0m.')
print(f'O menor valor foi \033[34m{menor}\033[0m na(s) posição(ões) \033[34m{posMenorStr}\033[0m.')

print('-=-' * 15, '\033[31mAprimorando Dicionários\033[m', '-=-' * 15)

data = list()
infos = dict()
goals = list()
count = 0
while True:
    count += 1
    print('\033[34mCadastrando Jogador\033[0m')
    infos['name'] = str(input(f'Nome do {count}º jogador: ')).strip().capitalize()
    matches = int(input(f'Número de partidas de {infos["name"]}: '))
    while matches <= 0:
        print('\033[31mValor Inválido!\033[0m')
        matches = int(input(f'Número de partidas de {infos["name"]}: '))
    infos['matches'] = matches
    for p in range(0, infos['matches']):
        goal = int(input(f'Gols na {p + 1}º partida: '))
        while goal < 0:
            print('\033[31mValor Inválido!\033[0m')
            goal = int(input(f'Gols na {p + 1}º partida: '))
        goals.append(goal)
    infos['goals'] = goals[:]
    infos['total'] = sum(goals)
    data.append(infos.copy())
    goals.clear()
    print(data)
    addMore = str(input('Adicionar mais jogadores (y/n): ')).strip().upper()
    while addMore not in ['Y', 'N']:
        print('\033[31mValor Inválido! (y/n)\033[0m')
        addMore = str(input('Adicionar mais jogadores (y/n): ')).strip().upper()
    print('\033[37m-\033[0m' * 45)
    if addMore == 'N':
        break

print(f'Nº {"Nome":>5} {"Gols":>12} {"Total":>22}')
print('\033[37m-\033[0m' * 45)
for c in range(0, len(data)):
    print(f'{c}.  {data[c]["name"]:<12} {str(data[c]["goals"])[1:-1]:<21} {data[c]["total"]}')
print('\033[37m-\033[0m' * 45)
while True:
    print('\033[34mConsultando Jogadores\033[0m')
    while True:
        consult = str(input('Nº do Jogador (ou "stop"): ')).strip().lower()
        if consult.isnumeric():
            if int(consult) < 0 or int(consult) >= len(data):
                print('\033[31mValor Inválido!\033[0m')
            else:
                break
        elif consult == 'stop':
            break
        else:
            print('\033[31mValor Inválido!\033[0m')

    if consult.isnumeric():
        print('\033[37m-\033[0m' * 40)
        print(f'Levantamento do Jogador {data[int(consult)]["name"]}:')
        for pos, c in enumerate(data[int(consult)]['goals']):
            print(f'{pos + 1}º Partida: {c} gols')
    elif consult == 'stop':
        break
    print('\033[37m-\033[0m' * 40)

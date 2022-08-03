print('-=-' * 15, '\033[31mCadastro de um Jogador de Futebol\033[m', '-=-' * 15)

data = dict()
data['name'] = str(input('Nome do Jogador: ')).strip().capitalize()
data['matches'] = int(input(f'Total de Partidas do {data["name"]}: '))

data['goals'] = list()
for p in range(0, data['matches']):
    data['goals'].append(int(input(f'Total de Gols da {p + 1}º Partida: ')))
data['total'] = sum(data['goals'])
data['mean'] = data['total'] / data['matches']
print('\033[37m-\033[0m' * 40)
print(data)
print('\033[37m-\033[0m' * 40)
print(f'O campo "name" tem o valor {data["name"]}')
print(f'O campo "goals" tem o valor {data["goals"]}')
print(f'O campo "total" tem o valor {data["total"]}')
print(f'O campo "mean" tem o valor {data["mean"]}')
print('\033[37m-\033[0m' * 40)
print(f'{data["name"]} jogou {data["matches"]} partidas:')
for c in range(0, data["matches"]):
    print(f'    Na {c + 1}º partida, fez {data["goals"][c]} gols.')
print(f'Com uma média de {round(data["mean"], 2)} gols por partida, ' 
      f'terminou o campeonato com um total de {data["total"]} gols.')

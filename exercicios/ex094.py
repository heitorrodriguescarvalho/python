print('-=-' * 15, '\033[31mUnindo Dicionários e Listas\033[m', '-=-' * 15)

data = list()
personalInfo = dict()
count = 0
while True:
    count += 1
    personalInfo['name'] = str(input(f'{count}º Nome: ')).strip().capitalize()
    personalInfo['age'] = int(input(f'{count}º Idade: '))
    personalInfo['gender'] = str(input(f'{count}º Gênero (m/f): ')).strip().upper()
    while personalInfo['gender'] not in ['M', 'F']:
        print('\033[31mDigite um Valor Válido! (m/f)\033[0m')
        personalInfo['gender'] = str(input(f'{count}º Gênero (m/f): ')).strip().upper()
    data.append(personalInfo.copy())
    print(data)
    addMore = str(input('Adicionar mais (y/n): ')).strip().upper()
    while addMore not in ['Y', 'N']:
        print('\033[31mDigite um Valor Válido! (y/n)\033[0m')
        addMore = str(input('Adicionar mais (y/n): ')).strip().upper()
    if addMore == 'N':
        break
print('\033[37m-\033[0m' * 40)

women = list()
mean = 0
olderPeople = list()
for c in range(0, len(data)):
    mean += data[c]['age']
    if data[c]['gender'] == 'F':
        women.append(data[c]['name'])
mean /= len(data)
for c in range(0, len(data)):
    if data[c]['age'] > mean:
        olderPeople.append(data[c]['name'])

print(f'- {len(data)} pessoas foram cadastradas;')
print(f'- A média das idades é {round(mean, 2)} anos;')
print(f'- Foram cadastradas {len(women)} mulheres: {", ".join(women)};')
print(f'- {len(olderPeople)} pessoas possuem a idade acima da média: {", ".join(olderPeople)}.')

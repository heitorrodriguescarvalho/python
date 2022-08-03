import datetime
date = datetime.date.today()
currentYear = date.year

print('-=-' * 15, '\033[31mCadastro de Trabalhador em Python\033[m', '-=-' * 15)

data = dict()
data['name'] = str(input('Nome: ')).strip().capitalize()
while True:
    data['birthday'] = int(input('Ano de Nascimento: '))
    if len(str(data['birthday'])) != 4:
        print('\033[31mDigite um Ano Válido com 4 dígitos!')
    else:
        break
data['age'] = currentYear - data['birthday']
data['ctps'] = int(input('Carteira de Trabalho (0 caso não tenha): '))
if data['ctps'] != 0:
    while True:
        data['hiringYear'] = int(input('Ano de Contratação: '))
        if data['hiringYear'] < data['birthday']:
            print('\033[31mVocê não pode ser contratado antes de nascer!\033[0m')
        else:
            break
    data['income'] = float(input('Salário: '))
    data['retire'] = data['hiringYear'] + 35 - data['birthday']
print('\033[37m-\033[0m' * 40)
print(f'''Nome: {data["name"]};
Idade: {data["age"]};
''', end="")
if data['ctps'] != 0:
    print(f'''CTPS: {data["ctps"]};
Ano de Contratação: {data["hiringYear"]};
Salário: R${data["income"]:.2f};
Aposentadoria: aos {data["retire"]} anos.
''')

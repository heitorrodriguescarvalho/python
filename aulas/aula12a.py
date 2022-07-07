nome = str(input('Qual é o seu nome? ')).capitalize()
if nome == 'Heitor':
    print('Que nome bonito!')
elif nome == 'Fábio' or nome == 'Fernanda':
    print('Que nome legal!')
else:
    print('Que nome bosta!')
print(f'Tenha um bom dia, {nome}.')

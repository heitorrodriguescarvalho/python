print('-=-' * 15, '\033[31mDicionário em Python\033[m', '-=-' * 15)

dados = dict()
dados['nome'] = str(input('Nome: ')).strip().capitalize()
dados['media'] = float(input('Média: '))
if dados['media'] >= 6:
    print(f'{dados["nome"]} foi \033[34maprovado!\033[0m')
else:
    print(f'{dados["nome"]} foi \033[34mreprovado!\033[0m')

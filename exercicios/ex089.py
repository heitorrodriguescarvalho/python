print('-=-' * 15, '\033[31mBoletim com Listas Compostas\033[m', '-=-' * 15)

boletim = list()
while True:
    print('\033[34mCadastrando Aluno!\033[0m')
    nome = str(input('Nome: ')).strip().capitalize()
    while True:
        nota1 = float(input('1º nota: '))
        if nota1 in range(0, 11):
            break
    while True:
        nota2 = float(input('2º nota: '))
        if nota2 in range(0, 11):
            break
    dados = [nome, [nota1, nota2]]
    boletim.append(dados[:])
    print('\033[37m-\033[0m' * 40)
    continuar = ''
    while continuar not in ['y', 'n']:
        continuar = str(input('Adicionar mais alunos (y/n): '))
    print('\033[37m-\033[0m' * 40)
    if continuar == 'n':
        break
print(f'{"Nº"}{"Nome":>7}{"Média":>19}')
print('\033[37m-\033[0m' * 29)
for c in range(0, len(boletim)):
    print(f'{c}{".":<4}{boletim[c][0]:<18}{(boletim[c][1][0] + boletim[c][1][1]) / 2}')
while True:
    consulta = ''
    while consulta not in range(0, len(boletim)):
        consulta = int(input('Consultar nota (nº): '))
    print(f'\033[34m{boletim[consulta][0]}\033[0m')
    print(f'1º nota: {boletim[consulta][1][0]:.1f}')
    print(f'2º nota: {boletim[consulta][1][1]}:.1f')
    continuar = ''
    while continuar not in ['y', 'n']:
        continuar = str(input('Consultar mais notas (y/n): '))
    print('\033[37m-\033[0m' * 40)
    if continuar == 'n':
        break

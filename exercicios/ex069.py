print('-=-' * 15, '\033[31mAnalizando Dados Idade e Sexo\033[m', '-=-' * 15)

# Pega os dados dos cadastrados.
adultos = 0
homens = 0
mulheres = 0
mulheresJovens = 0
c = 0
adcPessoa = 'y'
while adcPessoa != 'n':
    c += 1
    print('\033[34mCadastrando Pessoa\033[0m')
    idade = int(input(f'Digite a idade da {c}º pessoa: '))
    sexo = str(input(f'Digite o sexo da {c}º pessoa (m/f): ')).lower().strip()
    while sexo not in ['m', 'f']:
        sexo = str(input(f'\033[31mValor Inválido\033[0m, digite o sexo da {c}º pessoa: '))

    print('\033[37m-\033[0m' * 40)

    # Faz as verificações dos dados.
    if idade > 18:
        adultos += 1

    if sexo == 'm':
        homens += 1
    else:
        mulheres += 1
        if idade < 20:
            mulheresJovens += 1

    # Verifica se mais pessoas vão ser adicionadas.
    while True:
        adcPessoa = str(input('Deseja adicionar mais alguma pessoa (y/n)? ')).lower().strip()
        if adcPessoa in ['y', 'n']:
            break
        else:
            print('\033[31mValor Inválido!\033[0m')

    print('\033[37m-\033[0m' * 40)

# Apresenta os dados finais.
print(f'1. Das \033[33m{c}\033[0m pessoas, \033[34m{adultos}\033[0m possuem mais do que \033[32m18 anos\033[0m;')
print(f'2. Das \033[33m{c}\033[0m pessoas, \033[34m{homens}\033[0m são \033[32mhomens\033[0m;')
print(f'3. Das \033[33m{mulheres}\033[0m mulheres, '
      f'\033[34m{mulheresJovens}\033[0m possuem menos do que \033[32m20 anos\033[0m.')

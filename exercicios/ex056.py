print('-=-' * 15, '\033[31mAnalizando a Idade Média, o Homem Mais Velho '
                  'e Quantas Mulheres Tem Menos de 20 Anos\033[m', '-=-' * 15)

# Escolhe quantas pessoas serão analizadas.
numPessoas = int(input('Quantas pessoas você deseja analizar? '))

# Pega os dados e os coloca nas suas respectivas listas.
# Separa a idade dos homens e das mulheres e pega o nome dos homens.
# Pega a média das idades.
nomes = []
idades = []
sexos = []
idadesMasculino = []
idadesFeminino = []
nomesMasculino = []
idadesSomadas = int(0)
for c in range(0, numPessoas):
    nomes.append(str(input(f'Digite o nome da {c + 1}º pessoa: ')).capitalize().strip())
    idades.append(int(input(f'Digite a idade da {c + 1}º pessoa: ')))
    sexos.append(str(input(f'Digite o sexo da {c + 1}º pessoa (M/F): ')).upper().strip())

    if sexos[c] == 'M':
        idadesMasculino.append(idades[c])
        nomesMasculino.append(nomes[c])
    elif sexos[c] == 'F':
        idadesFeminino.append(idades[c])
    else:
        print('\033[31mAlgum(s) dos valores digitados na categoria "sexo" é(são) inválido(s):\n'
              'Pode ser que o resultado não seja o esperado!')

    idadesSomadas = idadesSomadas + idades[c]
idadeMedia = idadesSomadas / numPessoas

# Pega o valor da maior idade masculina.
idadeMasculinoMaior = int
for c in range(0, len(idadesMasculino)):
    if c == 0:
        idadeMasculinoMaior = idadesMasculino[c]
    else:
        if idadeMasculinoMaior < idadesMasculino[c]:
            idadeMasculinoMaior = idadesMasculino[c]

# Pega o nome dos homens que possuem a maior idade.
nomesIdadeMasculinoMaior = []
for c in range(0, len(nomesMasculino)):
    if idadesMasculino[c] == idadeMasculinoMaior:
        nomesIdadeMasculinoMaior.append(nomesMasculino[c])

# Formata os nomes dos homens mais velhos em um str.
homensMaisVelhos = str
if len(nomesIdadeMasculinoMaior) > 1:
    ultimoNome = nomesIdadeMasculinoMaior[-1]
    del nomesIdadeMasculinoMaior[-1]
    if len(nomesIdadeMasculinoMaior) > 1:
        homensMaisVelhos = ', '.join(nomesIdadeMasculinoMaior)
    else:
        homensMaisVelhos = nomesIdadeMasculinoMaior[0]
    homensMaisVelhos = f'{homensMaisVelhos} e {ultimoNome}'
else:
    homensMaisVelhos = nomesIdadeMasculinoMaior[0]

# Verifica quantas mulheres tem menos de 20 anos.
mulheresJovens = int(0)
for c in range(0, len(idadesFeminino)):
    if idadesFeminino[c] < 20:
        mulheresJovens = mulheresJovens + 1

# Respostas conforme a quantidade de indivíduos.
print(f'A idade média dos \033[33m{numPessoas} indivíduos\033[0m é \033[34m{round(idadeMedia, 1)}\033[0m')
if len(nomesIdadeMasculinoMaior) > 1:
    print(f'Dos \033[33m{len(nomesMasculino)} homens\033[0m, os mais velhos são: \033[34m{homensMaisVelhos}\033[0m;')
elif len(nomesIdadeMasculinoMaior) == 1:
    print(f'\033[33m{homensMaisVelhos}\033[0m é o único homem;')
else:
    print('\033[31mNão há homens.')
if len(idadesFeminino) > 1:
    print(f'Das \033[33m{len(idadesFeminino)} mulheres\033[0m, \033[34m{mulheresJovens}\033[0m têm menos de 20 anos.')
elif len(idadesFeminino) == 1:
    print(f'De \033[33m{len(idadesFeminino)} mulher\033[0m, \033[34m{mulheresJovens}\033[0m tem menos de 20 anos.')
else:
    print('\033[31mNão há mulheres.')

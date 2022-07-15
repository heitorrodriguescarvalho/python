print('-=-' * 15, '\033[31mAnalizando a Idade Média, o Homem Mais Velho '
                  'e Quantas Mulheres Tem Menos de 20 Anos\033[m', '-=-' * 15)

# Escolhe quantas pessoas serão analizadas.
numPessoas = int(input('Quantas pessoas você deseja analizar? '))

# Pega os dados e os coloca nas suas respectivas listas.
nomes = []
idades = []
sexos = []
for c in range(0, numPessoas):
    nomes.append(str(input(f'Digite o nome da {c + 1}º pessoa: ')).capitalize().strip())
    idades.append(int(input(f'Digite a idade da {c + 1}º pessoa: ')))
    sexos.append(str(input(f'Digite o sexo da {c + 1}º pessoa (M/F): ')).upper().strip())

# Pega a média das idades
idadeMedia = float(0)
for c in range(0, numPessoas):
    idadeMedia = idadeMedia + idades[c]
idadeMedia = idadeMedia / numPessoas

# Separa a idade dos homens e das mulheres e pega o nome dos homens.
idadesMasculino = []
idadesFeminino = []
nomesMasculino = []

for c in range(0, numPessoas):
    if sexos[c] == 'M':
        idadesMasculino.append(idades[c])
        nomesMasculino.append(nomes[c])
    elif sexos[c] == 'F':
        idadesFeminino.append(idades[c])
    else:
        print('\033[31mAlgum(s) dos valores digitados na categoria "sexo" é(são) inválido(s):\n'
              'Pode ser que o resultado não seja o esperado!')

# Pega o valor da maior idade.
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
print(f'A idade média dos {numPessoas} indivíduos é {round(idadeMedia, 1)}')
if len(nomesIdadeMasculinoMaior) > 1:
    print(f'Dos {len(nomesMasculino)} homens, os mais velhos são: {homensMaisVelhos};')
elif len(nomesIdadeMasculinoMaior) == 1:
    print(f'Dos {len(nomesMasculino)} homens, o mais velhos é o {homensMaisVelhos};')
else:
    print('Não há homens.')
if len(idadesFeminino) > 1:
    print(f'Das {len(idadesFeminino)} mulheres, {mulheresJovens} possuem menos de 20 anos.')
elif len(idadesFeminino) == 1:
    print(f'Das {len(idadesFeminino)} mulheres, {mulheresJovens} possui menos de 20 anos.')
else:
    print('Não há mulheres.')

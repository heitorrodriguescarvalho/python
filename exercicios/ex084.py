print('-=-' * 15, '\033[31mLista Composta e Análise de Dados\033[m', '-=-' * 15)

dados = []
pessoas = []
cont = 0
while True:
    cont += 1
    print(cont)
    dados.append(str(input(f'Digite o nome da {cont}º pessoa: ')).strip().capitalize())
    dados.append(float(input(f'Digite o peso da {cont}º pessoa: ')))
    print('\033[37m-\033[0m' * 40)
    pessoas.append(dados[:])
    continuar = ''
    if cont == 1:
        maiorPeso = dados[1]
        menorPeso = dados[1]
    else:
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]
        elif dados[1] < menorPeso:
            menorPeso = dados[1]
    dados.clear()
    while continuar not in ['y', 'n']:
        continuar = str(input('Adicionar outra pessoa (y/n): ')).strip().lower()
    print('\033[37m-\033[0m' * 40)
    if continuar == 'n':
        break
pesados = []
leves = []
for c in range(0, len(pessoas)):
    if pessoas[c][1] == maiorPeso:
        pesados.append(str(pessoas[c][0]))
    elif pessoas[c][1] == menorPeso:
        leves.append(str(pessoas[c][0]))
print(f'Ao todo, foram cadastradas {len(pessoas)};')
print(f'O maior peso foi \033[34m{maiorPeso:.2f} Kg\033[0m. Possuem esse peso: \033[34m{pesados[1:-1]}\033[0m;')
print(f'O menor peso foi \033[34m{menorPeso:.2f} Kg\033[0m. Possuem esse peso: \033[34m{leves[1:-1]}\033[0m;')

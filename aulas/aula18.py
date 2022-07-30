dados = []
pessoas = []
adultos = 0

for c in range(0, 4):
    dados.append(str(input(f'Nome da {c+1}º pessoa: ')).strip().capitalize())
    dados.append(int(input(f'Idade da {c+1}º pessoa: ')))
    pessoas.append(dados[:])
    if dados[1] >= 18:
        adultos += 1
    dados.clear()
for c in range(0, len(pessoas)):
    print(f'{pessoas[c][0]} tem {pessoas[c][1]} anos.')
print(f'Logo concluímos que das {len(pessoas)} pessoas, {adultos} são adultos.')

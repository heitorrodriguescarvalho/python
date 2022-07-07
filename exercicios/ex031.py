km = float(input('Qual é a distância da sua viagem? '))

if km > 200:
    preco = km * 0.45
else:
    preco = km * 0.5

preco = str(round(preco, 2))
print(f'Sua viagem custará R${preco.replace(".", ",")}')

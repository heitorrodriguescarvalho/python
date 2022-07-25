print('-=-' * 15, '\033[31mLista de Preços com Tuplas\033[m', '-=-' * 15)

lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila',
         120.5, 'Canetas', 22.3, 'Livro', 34.9)

print('\033[37m-\033[0m' * 40)
print(f'\033[34m{"Listagem de Preços":>28}\033[0m')
print('\033[37m-\033[0m' * 40)

cont = 0
while cont < len(lista):
    print(f'{lista[cont]:.<30}R${lista[cont + 1]:>7.2f}')
    cont += 2
print('\033[37m-\033[0m' * 40)

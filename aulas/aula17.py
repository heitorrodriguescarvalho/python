lista = [4, 3, 5, 0]
lista.append(1)
print(lista)
lista.sort()
print(f'A lista em ordem fica: {lista}')
lista.sort(reverse=True)
print(f' A lista em ordem reversa fica: {lista}')

if lista[2] == 5:
    del lista[2]
    lista.insert(2, 8)
else:
    print('Não encontrei o valor 5 na posição 2.')

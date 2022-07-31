print('-=-' * 15, '\033[31mMais Sobre Matriz em Python\033[m', '-=-' * 15)

matriz = list()
for x in range(0, 3):
    for y in range(0, 3):
        matriz.append(int(input(f'Digite o valor de ({x}, {y}): ')))
matriz.sort()
print('\033[37m-\033[0m' * 40)
somaColuna3 = 0
for c in range(1, 10):
    if c % 3 == 0:
        print(f'[ {matriz[c-1]} ] ')
        somaColuna3 += matriz[c-1]
    else:
        print(f'[ {matriz[c-1]} ] ', end="")
print('\033[37m-\033[0m' * 40)
somaPares = 0
for pos, n in enumerate(matriz):
    if matriz[pos] % 2 == 0:
        somaPares += n
linha2 = [matriz[3], matriz[4], matriz[5]]
maiorLinha2 = max(linha2)
print(f'A soma dos valores pares é \033[34m{somaPares}\033[0m;')
print(f'A soma dos valores da terceira coluna é \033[34m{somaColuna3}\033[0m;')
print(f'O maior valor da segunda linha é \033[34m{maiorLinha2}\033[0m.')

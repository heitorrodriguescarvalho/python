print('-=-' * 15, '\033[31mMatriz em Python\033[m', '-=-' * 15)

matriz = list()
for x in range(0, 3):
    for y in range(0, 3):
        matriz.append(int(input(f'Digite o valor de ({x}, {y}): ')))
matriz.sort()
print('\033[37m-\033[0m' * 40)

for c in range(1, 10):
    if c % 3 == 0:
        print(f'[ {matriz[c-1]} ] ')
    else:
        print(f'[ {matriz[c-1]} ] ', end="")

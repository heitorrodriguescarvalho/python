print('-=-' * 15, '\033[31mSomando Valores\033[m', '-=-' * 15)

print('\033[31mAviso: para Parar digite "999"!\033[0m (O número "999" será desconsidarado na soma)')

soma = num = 0
while True:
    num = int(input('Digite um número a ser somado: '))
    if num == 999:
        break
    soma += num

print(f'A soma de todos os valores foi de \033[34m{soma}\033[0m.')

print('-=-' * 15, '\033[31mCalculando o Fatorial\033[m', '-=-' * 15)

num = int(input('Qual número deverá ter o fatorial calculado? '))

c = num
fatorial = num
while c > 1:
    c -= 1
    fatorialAntigo = fatorial
    fatorial *= c
    print(f'\033[33m{fatorialAntigo} x {c} \033[0m= \033[34m{fatorial}\033[0m')

print(f'O \033[33mfatorial\033[0m do número \033[33m{num}\033[0m é \033[34m{fatorial}\033[0m.')

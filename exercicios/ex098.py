from time import sleep

print('-=-' * 15, '\033[31mFunção de Contador\033[m', '-=-' * 15)


def count(first, last, step):
    print(f'Contagem de {first} a {last} de {step} em {step}:')
    if step == 0:
        step = 1
    if first > last:
        step = -step
        last = last - 2
    elif step * -1 > 0:
        step *= -1
    cont = 0
    for c in range(first, last + 1, step):
        cont += 1
        print(c, end=" ")
        sleep(0.3)
        if cont == 11:
            print()
            cont = 0
    print()
    print('\033[37m-\033[0m' * 38)


count(1, 10, 1)
count(10, 0, 2)
print('\033[34mContagem Personalizada\033[0m')
n1 = int(input('Início: '))
n2 = int(input('Final: '))
n3 = int(input('Passo: '))
print('\033[37m-\033[0m' * 38)
count(n1, n2, n3)

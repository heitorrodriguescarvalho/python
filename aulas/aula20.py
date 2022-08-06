def soma(num):
    print(f'A soma dos valores é \033[34m{sum(num)}\033[0m')


lista = list()
cont = 0
while True:
    cont += 1
    n = int(input(f'Adicione um valor (999 para parar): '))
    if n == 999:
        break
    else:
        lista.append(n)
soma(lista)

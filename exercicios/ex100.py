from random import randint
from time import sleep

print('-=-' * 15, '\033[31mFunções para Sortear e Somar\033[m', '-=-' * 15)


def sorteia(num):
    print('Foram sorteados os valores: ', end="")
    for c in range(0, 5):
        num.append(randint(1, 10))
        sleep(0.5)
        print(num[c], end=" ")
    print()


def somapar(lista):
    print('A soma de ', end="")
    soma = 0
    for n in lista:
        if n % 2 == 0:
            print(n, end=" ")
            soma += n
    print(f'é {soma}.')

numeros = list()
sorteia(numeros)
somapar(numeros)

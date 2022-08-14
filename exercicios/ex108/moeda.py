def aumentar(n, a):
    aumento = n * (a / 100)
    num = n + aumento
    return num


def diminuir(n, d):
    diminui = n * (d / 100)
    num = n - diminui
    return num


def metade(n):
    num = n / 2
    return num


def dobro(n):
    num = n * 2
    return num


def moeda(n):
    num = round(n, 2)
    num = str(num)
    if str(n)[-2] == '.':
        num = f'{n}0'
    num = num.replace('.', ',')
    return num

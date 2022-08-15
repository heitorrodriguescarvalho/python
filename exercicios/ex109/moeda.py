def aumentar(n, a, f=True):
    aumento = n * (a / 100)
    num = n + aumento
    if f:
        num = moeda(num)
    return num


def diminuir(n, d, f=True):
    diminui = n * (d / 100)
    num = n - diminui
    if f:
        num = moeda(num)
    return num


def metade(n, f=True):
    num = n / 2
    if f:
        num = moeda(num)
    return num


def dobro(n, f=True):
    num = n * 2
    if f:
        num = moeda(num)
    return num


def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')

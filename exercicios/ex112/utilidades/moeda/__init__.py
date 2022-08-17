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


def resumo(n, a, d):
    print('\033[37m-\033[m' * 30)
    print(f'            Resumo')
    print('\033[37m-\033[m' * 30)
    print(f'{"Preço:":<18} {moeda(n)}')
    print(f'{"Dobro:":<18} {dobro(n, True)}')
    print(f'{"Metade:":<18} {metade(n, True)}')
    print(f'{"Com aumento:":<18} {aumentar(n, a, True)}')
    print(f'{"Com desconto:":<18} {diminuir(n, d, True)}')

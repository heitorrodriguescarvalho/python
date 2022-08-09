def soma(a=0, b=0, c=0):
    """
    Soma os valores das variáveis
    :param a: Primeiro valor
    :param b: Segundo Valor
    :param c: Terceiro Valor
    :return: A soma de a, b e c
    """
    return a + b + c


a = int(input('Digite um valor: '))
b = int(input('Digite mais um valor: '))
c = int(input('Digite mais outro valor: '))
print(f'A soma de {a}, {b} e {c} é de {soma(a, b, c)}.')

print('-=-' * 15, '\033[31mAnalizando se é Possivel Formar um Triângulo e seu Tipo\033[m', '-=-' * 15)

r1 = float(input('Digite o comprimento da primeira reta:'))
r2 = float(input('Da segunda:'))
r3 = float(input('E da terceira:'))

if r2 - r3 < r1 < r2 + r3 and r1 - r3 < r2 < r1 + r3 and r1 - r2 < r3 < r1 + r2:
    print('Um triângulo com essas medidas pode existir.')

    if r1 == r2 and r2 == r3:
        print('Aliás, ele seria um Triângulo Equilátero.')

    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('Aliás, ele seria um Triângulo Isósceles.')

    else:
        print('Aliás, ele seria um Triângulo Escaleno')

else:
    print('Não é possível que um triângulo com essas medidas existam.')

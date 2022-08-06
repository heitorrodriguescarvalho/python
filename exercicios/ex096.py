print('-=-' * 15, '\033[31mFunção que Calcula Área\033[m', '-=-' * 15)


def area(com, lag):
    print(f'A área do terreno é de \033[34m{com * lag:.2f}m²\033[0m.')


comprimento = float(input('Comprimento (em metros): '))
largura = float(input('Largura (em metros): '))
area(comprimento, largura)

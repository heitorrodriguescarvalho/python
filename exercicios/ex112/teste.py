from utilidades import moeda, dado

print('-=-' * 15, '\033[31mTransformando Módulos em Pacotes\033[m', '-=-' * 15)

num = dado.leiadinheiro('Digite o preço: R$')
aumento = int(input('Qual será o aumento calculado: '))
while aumento < 0:
    print('\033[31mValor Inválido\033[0m')
    aumento = int(input('Qual será o aumento calculado: '))
diminui = int(input('Qual será a diminuição calculada: '))
while diminui < 0:
    print('\033[31mValor Inválido\033[0m')
    diminui = int(input('Qual será a diminuição calculada: '))
moeda.resumo(float(num.replace(',', '.')), aumento, diminui)

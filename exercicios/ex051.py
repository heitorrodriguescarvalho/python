print('-=-' * 15, '\033[31mRealizando uma Progressão Aritmética\033[m', '-=-' * 15)

numInicio = int(input('Digite o \033[33mnúmero inicial\033[0m da PA: '))
numRazao = int(input('Digite o \033[33mnúmero da razão\033[0m da PA: '))

pa = str(numInicio)

for c in range(0, 10):
    pa = pa + f', {numInicio + numRazao * (c + 1)}'

print(f'A PA de \033[33minício em {numInicio}\033[0m e de \033[33mrazão {numRazao}\033[0m obtém a seguinte progressão: \033[34m{pa}...')

from emoji import emojize

print('-=-' * 15, '\033[31mRealizando uma Progressão Aritmética\033[m', '-=-' * 15)

numInicio = int(input('Digite o \033[33mnúmero inicial\033[0m da PA: '))
numRazao = int(input('Digite o \033[33mnúmero da razão\033[0m da PA: '))
numMultiplos = int(input('Digite \033[33mnúmero de múltiplos\033[0m da PA: '))

progressao = numInicio
print(progressao, end='')
for c in range(0, numMultiplos):
    progressao += numRazao
    print(f' {emojize(":seta_para_a_direita:", language = "pt")} {progressao}', end="")

from emoji import emojize

print('-=-' * 15, '\033[31mRealizando uma Progressão Aritmética\033[m', '-=-' * 15)

numInicio = int(input('Por qual número a PA deve começar? '))
numRazao = int(input('Qual a razão da PA? '))
numCalc = int(10)

c = int(1)
pa = numInicio
print(f'\033[33m{pa}', end="")
while numCalc > 0:
    while c < numCalc:
        c += 1
        pa += numRazao
        print(emojize("\033[33m :seta_para_a_direita:", language="pt"), pa, end="")

    maisCalc = int(input('\n\033[0mDeseja calcular \033[32mmais quantos números\033[0m (0 para nenhum)? '))
    if maisCalc > 0:
        numCalc += maisCalc
    else:
        numCalc = 0
        print('\033[31mFinalizou o programa!')

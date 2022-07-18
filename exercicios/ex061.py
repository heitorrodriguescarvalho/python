from emoji import emojize

print('-=-' * 15, '\033[31mRealizando uma Progressão Aritmética\033[m', '-=-' * 15)

numInicio = int(input('Por qual número a PA deve começar? '))
numRazao = int(input('Qual a razão da PA? '))
numCalc = int(input('Quantos números devem ser calculados? '))

c = int(1)
pa = numInicio
print(pa, end="")
while c < numCalc:
    c += 1
    pa += numRazao
    print(emojize(" :seta_para_a_direita:", language="pt"), pa, end="")
